from PyTrivialOpenGL_TestsAndExamples.utility.ExampleManager import ExampleManager
from PyTrivialOpenGL_TestsAndExamples import examples
from PyTrivialOpenGL_TestsAndExamples import debugs
from PyTrivialOpenGL_TestsAndExamples.tests import manual_tests

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
    "area_and_state", 
    debugs.area_and_state.run, 
    run_options + special_debug_options, 
    ["centered", "draw_area_size"]
)
example_manager.add_example(
    "mouse_and_keyboard", 
    debugs.mouse_and_keyboard.run, 
    run_options + special_debug_options, 
    ["centered", "draw_area_size"]
)

example_manager.add_example("winapi",           debugs.winapi.run,          ["min_max"])
example_manager.add_example("winapi_window",    debugs.winapi_window.run,   ["all_wm"])
example_manager.add_example("wgl_window",       debugs.wgl_window.run,      ["list_pixel_formats"])

example_manager.add_example("draw_array",       manual_tests.draw_array.run)
example_manager.add_example("draw_elements",    manual_tests.draw_elements.run)
example_manager.add_example("draw_rectangle",   manual_tests.draw_rectangle.run)
example_manager.add_example("matrix",           manual_tests.matrix.run)
example_manager.add_example("clip_plane",       manual_tests.clip_plane.run)
example_manager.add_example("light",            manual_tests.light.run)
example_manager.add_example("draw_pixels",      manual_tests.draw_pixels.run)
example_manager.add_example("draw_stipple",     manual_tests.draw_stipple.run)
example_manager.add_example("display_list",     manual_tests.display_list.run)

example_manager.add_example("simple_triangle",  lambda name, options: examples.simple_triangle.run())

def run():
    example_manager.set_default("area_and_state")
    example_manager.run_examples()

if __name__ == "__main__":
   run()