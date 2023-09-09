if __name__ == "__main__":
   import _setup_path_env
   _setup_path_env.run()
   

import os as _os
import PyTrivialOpenGL_TestsAndExamples.tests.unit_tests as _unit_tests

def run():
    output_rel_path = _os.path.relpath(_os.path.dirname(__file__) + "/../log/unit_tests")
    _unit_tests.run([], output_rel_path)

if __name__ == "__main__":
    run()