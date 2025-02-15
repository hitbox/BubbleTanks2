class MainMenuStates:
    SPLASH_SCREEN = 0
    MAIN_PAGE = 1
    SETTINGS = 2
    CREDITS = 3
    LANGUAGES = 4
    RESOLUTIONS = 5
    SCREEN_MODES = 6
    EXIT = 7
    NEW_GAME = 8
    LOAD_GAME = 9
    OVERRIDE_SAVE = 10
    DELETE_SAVE = 11


class PauseMenuStates:
    STATS = 0
    MAP = 1
    OPTIONS = 2
    DIALOG_MENU = 3
    DIALOG_DESKTOP = 4
    SCREEN_MODES = 5


class UpgradeMenuStates:
    MAIN_STATE = 0


class VictoryMenuStates:
    MAIN_STATE = 0


class UpgradeButtonType:
    LEFT = 0
    CENTER = 1
    RIGHT = 2
    WIDE_LEFT = 3
    WIDE_RIGHT = 4


class PopupWindowStates:
    CLOSED = 0
    OPENING = 1
    CLOSING = 2
    OPENED = 3


__all__ = [

    "MainMenuStates",
    "PauseMenuStates",
    "UpgradeMenuStates",
    "VictoryMenuStates",
    "UpgradeButtonType",
    "PopupWindowStates"

]