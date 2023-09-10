"""
Creates window with OpenGL Rendering Context.
Allows to draw to window with use of OpenGL functions.

To run window use `to_window().create_and_run(...)`.
"""

__author__  = "underwatergrasshopper"
__version__ = "0.1.1"

# This module and modules imported below are logically part of one module.
# Note: They are physically separated only for convenience.
from .Point         import *
from .Size          import *
from .Area          import *
from .Color         import *

from .Log           import *
from .Utility       import *
from .SpecialDebug  import *
from .Exceptions    import *

from .Font          import *
from .FineText      import *
from .TextAdjuster  import *
from .TextDrawer    import *
from .Key           import *
from .Window        import *
