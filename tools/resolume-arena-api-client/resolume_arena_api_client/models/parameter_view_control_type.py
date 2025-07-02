from enum import Enum


class ParameterViewControlType(str, Enum):
    BASED_ON_PARAM = "based_on_param"
    CHOICE_BUTTONS = "choice_buttons"
    CHOICE_COMBOBOX = "choice_combobox"
    COLOR_PALLETTE = "color_pallette"
    COLOR_PICKER = "color_picker"
    DURATION_SPINNER = "duration_spinner"
    ROTARY = "rotary"
    SLIDER = "slider"
    SLIDER_COLOR_ALPHA = "slider_color_alpha"
    SLIDER_COLOR_BLUE = "slider_color_blue"
    SLIDER_COLOR_BRIGHTNESS = "slider_color_brightness"
    SLIDER_COLOR_GREEN = "slider_color_green"
    SLIDER_COLOR_HUE = "slider_color_hue"
    SLIDER_COLOR_OPACITY = "slider_color_opacity"
    SLIDER_COLOR_RED = "slider_color_red"
    SLIDER_COLOR_SATURATION = "slider_color_saturation"
    SPINNER = "spinner"
    TEXT = "text"
    TEXT_MULTILINE = "text_multiline"

    def __str__(self) -> str:
        return str(self.value)
