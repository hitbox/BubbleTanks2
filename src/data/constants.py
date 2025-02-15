from data.scripts import load_resolution


# screen
SCR_W, SCR_H = load_resolution()
SCR_W2 = SCR_W // 2
SCR_H2 = SCR_H // 2
SCR_SIZE = SCR_W, SCR_H
H_SCALE_FACTOR = SCR_H / 960
W_SCALE_FACTOR = SCR_W / 1280

# languages
ENGLISH = 0
RUSSIAN = 1

# screen modes
WINDOWED_MODE = 0
BORDERLESS_MODE = 1
FULLSCREEN_MODE = 2

# animation states
OPEN = 1
WAIT = 0
CLOSE = -1

# game
ROOM_RADIUS = int(7/6 * SCR_H)
DIST_BETWEEN_ROOMS = 2 * ROOM_RADIUS + SCR_W2
TRANSPORTATION_TIME = 600

# boss disposition states
BOSS_IS_FAR_AWAY = 0
BOSS_IN_NEIGHBOUR_ROOM = 1
BOSS_IN_CURRENT_ROOM = 2

# gun types
FIXED_GUN = 0
ROTATING_GUN = 1
AUTO_GUN = 2

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (51, 102, 204)
BLUE_GLARE_1 = (216, 225, 245)
BLUE_GLARE_2 = (79, 121, 210)
BUBBLE_COLOR = (40, 139, 213)
BUBBLE_COLOR_2 = (131, 201, 243)
BUBBLE_COLOR_3 = (119, 183, 220)
BUBBLE_GLARE_1 = (255, 255, 255)
BUBBLE_GLARE_2 = (127, 183, 232)
BUBBLE_GLARE_3 = (237, 245, 252)
BUBBLE_GLARE_4 = (182, 226, 247)
ORANGE = (210, 168, 0)
ORANGE_GLARE_1 = (255, 237, 166)
ORANGE_GLARE_2 = (251, 201, 0)
LIGHT_ORANGE = (235, 217, 143)
LIGHT_ORANGE_GLARE_1 = (255, 247, 216)
LIGHT_ORANGE_GLARE_2 = (253, 231, 143)
COLOR_KEY = (239, 239, 239)
RED = (210, 43, 0)
RED_GLARE_1 = (255, 209, 198)
RED_GLARE_2 = (255, 62, 12)
PINK = (255, 128, 128)
LIGHT_RED_2 = (244, 192, 179)
LIGHT_RED = (209, 85, 3)
LEECH_EFFECT_COLOR = (234, 6, 4)
VIOLET = (125, 12, 186)
VIOLET_GLARE_1 = (242, 223, 253)
VIOLET_GLARE_2 = (176, 67, 241)
PURPLE = (172, 199, 236)
PURPLE_GLARE_1 = (220, 235, 248)
PURPLE_GLARE_2 = (180, 204, 238)
GREY = (200, 200, 200)
GREY_2 = (170, 170, 170)
HIT_COLOR = (209, 244, 255)
UPG_LABEL_COLOR = (58, 170, 231)
PLAYER_BG_COLOR = (178, 220, 246)
PLAYER_BULLET_GLARE_1 = (255, 217, 179)
PLAYER_BULLET_GLARE_2 = (247, 131, 17)
ROOM_HIGHLIGHT_COLOR = (245, 252, 253, 100)
ROOM_COLOR = (192, 226, 250)
STATUS_BAR_BG = (232, 244, 253)
TANK_BG_COLOR = (124, 202, 231)
INFECTION_EDGE_COLOR = (255, 215, 195)
CONFUSION_COLOR = (117, 106, 146)
CONFUSION_EDGE_COLOR = (216, 180, 171)

CONFUSION_COLORS = [
    [(117, 106, 146), (216, 180, 171), (134, 117, 150)],
    [(95, 96, 203), (194, 170, 228), (112, 107, 207)],
    [(101, 163, 129), (200, 237, 154), (118, 174, 133)],
    [(132, 143, 122), (231, 217, 147), (149, 154, 126)],
    [(132, 61, 224), (231, 135, 249), (149, 72, 228)],
    [(132, 163, 224), (231, 237, 249), (149, 174, 228)],
    [(30, 61, 122), (129, 135, 147), (47, 72, 126)],
    [(71, 61, 183), (170, 135, 208), (88, 72, 187)],
    [(112, 143, 122), (211, 217, 147), (129, 154, 126)],
    [(30, 122, 142), (129, 196, 167), (47, 133, 146)],
]


COLORS = {
    "blue": BLUE,
    "orange": ORANGE,
    "light orange": LIGHT_ORANGE,
    "violet": VIOLET,
    "red": RED,
    "light red": LIGHT_RED,
    "light red 2": LIGHT_RED_2,
    "bubble color": BUBBLE_COLOR,
    "confusion": CONFUSION_COLOR
}


INFECTION_COLORS = {
    ORANGE: (255, 128, 0),
    BLUE: (201, 62, 144),
    RED: (255, 0, 0),
    LIGHT_ORANGE: (255, 177, 83)
}

GLARE_COLORS = {
    ORANGE:         [ORANGE_GLARE_1,        ORANGE_GLARE_2],
    BLUE:           [BLUE_GLARE_1,          BLUE_GLARE_2],
    BUBBLE_COLOR:   [BUBBLE_GLARE_1,        BUBBLE_GLARE_2],
    BUBBLE_COLOR_2: [BUBBLE_GLARE_3,        BUBBLE_GLARE_4],
    BUBBLE_COLOR_3: [BUBBLE_GLARE_3,        BUBBLE_GLARE_4],
    LIGHT_RED:       [PLAYER_BULLET_GLARE_1, PLAYER_BULLET_GLARE_2],
    VIOLET:         [VIOLET_GLARE_1,        VIOLET_GLARE_2],
    RED:            [RED_GLARE_1,           RED_GLARE_2],
    LIGHT_ORANGE:   [LIGHT_ORANGE_GLARE_1,  LIGHT_ORANGE_GLARE_2],
    PURPLE:         [PURPLE_GLARE_1,        PURPLE_GLARE_2],
    CONFUSION_COLOR: [(216, 180, 171), (134, 117, 150)]
}

INFECTION_GLARE_COLORS = {
    ORANGE_GLARE_1: (255, 197, 106),
    ORANGE_GLARE_2: (255, 161, 0),
    BLUE_GLARE_1: (255, 185, 185),
    BLUE_GLARE_2: (229, 81, 150),
    RED_GLARE_1: (255, 169, 138),
    RED_GLARE_2: (255, 0, 0),
    LIGHT_ORANGE_GLARE_1: (255, 208, 156),
    LIGHT_ORANGE_GLARE_2: (255, 192, 83)
}


__all__ = [

    "SCR_W",
    "SCR_H",
    "SCR_W2",
    "SCR_H2",
    "SCR_SIZE",
    "ENGLISH",
    "RUSSIAN",
    "OPEN",
    "CLOSE",
    "WAIT",
    "ROOM_RADIUS",
    "DIST_BETWEEN_ROOMS",
    "TRANSPORTATION_TIME",
    "BOSS_IS_FAR_AWAY",
    "BOSS_IN_NEIGHBOUR_ROOM",
    "BOSS_IN_CURRENT_ROOM",
    "H_SCALE_FACTOR",
    "W_SCALE_FACTOR",
    "BLACK",
    "WHITE",
    "BLUE",
    "BLUE_GLARE_1",
    "BLUE_GLARE_2",
    "BUBBLE_COLOR",
    "BUBBLE_COLOR_2",
    "BUBBLE_COLOR_3",
    "BUBBLE_GLARE_1",
    "BUBBLE_GLARE_2",
    "BUBBLE_GLARE_3",
    "BUBBLE_GLARE_4",
    "ORANGE",
    "ORANGE_GLARE_1",
    "ORANGE_GLARE_2",
    "LIGHT_ORANGE",
    "LIGHT_ORANGE_GLARE_1",
    "LIGHT_ORANGE_GLARE_2",
    "COLOR_KEY",
    "RED",
    "PINK",
    "RED_GLARE_1",
    "RED_GLARE_2",
    "LIGHT_RED_2",
    "LIGHT_RED",
    "LEECH_EFFECT_COLOR",
    "VIOLET",
    "VIOLET_GLARE_1",
    "VIOLET_GLARE_2",
    "PURPLE",
    "PURPLE_GLARE_1",
    "PURPLE_GLARE_2",
    "GREY",
    "GREY_2",
    "HIT_COLOR",
    "UPG_LABEL_COLOR",
    "PLAYER_BG_COLOR",
    "PLAYER_BULLET_GLARE_1",
    "PLAYER_BULLET_GLARE_2",
    "ROOM_HIGHLIGHT_COLOR",
    "ROOM_COLOR",
    "STATUS_BAR_BG",
    "TANK_BG_COLOR",
    "CONFUSION_COLOR",
    "CONFUSION_EDGE_COLOR",
    "INFECTION_EDGE_COLOR",
    "COLORS",
    "INFECTION_COLORS",
    "GLARE_COLORS",
    "INFECTION_GLARE_COLORS",
    "CONFUSION_COLORS",
    "WINDOWED_MODE",
    "BORDERLESS_MODE",
    "FULLSCREEN_MODE",
    "FIXED_GUN",
    "ROTATING_GUN",
    "AUTO_GUN"
    
]
