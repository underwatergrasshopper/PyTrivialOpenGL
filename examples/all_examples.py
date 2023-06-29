import PyTrivialOpenGL as togl
from ExampleManager     import *

################################################################################

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

example_manager = ExampleManager()

################################################################################

def run_window_example(name, options):
    togl.set_log_level(togl.LogLevel.DEBUG)

    window = togl.to_window()

    return window.create_and_run(
        icon_file_name = "tests\\assets\\icon.ico"
    )

example_manager.add_example("run_window", run_window_example)

################################################################################

def _main():
    example_manager.set_default("run_window")
    example_manager.run_examples()

if __name__ == "__main__":
   _main()