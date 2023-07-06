from ExampleManager import *

import area_and_state_debug
import simple_triangle
import window_area

example_manager = ExampleManager()

example_manager.add_example("area_and_state_debug", area_and_state_debug.run)
example_manager.add_example("simple_triangle", simple_triangle.run)
example_manager.add_example("window_area", window_area.run)

def run():
    example_manager.set_default("area_and_state_debug")
    example_manager.run_examples()

if __name__ == "__main__":
   run()