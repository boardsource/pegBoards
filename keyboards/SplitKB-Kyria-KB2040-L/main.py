import sys
from kb import KMKKeyboard
from kmk.hid import HIDModes
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.tapdance import TapDance
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled_display import (
    Oled,
    OledData,
    OledDisplayMode,
    OledReactionType,
)
from kmk.extensions.peg_rgb_matrix import Rgb_matrix, Color
from kmk.extensions.international import International

keyboard = KMKKeyboard()
keyboard.debug_enabled = True

# encodercount
# 2
# encodercount

encoder_handler = EncoderHandler()
encoder_handler.pins = ((keyboard.encoder_pin_0, keyboard.encoder_pin_1, None, False),)

keyboard.modules = [Layers(), ModTap(), TapDance()]
keyboard.extensions = [MediaKeys(), International()]

split = Split(split_type=SplitType.UART, use_pio=True, split_side=SplitSide.LEFT)
keyboard.modules.append(split)

# ledmap
rgb_ext = Rgb_matrix(
    ledDisplay=[
        Color.OFF,
        Color.OFF,
        Color.RED,
        Color.ORANGE,
        Color.OFF,
        Color.YELLOW,
        Color.GREEN,
        Color.BLUE,
        Color.PURPLE,
        Color.OFF,
        Color.OFF,
        Color.PURPLE,
        Color.BLUE,
        Color.GREEN,
        Color.YELLOW,
        Color.OFF,
        Color.ORANGE,
        Color.RED,
        Color.OFF,
        Color.OFF,
    ],
    split=True,
    rightSide=False,
    disable_auto_write=False,
)
# ledmap

keyboard.extensions.append(rgb_ext)

# oled
oled_ext = Oled(
    OledData(
        corner_one={
            0: OledReactionType.STATIC,
            1: ["Kyria v1", "", "", "", "", "", "", ""],
        },
        corner_two={
            0: OledReactionType.LAYER,
            1: [
                "QWERTY",
                "DVORAK",
                "COLEMAK-DH",
                "LOWER",
                "RAISE",
                "FUNC",
                "ADJUST",
                "",
            ],
        },
        corner_three={
            0: OledReactionType.STATIC,
            1: [sys.platform, "", "", "", "", "", "", ""],
        },
        corner_four={
            0: OledReactionType.STATIC,
            1: ["", "", "", "", "", "", "", ""],
        },
    ),
    toDisplay=OledDisplayMode.TXT,
    oHeight=64,
    flip=True,
)
# oled

keyboard.extensions.append(oled_ext)

# Edit your layout below
# Currently, that's a default QMK Kyria Layout - https://config.qmk.fm/#/splitkb/kyria/rev1/LAYOUT
ESC_LCTL = KC.MT(KC.ESC, KC.LCTL)
QUOTE_RCTL = KC.MT(KC.QUOTE, KC.RCTL)
ENT_LALT = KC.MT(KC.ENT, KC.LALT)
MINUS_RCTL = KC.MT(KC.MINUS, KC.RCTL)

# fmt: off
# keymap
keyboard.keymap = [
    [
        KC.TAB,        KC.Q,          KC.W,          KC.E,          KC.R,          KC.T,                                                                      KC.Y,          KC.U,          KC.I,          KC.O,          KC.P,          KC.BSPC,
        ESC_LCTL,      KC.A,          KC.S,          KC.D,          KC.F,          KC.G,                                                                      KC.H,          KC.J,          KC.K,          KC.L,          KC.SCLN,       QUOTE_RCTL,
        KC.LSFT,       KC.Z,          KC.X,          KC.C,          KC.V,          KC.B,          KC.LBRC,       KC.CAPS,       KC.MO(5),      KC.RBRC,       KC.N,          KC.M,          KC.COMM,       KC.DOT,        KC.SLSH,       KC.RSFT,
                                                     KC.MO(6),      KC.LGUI,       ENT_LALT,      KC.SPC,        KC.MO(3),      KC.MO(4),      KC.SPC,        KC.RALT,       KC.RGUI,       KC.APP,
    ],
    [
        KC.TAB,        KC.QUOT,       KC.COMM,       KC.DOT,        KC.P,          KC.Y,                                                                      KC.F,          KC.G,          KC.C,          KC.R,          KC.L,          KC.BSPC,
        ESC_LCTL,      KC.A,          KC.O,          KC.E,          KC.U,          KC.I,                                                                      KC.D,          KC.H,          KC.T,          KC.N,          KC.S,          MINUS_RCTL,
        KC.LSFT,       KC.SCLN,       KC.Q,          KC.J,          KC.K,          KC.X,          KC.LBRC,       KC.CAPS,       KC.MO(5),      KC.RBRC,       KC.B,          KC.M,          KC.W,          KC.V,          KC.Z,          KC.RSFT,
                                                     KC.MO(6),      KC.LGUI,       ENT_LALT,      KC.SPC,        KC.MO(3),      KC.MO(4),      KC.SPC,        KC.RALT,       KC.RGUI,       KC.APP,
    ],
    [
        KC.TAB,        KC.Q,          KC.W,          KC.F,          KC.P,          KC.B,                                                                      KC.J,          KC.L,          KC.U,          KC.Y,          KC.SCLN,       KC.BSPC,
        ESC_LCTL,      KC.A,          KC.R,          KC.S,          KC.T,          KC.G,                                                                      KC.M,          KC.N,          KC.E,          KC.I,          KC.O,          QUOTE_RCTL,
        KC.LSFT,       KC.Z,          KC.X,          KC.C,          KC.D,          KC.V,          KC.LBRC,       KC.CAPS,       KC.MO(5),      KC.RBRC,       KC.K,          KC.H,          KC.COMM,       KC.DOT,        KC.SLSH,       KC.RSFT,
                                                     KC.MO(6),      KC.LGUI,       ENT_LALT,      KC.SPC,        KC.MO(3),      KC.MO(4),      KC.SPC,        KC.RALT,       KC.RGUI,       KC.APP,
    ],
    [
        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,                                                    KC.PGUP,    KC.HOME,    KC.UP,      KC.END,     KC.VOLU,    KC.DEL,
        KC.TRNS,    KC.LGUI,    KC.LALT,    KC.LCTL,    KC.LSFT,    KC.TRNS,                                                    KC.PGDN,    KC.LEFT,    KC.DOWN,    KC.RGHT,    KC.VOLD,    KC.INS,
        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.SLCK,    KC.TRNS,    KC.TRNS,    KC.PAUS,    KC.MPRV,    KC.MPLY,    KC.MNXT,    KC.MUTE,    KC.PSCR,
                                            KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
    ],
    [
        KC.GRV,     KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,                                                      KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.EQL,
        KC.TILD,    KC.EXLM,    KC.AT,      KC.HASH,    KC.DLR,     KC.PERC,                                                    KC.CIRC,    KC.AMPR,    KC.ASTR,    KC.LPRN,    KC.RPRN,    KC.PLUS,
        KC.PIPE,    KC.BSLS,    KC.COLN,    KC.SCLN,    KC.MINS,    KC.LBRC,    KC.LCBR,    KC.TRNS,    KC.TRNS,    KC.RCBR,    KC.RBRC,    KC.UNDS,    KC.COMM,    KC.DOT,     KC.SLSH,    KC.QUES,
                                            KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
    ],
    [
        KC.TRNS,    KC.F9,      KC.F10,     KC.F11,     KC.F12,     KC.TRNS,                                                    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
        KC.TRNS,    KC.F5,      KC.F6,      KC.F7,      KC.F8,      KC.TRNS,                                                    KC.TRNS,    KC.RSFT,    KC.RCTL,    KC.LALT,    KC.RGUI,    KC.TRNS,
        KC.TRNS,    KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
                                            KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
    ],
    [
        KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.DF(0),      KC.TRNS,       KC.TRNS,                                                                   KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,
        KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.DF(1),      KC.TRNS,       KC.TRNS,                                                                   KC.RGB_TOG,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
        KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.DF(2),      KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
                                                     KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,
    ],
    [
        KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,      KC.TRNS,       KC.TRNS,                                                                   KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,
        KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,      KC.TRNS,       KC.TRNS,                                                                   KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
        KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,      KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
                                                     KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,
    ]
]
# keymap
# fmt: on

# Edit your encoder layout below
encoder_handler.map = (
    ((KC.VOLD, KC.VOLU),),
    ((KC.VOLD, KC.VOLU),),
    ((KC.VOLD, KC.VOLU),),
    ((KC.MPRV, KC.MNXT),),
    ((KC.MPRV, KC.MNXT),),
    ((KC.MPRV, KC.MNXT),),
    ((KC.MPRV, KC.MNXT),),
)

keyboard.extensions.append(encoder_handler)

if __name__ == "__main__":
    keyboard.go(hid_type=HIDModes.USB)
