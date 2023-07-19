import re as _re
import os as _os

__all__ = [
    "Example",
    "ExampleManager",
]

class Example:
    def __init__(self, name, function, possible_options, default_options):
        """
        name                : str
        function            : Callable[[str, set[str]], int]
            Called as function(name, options).

        possible_options    : set[str]
        default_options     : set[str]
        """
        self.name               = name
        self.function           = function
        self.option_names       = possible_options if possible_options else []
        self.possible_options   = set(possible_options) if possible_options else set()
        self.default_options    = default_options

    def def_opt_to_str(self):
        text = ""
        for option in self.default_options:
            if text != "":
                text += " "
            text += option
        return text

class ExampleManager:
    """
    examples                : dict[str, Example]
    default_example_name    : str
    """
    def __init__(self):
        self.example_names          = []
        self.examples               = {}
        self.default_example_name   = ""

    def set_default(self, default_example_name):
        """
        default_example_name    : str
        """
        self.default_example_name = default_example_name

    def add_example(self, name, function, possible_options = None, default_options = None):
        """
        name                : str
        function            : Callable[[str, set[str]], NoneType]
        possible_options    : set[str]
        possible_options    : set[str]
        """

        if default_options == None:
            default_options = set()
        else:
            default_options = set(default_options)

        self.example_names.append(name)
        self.examples[name] = Example(name, function, possible_options, default_options)

    def _display_examples(self):
        max_len = max(len(example_name) for example_name in self.example_names)
        max_len += 2 # offset for ', '
        offset = 4 + 1 # 'tab' + '\n'
        max_num_of_columns = max(1, (_os.get_terminal_size().columns - offset) // max_len)

        if len(self.example_names) > 0:
            print("    ", end = "")

        count = 0
        for example_name in self.example_names:
            print("%-*s" % (max_len, example_name + ", "), end = "")
            count +=1
            if count % max_num_of_columns == 0 and count != len(self.example_names):
                print("\n    ", end = "")
        print("")

    def _display_possible_options(self, example):
        max_len = max(len(option) for option in example.option_names) if len(example.option_names) > 0 else 0
        max_len += 2 # offset for ', '
        offset = 4 + 1 # 'tab' + '\n'
        max_num_of_columns = max(1, (_os.get_terminal_size().columns - offset) // max_len)
        
        if len(self.examples) > 0:
            print("    ", end = "")

        count = 0
        for option in example.option_names:
            print("%-*s" % (max_len, option + ", "), end = "")
            count +=1
            if count % max_num_of_columns == 0 and count != len(example.option_names):
                print("\n    ", end = "")
        print("")

    def run_examples(self):
        while True:
            print("--- Example Manager ---")
            print("Examples:")
            self._display_examples()
            print("")

            print("(type example name)")
            print("(e=Exit, d=%s)" % self.default_example_name)
            example_name = input("Select: ")
            print("")

            if example_name == "e":
                exit(0)

            elif example_name == "d":
                example_name = self.default_example_name

            example = self.examples.get(example_name, None)
            if example:
                print("Options:")
                self._display_possible_options(example)
                print("")

                print("(type one or multiple options names)")
                print("(e=Exit, d=%s)" % example.def_opt_to_str())
                raw_options = input("Select: ")
                print("")

                raw_options = _re.split(r"[\t\n ]+", raw_options)

                options = set()
                
                if raw_options == ["e"]:
                    exit(0)

                elif raw_options == ["d"]:
                    options = example.default_options

                elif raw_options != [""]:
                    options = set(raw_options)

                is_valid_option = True
                for option in options:
                    if option not in example.possible_options:
                        is_valid_option = False
                        print("Error: Option '%s' does not exist." % option)
                        break

                if is_valid_option:
                    result = example.function(example_name, options)
                    print("")
                    print("Example ended with result code: %d." % result)
            else:
                print("Error: Example '%s' do not exist in expected options." % example_name)
                
            print("")