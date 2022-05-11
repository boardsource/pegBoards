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
# codeblock
if True:
    print("go on the")
# codeblock
# codeblock
if True:
    print("shot through the heart")
# codeblock
# codeblock#Prints a song
"""
This is not the best song but its all right
"""

if True:
    print("shot through the heart")
# codeblock
# codeblock
"""
Tester block
dont get
its bad
for real
"""

if True:
    print("shot through the heart")
# codeblock
# oled
oled_ext = Oled(OledData(corner_one={0:OledReactionType.STATIC,1:["qwertyzzzz"]},corner_two={0:OledReactionType.LAYER,1:["1","2","3","4","5","6","7","8"]},corner_three={0:OledReactionType.LAYER,1:["base","raise","lower","adjust","5","6","7","8"]},corner_four={0:OledReactionType.LAYER,1:["qwertyzzz","nums","shifted","leds","5","6","7","8"]}),toDisplay=OledDisplayMode.TXT,flip=False)
# oled
keyboard.extensions.append(oled_ext)
# ledmap
rgb_ext = Rgb_matrix(ledDisplay=[[100,100,100],[255,0,0],[0,0,255],[0,255,0],[255,247,0],[255,77,0],[255,0,242],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[255,55,55],[255,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[255,55,55],[255,55,55],[55,55,55],[55,55,55],[55,55,55],[172,45,45],[255,0,0],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[255,55,55],[255,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[255,55,55],[255,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[255,55,55],[255,55,55],[55,55,55],[55,55,55],[200,0,255],[255,55,55],[55,55,55],[55,55,55],[255,55,55],[200,0,255],[200,0,255],[200,0,255],[200,0,255],[200,0,255],[200,0,255],[200,0,255],[200,0,255],[200,0,255],[200,0,255],[200,0,255],[200,0,255]],split=True,rightSide=False,disable_auto_write=True)
# ledmap
keyboard.extensions.append(rgb_ext)
# TODO Comment one of these on each side
split_side = SplitSide.LEFT
#split_side = SplitSide.RIGHT
split = Split(split_side = split_side,data_pin=keyboard.rx, data_pin2=keyboard.tx, uart_flip=False)
keyboard.modules.append(split)
# encodercount
# 2
# encodercount
# keymap
keyboard.keymap = [ [KC.ESCAPE,KC.LT(1, KC.ENT, tap_time=100),send_string('testing'),KC.N3,KC.N4,KC.N5,KC.P,KC.N7,KC.N8,KC.N9,KC.N0,KC.BSPC,KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.BSPC,KC.LCTRL,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.SCOLON,KC.QUOTE,KC.LSHIFT,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.RGB_TOG,KC.RBRACKET,KC.N,KC.M,KC.COMMA,KC.DOT,KC.SLASH,KC.RSHIFT,KC.LGUI,KC.MO(1),KC.LCTRL,KC.SPACE,KC.ENTER,KC.MO(2),KC.RALT,KC.RCTRL,KC.UP,KC.DOWN,KC.A,KC.Z], 
[KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.BSPC,KC.LCTRL,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.SCOLON,KC.QUOTE,KC.LSHIFT,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.LBRACKET,KC.RBRACKET,KC.N,KC.M,KC.COMMA,KC.DOT,KC.SLASH,KC.RSHIFT,KC.LGUI,KC.MO(1),KC.NO,KC.SPACE,KC.ENTER,KC.MO(2),KC.RALT,KC.RCTRL,KC.RIGHT,KC.LEFT,KC.UP,KC.DOWN], 
[KC.N2,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,KC.BSPC,KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.BSPC,KC.NO,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.NO,KC.NO,KC.NO,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.NO,KC.NO,KC.N,KC.M,KC.NO,KC.DOT,KC.NO,KC.NO,KC.LGUI,KC.MO(1),KC.NO,KC.NO,KC.NO,KC.MO(2),KC.RALT,KC.NO,KC.UP,KC.DOWN,KC.A,KC.Z], 
[KC.N3,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,KC.BSPC,KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.BSPC,KC.NO,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.NO,KC.NO,KC.NO,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.NO,KC.NO,KC.N,KC.M,KC.NO,KC.DOT,KC.NO,KC.NO,KC.LGUI,KC.MO(1),KC.NO,KC.NO,KC.NO,KC.MO(2),KC.RALT,KC.NO,KC.UP,KC.DOWN,KC.A,KC.Z], 
[KC.N4,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,KC.BSPC,KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.BSPC,KC.NO,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.NO,KC.NO,KC.NO,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.NO,KC.NO,KC.N,KC.M,KC.NO,KC.DOT,KC.NO,KC.NO,KC.LGUI,KC.MO(1),KC.NO,KC.NO,KC.NO,KC.MO(2),KC.RALT,KC.NO,KC.UP,KC.DOWN,KC.A,KC.Z], 
[KC.N5,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,KC.BSPC,KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.BSPC,KC.NO,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.NO,KC.NO,KC.NO,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.NO,KC.NO,KC.N,KC.M,KC.NO,KC.DOT,KC.NO,KC.NO,KC.LGUI,KC.MO(1),KC.NO,KC.NO,KC.NO,KC.MO(2),KC.RALT,KC.NO,KC.UP,KC.DOWN,KC.A,KC.Z], 
[KC.N6,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,KC.BSPC,KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.BSPC,KC.NO,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.NO,KC.NO,KC.NO,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.NO,KC.NO,KC.N,KC.M,KC.NO,KC.DOT,KC.NO,KC.NO,KC.LGUI,KC.MO(1),KC.NO,KC.NO,KC.NO,KC.MO(2),KC.RALT,KC.NO,KC.UP,KC.DOWN,KC.A,KC.Z], 
[KC.N7,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,KC.BSPC,KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.BSPC,KC.NO,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.NO,KC.NO,KC.NO,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.NO,KC.NO,KC.N,KC.M,KC.NO,KC.DOT,KC.NO,KC.NO,KC.LGUI,KC.MO(1),KC.NO,KC.NO,KC.NO,KC.MO(2),KC.RALT,KC.NO,KC.UP,KC.DOWN,KC.A,KC.Z] ] 
# keymap
if __name__ == '__main__': 
    keyboard.go(hid_type=HIDModes.USB)