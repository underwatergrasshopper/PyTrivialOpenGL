from ExampleManager import *

import area_and_state_debug
import simple_triangle
import window_area

example_manager = ExampleManager()

run_options = [        
    "disable_auto_sleep",
    "no_resize",
    "no_maximize",
    "centered",
    "draw_area_size",
    "draw_area_only",
    "redraw_on_request",
     
    "maximized",
    "minimized",
    "windowed_full_screened",
]

special_debug_options = [        
    "notify_remaining_messages",
    "notify_draw_call",
    "notify_mouse_move",
    "notify_key_message",
    "notify_character_message",
    "notify_timer",
    "full_exit_track_in_callback",
]

example_manager.add_example(
    "area_and_state_debug", 
    area_and_state_debug.run, 
    run_options + special_debug_options, 
    ["centered", "draw_area_size"]
)
example_manager.add_example("simple_triangle", simple_triangle.run)
example_manager.add_example("window_area", window_area.run)

def run():
    example_manager.set_default("area_and_state_debug")
    example_manager.run_examples()

if __name__ == "__main__":
   run()