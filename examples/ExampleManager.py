import re as _re

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
        possible_options    : set[str]
        """
        self.name               = name
        self.function           = function
        self.possible_options   = possible_options
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
        
        if possible_options == None:
            possible_options = set()
        else:
            possible_options = set(possible_options)

        if default_options == None:
            default_options = set()
        else:
            default_options = set(default_options)

        self.examples[name] = Example(name, function, possible_options, default_options)

    def _display_examples(self):
        count = 0
        for example_name in self.examples.keys():
            print("% 19s, " % example_name, end = "")
            count +=1
            if count % 4 == 0:
                print("")
        print("")

    def _display_possible_options(self, example):
        count = 0
        for option in example.possible_options:
            print("% 19s, " % option, end = "")
            count +=1
            if count % 4 == 0:
                print("")
        print("")

    def run_examples(self):
        while True:
            print("--- Example Manager ---")
            print("Examples:")
            self._display_examples()
            print("")

            print("(e=Exit, d=%s)" % self.default_example_name)
            example_name = input("select example: ")
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

                print("(e=Exit, d=%s)" % example.def_opt_to_str())
                raw_options = input("select options: ")
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