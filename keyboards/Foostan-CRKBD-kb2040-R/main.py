from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.hid import HIDModes
from kmk.handlers.sequences import send_string
import supervisor
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData
from kmk.extensions.peg_rgb_matrix import Rgb_matrix
from kmk.modules.split import Split, SplitSide, SplitType
keyboard = KMKKeyboard()
modtap = ModTap()
layers_ext = Layers()
keyboard.modules.append(layers_ext)
keyboard.modules.append(modtap)
# oled
oled_ext = Oled(OledData(corner_one={0:OledReactionType.LAYER,1:["","","","","","","",""]},corner_two={0:OledReactionType.LAYER,1:["","","","","","","",""]},corner_three={0:OledReactionType.LAYER,1:["","","","","","","",""]},corner_four={0:OledReactionType.LAYER,1:["","","","","","","",""]}),toDisplay=OledDisplayMode.TXT,flip=False)
# oled
keyboard.extensions.append(oled_ext)
# ledmap
rgb_ext = Rgb_matrix(ledDisplay=[[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255]],split=True,rightSide=True,disable_auto_write=True)
# ledmap
keyboard.extensions.append(rgb_ext)
# TODO Comment one of these on each side
#split_side = SplitSide.LEFT
#split_side = SplitSide.RIGHT
split = Split(use_pio=True)
keyboard.modules.append(split)

# keymap
keyboard.keymap = [ [KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.BSPC,KC.LCTRL,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.SCOLON,KC.QUOTE,KC.LSHIFT,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.N,KC.M,KC.COMMA,KC.DOT,KC.SLASH,KC.ESCAPE,KC.LGUI,KC.MO(1),KC.SPACE,KC.ENTER,KC.MO(2),KC.RALT,KC.RALT,KC.NO,KC.NO,KC.NO],
[KC.TAB,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,KC.BSPC,KC.LCTRL,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.LEFT,KC.DOWN,KC.UP,KC.RIGHT,KC.NO,KC.NO,KC.LSHIFT,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.LGUI,KC.TRNS,KC.SPACE,KC.ENTER,KC.MO(3),KC.RALT,KC.RALT,KC.NO,KC.NO,KC.NO],
[KC.TAB,KC.EXCLAIM,KC.AT,KC.HASH,KC.DOLLAR,KC.PERCENT,KC.CIRCUMFLEX,KC.AMPERSAND,KC.ASTERISK,KC.LEFT_PAREN,KC.RIGHT_PAREN,KC.BSPC,KC.LCTRL,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.MINUS,KC.EQUAL,KC.LBRACKET,KC.RBRACKET,KC.BSLASH,KC.GRAVE,KC.LSHIFT,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.UNDERSCORE,KC.PLUS,KC.LEFT_CURLY_BRACE,KC.RIGHT_CURLY_BRACE,KC.PIPE,KC.TILDE,KC.LGUI,KC.MO(3),KC.SPACE,KC.ENTER,KC.TRNS,KC.RALT,KC.RALT,KC.NO,KC.NO,KC.NO],
[KC.RESET,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.RGB_TOG,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.LGUI,KC.TRNS,KC.SPACE,KC.ENTER,KC.TRNS,KC.RALT,KC.RALT,KC.NO,KC.NO,KC.NO],
[KC.NO],
[KC.NO] ]
# keymap
if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.USB)
