from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.hid import HIDModes
from kmk.handlers.sequences import send_string
import supervisor
keyboard = KMKKeyboard()
modtap = ModTap()
layers_ext = Layers()
keyboard.modules.append(layers_ext)
keyboard.modules.append(modtap)
keyboard.modules = [layers_ext, modtap]

# keymap
keyboard.keymap = [ [KC.GRAVE,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.MINUS,KC.TAB,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.SCOLON,KC.QUOTE,KC.LSHIFT,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.ESCAPE,KC.ENTER,KC.N,KC.M,KC.COMMA,KC.DOT,KC.SLASH,KC.RSHIFT,KC.LCTRL,KC.LALT,KC.LGUI,KC.LBRACKET,KC.DELETE,KC.TAB,KC.MO(1),KC.MO(2),KC.SPACE,KC.BSPC,KC.RBRACKET,KC.RGUI,KC.RALT,KC.RCTRL],
[KC.NO,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,KC.NO,KC.PLUS,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.PIPE,KC.HASH,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.AT,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO],
[KC.NO,KC.F1,KC.F2,KC.F3,KC.F4,KC.NO,KC.NO,KC.HOME,KC.NO,KC.PGUP,KC.END,KC.NO,KC.NO,KC.F5,KC.F6,KC.F7,KC.F8,KC.NO,KC.NO,KC.LEFT,KC.DOWN,KC.UP,KC.NO,KC.NO,KC.NO,KC.F9,KC.F10,KC.F11,KC.F12,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO] ]
# keymap
if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.USB)
