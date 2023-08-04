from PyTrivialOpenGL_TestsAndExamples.utility.ExampleRunner import ExampleRunner, ExampleCategoryBit

def run():
    example_runner = ExampleRunner()
    example_runner.run(ExampleCategoryBit.ALL, "debug.area_and_state")

if __name__ == "__main__":
   run()