if __name__ == "__main__":
   import _setup_path_env
   _setup_path_env.run()
   
from PyTrivialOpenGL_TestsAndExamples.utility.ExampleManager import ExampleManager

example_manager = ExampleManager()

def run():
    def example_1(name, options):
        print(name, options)
        return 0

    def example_2(name, options):
        print(name, options)
        return 0

    def example_3(name, options):
        print(name, options)
        return 0

    def example_4(name, options):
        print(name, options)
        return 0

    def example_5(name, options):
        print(name, options)
        return 0
        
    example_manager.set_default("example_2")

    example_manager.add_example("example_1", example_1)
    example_manager.add_example("example_2", example_2, ["a"])
    example_manager.add_example("example_3", example_3, ["a", "c", "d", "e", "f"])
    example_manager.add_example("example_4", example_4, ["a", "c", "d", "e", "f"], ["a", "d"])
    example_manager.add_example("example_5", example_5)

    example_manager.run_examples()

if __name__ == "__main__":
    run()