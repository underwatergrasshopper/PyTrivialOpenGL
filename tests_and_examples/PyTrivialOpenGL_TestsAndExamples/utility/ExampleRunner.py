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
        
        example_manager = ExampleManager()

        if category & ExampleCategoryBit.EXAMPLES:
           example_manager.add_example("simple_triangle",  lambda name, options: examples.simple_triangle.run())

        if category & ExampleCategoryBit.DEBUGS:
            example_manager.add_example("winapi",           debugs.winapi.run,          ["min_max"])
            example_manager.add_example("winapi_window",    debugs.winapi_window.run,   ["all_wm"])
            example_manager.add_example("wgl_window",       debugs.wgl_window.run,      ["list_pixel_formats"])

            example_manager.add_example(
                "area_and_state", 
                debugs.area_and_state.run, 
                self._run_options + self._special_debug_options, 
                ["centered", "draw_area_size"]
            )
            example_manager.add_example(
                "mouse_and_keyboard", 
                debugs.mouse_and_keyboard.run, 
                self._run_options + self._special_debug_options, 
                ["centered", "draw_area_size"]
            )

        if category & ExampleCategoryBit.MANUAL_TESTS:
            example_manager.add_example("draw_array",       manual_tests.draw_array.run)
            example_manager.add_example("draw_elements",    manual_tests.draw_elements.run)
            example_manager.add_example("draw_rectangle",   manual_tests.draw_rectangle.run)
            example_manager.add_example("matrix",           manual_tests.matrix.run)
            example_manager.add_example("clip_plane",       manual_tests.clip_plane.run)
            example_manager.add_example("light",            manual_tests.light.run)
            example_manager.add_example("draw_pixels",      manual_tests.draw_pixels.run)
            example_manager.add_example("draw_stipple",     manual_tests.draw_stipple.run)
            example_manager.add_example("display_list",     manual_tests.display_list.run)

        if default_example_name is None:
            if category & ExampleCategoryBit.MANUAL_TESTS:
                example_manager.set_default("display_list")

            if category & ExampleCategoryBit.DEBUGS:
                example_manager.set_default("area_and_state")

            if category & ExampleCategoryBit.EXAMPLES:
                example_manager.set_default("simple_triangle")
        else:
            example_manager.set_default(default_example_name)

        example_manager.run_examples()
