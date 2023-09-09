"""
run_unit_tests.py [<test_script_name>[::<test_function_name>] ...]

Note: Similarly to how pytest is doing this.

Examples:
   run_unit_tests.py test_area.py
   run_unit_tests.py test_area.py test_basics.py
   run_unit_tests.py test_area.py::test_area
"""

if __name__ == "__main__":
   import _setup_path_env
   _setup_path_env.run()
   
import os as _os
import PyTrivialOpenGL_TestsAndExamples.tests.unit_tests as _unit_tests

def main(argv = None):
   """
   argv : list[str] | None
      List of test script file names. They can be extended with test function name. 
      Similarly to how pytest is doing this: '<test_script_name>[::<test_function_name>]'.
      Examples:
         test_area.py
         test_area.py::test_area
   """
   if argv is not None and not (isinstance(argv, list) and all(isinstance(item, str) for item in argv)):
      raise TypeError("Unexpected type of 'argv' parameter.")
   
   _main(argv if argv else [])

def run(targets = None):
   """
   targets : list[str] | None
      List of test script file names. They can be extended with test function name. 
      Similarly to how pytest is doing this: '<test_script_name>[::<test_function_name>]'.
      Examples:
         test_area.py
         test_area.py::test_area
   """
   if targets is not None and not (isinstance(targets, list) and all(isinstance(item, str) for item in targets)):
      raise TypeError("Unexpected type of 'targets' parameter.")
   
   _run(targets)

def _main(argv):
   """
   argv : list[str]
   """
   _run(argv[1:])


def _run(targets):
   """
   targets : list[str]
   """
   output_rel_path = _os.path.relpath(_os.path.dirname(__file__) + "/../log/unit_tests")
   _unit_tests.run(targets, output_rel_path)

if __name__ == "__main__":
   import sys as _sys 

   _main(_sys.argv)