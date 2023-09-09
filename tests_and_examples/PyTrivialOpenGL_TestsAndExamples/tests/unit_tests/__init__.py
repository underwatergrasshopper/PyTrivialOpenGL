import pytest as _pytest
import os as _os

def run(targets = None, output_path = None):
    """
    targets         : list[str] | None
        List of test script files. Similar to how pytest is doing this.
        [<test_script_name>[::<test_function_name>] ...]
    output_path     : str | None
    run_path        : str | None
    """
    if targets is not None and not (isinstance(targets, list) and all(isinstance(item, str) for item in targets)):
        raise TypeError("Unexpected type of 'targets' parameter.")
    
    if targets is not None and not isinstance(output_path, str):
        raise TypeError("Unexpected type of 'output_path' parameter.")
    
    _run(targets, output_path)


def _run(targets, output_path):
    """
    targets         : list[str]
    output_path     : str
    """
    base_path = _os.path.relpath(_os.path.dirname(__file__)) + "/"

    if targets:
        targets = [base_path + target for target in targets]
    else:
        targets = [base_path]

    options = "--no-header -v -x".split(" ")
    if output_path:
        options += ["--basetemp=" + output_path]

    _pytest.main(targets + options)
