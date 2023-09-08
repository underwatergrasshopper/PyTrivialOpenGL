if __name__ == "__main__":
   import _setup_path_env
   _setup_path_env.run()

from PyTrivialOpenGL_TestsAndExamples.utility.ExampleRunner import ExampleRunner, ExampleCategoryBit

def run():
    example_runner = ExampleRunner()
    example_runner.run(ExampleCategoryBit.ALL, "debug.area_and_state")

if __name__ == "__main__":
    import sys as _sys
    for entry in _sys.path:
        print(entry)
    run()