# openwebui-cut-context

a filter function for **open-webui** to *cut the context of historical conversation turns*.

You can install this filter function by importing [https://openwebui.com/f/grayxu/cut_context](https://openwebui.com/f/grayxu/cut_context)

**NOTE**

Due to the limitations of functions, you are unable to set different function values for different models.  

A compromise is to preset some commonly used thresholds as individual functions in advance.  

Additionally, although the cut threshold set in the model settings cannot be altered individually, it can be changed at any time through user settings, and the filter will utilize the minimum value.