import re       as _re
import os       as _os
import pathlib  as _pathlib 
import inspect  as _inspect

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
    _example_names          : list[str]
    _examples               : dict[str, Example]
    _default_example_name   : str
    _output_path            : str
    _register_path          : str
    """
    def __init__(self):
        self._example_names         = []
        self._examples              = {}
        self._default_example_name  = ""

        self.set_output_path("")

    def set_output_path(self, output_path):
        """
        log_path_root : str
        """
        self._output_path = output_path
        
        if self._output_path:
            self._register_path = self._output_path + "/"
        else:
            self._register_path = ""

        self._register_path += "ExampleManager"

    def set_default(self, default_example_name):
        """
        default_example_name    : str
        """
        self._default_example_name = default_example_name

    def add_example(self, name, function, possible_options = None, default_options = None):
        """
        name                : str
        function            : Callable[...], None]
            Optional parameters of ...:
                name : str
                    Name of test.
                options : set[str]
                    Options of test.
                output_path : str
                    Path for creating files in it.

            Note: It can be one, many or none of those parameters.

        possible_options    : set[str]
        possible_options    : set[str]
        """

        if default_options == None:
            default_options = set()
        else:
            default_options = set(default_options)

        self._example_names.append(name)
        self._examples[name] = Example(name, function, possible_options, default_options)

    def _display_examples(self):
        max_len = max(len(example_name) for example_name in self._example_names)
        max_len += 2 # offset for ', '
        offset = 4 + 1 # 'tab' + '\n'
        max_num_of_columns = max(1, (_os.get_terminal_size().columns - offset) // max_len)

        if len(self._example_names) > 0:
            print("    ", end = "")

        count = 0
        for example_name in self._example_names:
            print("%-*s" % (max_len, example_name + ", "), end = "")
            count +=1
            if count % max_num_of_columns == 0 and count != len(self._example_names):
                print("\n    ", end = "")
        print("")

    def _display_possible_options(self, example):
        max_len = max(len(option) for option in example.option_names) if len(example.option_names) > 0 else 0
        max_len += 2 # offset for ', '
        offset = 4 + 1 # 'tab' + '\n'
        max_num_of_columns = max(1, (_os.get_terminal_size().columns - offset) // max_len)
        
        if len(self._examples) > 0:
            print("    ", end = "")

        count = 0
        for option in example.option_names:
            print("%-*s" % (max_len, option + ", "), end = "")
            count +=1
            if count % max_num_of_columns == 0 and count != len(example.option_names):
                print("\n    ", end = "")
        print("")

    def _log_text(self, text, file_name):
        _pathlib.Path(self._register_path).mkdir(parents = True, exist_ok = True)
        with open(self._register_path + "\\" + file_name, "w") as file:
            file.write(text)

    def _load_text(self, file_name):
        _pathlib.Path(self._register_path).mkdir(parents = True, exist_ok = True)

        file_name = self._register_path + "\\" + file_name

        if _os.path.isfile(file_name):
            with open(file_name, "r") as file:
                return file.read().strip()
        return None

    def run_examples(self):
        while True:
            print("--- Example Manager ---")
            print("Examples:")
            self._display_examples()
            print("")

            last_example_name = self._load_text("last_example_name.txt")

            print("(type example name)")
            if last_example_name is not None:
                print("(e=Exit, d=%s, l=%s)" % (self._default_example_name, last_example_name))
            else:
                print("(e=Exit, d=%s)" % self._default_example_name)
            example_name = input("Select: ")
            print("")

            if example_name == "e":
                exit(0)

            elif example_name == "d":
                example_name = self._default_example_name

            elif example_name == "l" and last_example_name is not None:
                example_name = last_example_name

            example = self._examples.get(example_name, None)
            if example:
                if example.name != last_example_name:
                    self._log_text(example.name, "last_example_name.txt")

                print("Options:")
                self._display_possible_options(example)
                print("")

                last_option_names = self._load_text("last_option_names.txt")

                print("(type one or multiple options names)")
                if last_option_names is not None:
                    print("(e=Exit, d=%s, l=%s)" % (example.def_opt_to_str(), last_option_names))
                    last_option_names = set(last_option_names.split(" ")) if last_option_names != "" else set()
                else:
                    print("(e=Exit, d=%s)" % example.def_opt_to_str())

                raw_options = input("Select: ")
                print("")

                raw_options = _re.split(r"[\t\n ]+", raw_options)

                options = set()
                
                if raw_options == ["e"]:
                    exit(0)

                elif raw_options == ["d"]:
                    options = example.default_options

                elif raw_options == ["l"] and last_option_names is not None:
                    options = last_option_names

                elif raw_options != [""]:
                    options = set(raw_options)


                is_valid_option = True
                for option in options:
                    if option not in example.possible_options:
                        is_valid_option = False
                        print("Error: Option '%s' does not exist." % option)
                        break

                if is_valid_option:
                    self._log_text(" ".join(options), "last_option_names.txt")

                    args = _inspect.getfullargspec(example.function).args
                    kwargs = {}
                    if "name" in args:          kwargs["name"]          = example_name
                    if "options" in args:       kwargs["options"]       = options
                    if "output_path" in args:   kwargs["output_path"]   = self._output_path

                    result = example.function(**kwargs)

                    print("")
                    print("Example ended with result code: %d." % result)
            else:
                print("Error: Example '%s' do not exist in expected options." % example_name)
                
            print("")