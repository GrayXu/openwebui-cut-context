"""
title: Cut the context of historical conversation turns

author: grayxu
author_url: https://github.com/grayxu
funding_url: https://github.com/grayxu
version: 0.1
"""

from pydantic import BaseModel, Field
from typing import Optional


class Filter:
    class Valves(BaseModel):
        priority: int = Field(
            default=0, description="Priority level for the filter operations."
        )
        header_turns: int = Field(
            default=4, description="Maximum number of conversation header turns allowed by the user."
        )
        tail_turns: int = Field(
            default=4, description="Maximum number of conversation tail turns allowed by the user."
        )
        pass

    class UserValves(BaseModel):
        header_turns: int = Field(
            default=4, description="Maximum number of conversation header turns allowed by the user."
        )
        tail_turns: int = Field(
            default=4, description="Maximum number of conversation tail turns allowed by the user."
        )
        pass

    def __init__(self):
        self.valves = self.Valves()
        pass

    def inlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        print(f"inlet:{__name__}")
        print(f"inlet:body:{body}")
        print(f"inlet:user:{__user__}")

        if __user__.get("role", "admin") in ["user", "admin"]:
            messages = body.get("messages", [])

            # Calculate max turns for the user
            header_turns = min(__user__["valves"].header_turns, self.valves.header_turns)
            tail_turns = min(__user__["valves"].tail_turns, self.valves.tail_turns)

            num_head = header_turns * 2
            num_tail = 1 + tail_turns * 2  # 1 for the role input

            # Cut the messages
            if len(messages) > num_head + num_tail:
                body["messages"] = messages[:num_head] + messages[-num_tail:]

        return body

    def outlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        print(f"outlet:{__name__}")
        print(f"outlet:body:{body}")
        print(f"outlet:user:{__user__}")

        return body
