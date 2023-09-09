if __name__ == "__main__":
   import _setup_path_env
   _setup_path_env.run()
   
import os as _os
from PyTrivialOpenGL_TestsAndExamples.utility.ExampleRunner import ExampleRunner, ExampleCategoryBit

def run():
    example_runner = ExampleRunner()
    output_path = _os.path.abspath(_os.path.dirname(__file__) + "/../out")
    example_runner.run(ExampleCategoryBit.EXAMPLES, output_path = output_path)

if __name__ == "__main__":
   run()