import os as _os

from .ExampleManager import ExampleManager

from ..         import examples
from ..         import debugs
from ..tests    import manual_tests

__all__ = [
    "ExampleCategoryBit",
    "ExampleRunner",
]

class ExampleCategoryBit:
    EXAMPLES        = 0x01
    DEBUGS          = 0x02
    MANUAL_TESTS    = 0x04

    ALL             = EXAMPLES | DEBUGS | MANUAL_TESTS

class ExampleRunner:
    def __init__(self):
        self._run_options = [        
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
            
            "disable_auto_sleep",
            "hidden",

            "opengl_3_3",
            "no_icon",
            "alt_center",
            "ask_on_close",

            "show_fps",
        ]

        self._special_debug_options = [        
            "notify_remaining_messages",
            "notify_draw_call",
            "notify_mouse_move",
            "notify_key_message",
            "notify_character_message",
            "notify_timer",
            "full_exit_track_in_callback",
        ]

    def run(self, category, default_example_name = None):
        """
        category                : int
            Bitfield made of 'ExampleCategoryBit' value or 0.
        default_example_name    : str | None
        """

        if not _os.path.exists("out"):
            _os.makedirs("out")
        
        example_manager = ExampleManager()

        if category & ExampleCategoryBit.EXAMPLES:
           example_manager.add_example("simple_triangle",  lambda name, options: examples.simple_triangle.run())

        if category & ExampleCategoryBit.DEBUGS:
            example_manager.add_example("debug.winapi",           debugs.winapi.run,          ["min_max"])
            example_manager.add_example("debug.winapi_window",    debugs.winapi_window.run,   ["all_wm"])
            example_manager.add_example("debug.wgl_window",       debugs.wgl_window.run,      ["list_pixel_formats"])

            example_manager.add_example(
                "debug.area_and_state", 
                debugs.area_and_state.run, 
                self._run_options + self._special_debug_options, 
                ["centered", "draw_area_size"]
            )
            example_manager.add_example(
                "debug.mouse_and_keyboard", 
                debugs.mouse_and_keyboard.run, 
                self._run_options + self._special_debug_options, 
                ["centered", "draw_area_size"]
            )

        if category & ExampleCategoryBit.MANUAL_TESTS:
            example_manager.add_example("mt.draw_array",        manual_tests.draw_array.run,        ["inter", "stride"])
            example_manager.add_example("mt.draw_elements",     manual_tests.draw_elements.run)
            example_manager.add_example("mt.draw_rectangle",    manual_tests.draw_rectangle.run)
            example_manager.add_example("mt.matrix",            manual_tests.matrix.run)
            example_manager.add_example("mt.clip_plane",        manual_tests.clip_plane.run)
            example_manager.add_example("mt.light_and_fog",     manual_tests.light_and_fog.run)
            example_manager.add_example("mt.draw_pixels",       manual_tests.draw_pixels.run)
            example_manager.add_example("mt.draw_stipple",      manual_tests.draw_stipple.run)
            example_manager.add_example("mt.display_list",      manual_tests.display_list.run)
            example_manager.add_example("mt.draw_texture",      manual_tests.draw_texture.run,      ["float", "1d", "sub", "vec", "fps"]),
            example_manager.add_example("mt.bezier_curve",      manual_tests.bezier_curve.run)
            example_manager.add_example("mt.bezier_surface",    manual_tests.bezier_surface.run)
            example_manager.add_example("mt.c_selection",       manual_tests.c_selection.run)
            example_manager.add_example("mt.selection",         manual_tests.selection.run)
            example_manager.add_example("mt.c_feedback",        manual_tests.c_feedback.run)
            example_manager.add_example("mt.feedback",          manual_tests.feedback.run)
            example_manager.add_example("mt.draw_font",         manual_tests.draw_font.run,         ["debug", "plane_0", "export", "show_fps", "left_top"])
            example_manager.add_example("mt.draw_text",         manual_tests.draw_text.run,         ["debug", "plane_0", "export", "show_fps", "left_top"])

        if default_example_name is None:
            if category & ExampleCategoryBit.MANUAL_TESTS:
                example_manager.set_default("mt.display_list")

            if category & ExampleCategoryBit.DEBUGS:
                example_manager.set_default("debug.area_and_state")

            if category & ExampleCategoryBit.EXAMPLES:
                example_manager.set_default("simple_triangle")
        else:
            example_manager.set_default(default_example_name)

        example_manager.run_examples()
