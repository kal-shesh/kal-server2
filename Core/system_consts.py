import sys
is_windows = hasattr(sys, 'getwindowsversion')

if is_windows:
    PATH_SEPARATOR = "\\"
else:
    PATH_SEPARATOR = "/"
