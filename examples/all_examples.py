from ExampleManager import *

import debug_area_and_state
import debug_mouse_and_keyboard
import simple_triangle
import window_area
import example_draw_array
import example_draw_elements
import example_draw_rectangle
import example_matrix
import example_clip_plane
import example_light
import example_draw_pixels
import example_draw_stipple
import example_display_list

example_manager = ExampleManager()

run_options = [        
    "disable_auto_sleep",
    "no_resize",
    "no_maximize",
    "centered",
    "draw_area_size",
    "draw_area_only",
    "redraw_on_request",

    "no_debug",
     
    "maximized",
    "minimized",
    "windowed_full_screened",

    "hidden",

    "opengl_3_3",
    "no_icon",
    "alt_center",
    "ask_on_close",

    "show_fps",
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
    debug_area_and_state.run, 
    run_options + special_debug_options, 
    ["centered", "draw_area_size"]
)
example_manager.add_example(
    "mouse_and_keyboard_debug", 
    debug_mouse_and_keyboard.run, 
    run_options + special_debug_options, 
    ["centered", "draw_area_size"]
)
example_manager.add_example("simple_triangle", simple_triangle.run)
example_manager.add_example("window_area", window_area.run)
example_manager.add_example("draw_array", example_draw_array.run)
example_manager.add_example("draw_elements", example_draw_elements.run)
example_manager.add_example("draw_rectangle", example_draw_rectangle.run)
example_manager.add_example("matrix", example_matrix.run)
example_manager.add_example("clip_plane", example_clip_plane.run)
example_manager.add_example("light", example_light.run)
example_manager.add_example("draw_pixels", example_draw_pixels.run)
example_manager.add_example("draw_stipple", example_draw_stipple.run)
example_manager.add_example("display_list", example_display_list.run)

def run():
    example_manager.set_default("area_and_state_debug")
    example_manager.run_examples()

if __name__ == "__main__":
   run()