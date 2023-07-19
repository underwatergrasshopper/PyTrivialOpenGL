from . import test_basics
from . import test_color
from . import test_size
from . import test_point
from . import test_area
from . import test_logger
from . import test_log
from . import test_key
from . import test_window

def run():
    test_basics.run()
    test_color.run()
    test_size.run()
    test_point.run()
    test_area.run()
    test_logger.run()
    test_log.run()
    test_key.run()
    test_window.run()