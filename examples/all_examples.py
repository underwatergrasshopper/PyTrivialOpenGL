from PyTrivialOpenGL    import *
from ExampleManager     import *

################################################################################

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

example_manager = ExampleManager()

################################################################################

def run_window_example(name, options):
    window = to_window()

    return window.create_and_run(area = Area(MAX_I32, MIN_I32, MAX_U16, MIN_U16))

example_manager.add_example("run_window", run_window_example)

################################################################################

def _main():
    example_manager.set_default("run_window")
    example_manager.run_examples()

if __name__ == "__main__":
   _main()