from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.hid import HIDModes
from kmk.handlers.sequences import send_string
import supervisor
from kmk.extensions.RGB import RGB
keyboard = KMKKeyboard()
modtap = ModTap()
layers_ext = Layers()
keyboard.modules = [layers_ext, modtap]
rgb_ext = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=48)
keyboard.extensions.append(rgb_ext)
# keymap
keyboard.keymap = [[KC.RGB_TOG, KC.A, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.L, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.L, KC.L, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.H, KC.DOT, KC.L, KC.LALT, KC.L, KC.LCTRL, KC.NO, KC.L, KC.SLASH, KC.TAB, KC.RCTRL], 
[KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, KC.QUOTE, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO], 
[KC.NO, KC.AT, KC.HASH, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.PLUS, KC.NO, KC.NO, KC.PIPE, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO], 
[KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.F11, KC.F12, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO]] 
# keymap
if __name__ == '__main__':
    if supervisor.runtime.usb_connected:
       keyboard.go()
    else:
        keyboard.go(hid_type = HIDModes.BLE)