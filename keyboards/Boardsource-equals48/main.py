from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.hid import HIDModes
from kmk.handlers.sequences import send_string
import supervisor
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData
from kmk.extensions.peg_rgb_matrix import Rgb_matrix
keyboard = KMKKeyboard()
modtap = ModTap()
layers_ext = Layers()
keyboard.modules.append(layers_ext)
keyboard.modules.append(modtap)
# codeblock
import simpleio
buzzer = keyboard.buzzer_pin
TONE_FREQ = [ 262,  # C4
              294,  # D4
              330,  # E4
              349,  # F4
              392,  # G4
              440,  # A4
              494 ] # B4
for i in range(len(TONE_FREQ)):
    simpleio.tone(buzzer, TONE_FREQ[i], duration=0.15)
# codeblock
# oled
oled_ext = Oled(OledData(corner_one={0:OledReactionType.STATIC,1:["layer:"]},corner_two={0:OledReactionType.LAYER,1:["1","2","3","4","5","6","7","8"]},corner_three={0:OledReactionType.LAYER,1:["base","raise","lower","adjust","5","6","7","8"]},corner_four={0:OledReactionType.LAYER,1:["qwerty","nums","shifted","leds","5","6","7","8"]}),toDisplay=OledDisplayMode.TXT,flip=False)
# oled
keyboard.extensions.append(oled_ext)
# ledmap
rgb_ext = Rgb_matrix(ledDisplay=[[85,0,255],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[85,0,255],[85,0,255],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[85,0,255],[85,0,255],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[85,0,255],[85,0,255],[85,0,255],[85,0,255],[85,0,255],[85,0,255],[0,255,234],[0,255,234],[85,0,255],[85,0,255],[85,0,255],[85,0,255],[85,0,255],[0,255,234],[85,0,255],[85,0,255],[85,0,255],[85,0,255],[0,255,234],[0,255,234],[85,0,255],[85,0,255],[85,0,0]],disable_auto_write=True)
# ledmap
keyboard.extensions.append(rgb_ext)
keyboard.modules = [layers_ext, modtap]

# keymap
keyboard.keymap = [ [KC.ESCAPE,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.BSPC,KC.TAB,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.SCOLON,KC.QUOTE,KC.LSHIFT,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.N,KC.M,KC.COMMA,KC.DOT,KC.SLASH,KC.ENTER,KC.PIPE,KC.LCTRL,KC.LALT,KC.LGUI,KC.MO(2),KC.SPACE,KC.SPACE,KC.MO(1),KC.LEFT,KC.DOWN,KC.UP,KC.RIGHT], 
[KC.NO,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,KC.BSPC,KC.NO,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.TRNS,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.NO,KC.NO,KC.PGUP,KC.NO,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.NO,KC.NO,KC.NO,KC.NO], 
[KC.NO,KC.NO,KC.AT,KC.HASH,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.BSPC,KC.NO,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.NO,KC.PLUS,KC.NO,KC.NO,KC.PIPE,KC.TRNS,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.TRNS,KC.TRNS,KC.HOME,KC.END,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.NO,KC.NO,KC.NO,KC.NO], 
[KC.NO,KC.NO,KC.AT,KC.HASH,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.BSPC,KC.NO,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.NO,KC.PLUS,KC.NO,KC.NO,KC.PIPE,KC.TRNS,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.TRNS,KC.TRNS,KC.HOME,KC.END,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.NO,KC.NO,KC.NO,KC.NO], 
[KC.NO,KC.NO,KC.AT,KC.HASH,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.BSPC,KC.NO,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.NO,KC.PLUS,KC.NO,KC.NO,KC.PIPE,KC.TRNS,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.TRNS,KC.TRNS,KC.HOME,KC.END,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.NO,KC.NO,KC.NO,KC.NO], 
[KC.NO,KC.NO,KC.AT,KC.HASH,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.BSPC,KC.NO,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.NO,KC.PLUS,KC.NO,KC.NO,KC.PIPE,KC.TRNS,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.TRNS,KC.TRNS,KC.HOME,KC.END,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.NO,KC.NO,KC.NO,KC.NO], 
[KC.NO,KC.NO,KC.AT,KC.HASH,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.BSPC,KC.NO,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.NO,KC.PLUS,KC.NO,KC.NO,KC.PIPE,KC.TRNS,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.TRNS,KC.TRNS,KC.HOME,KC.END,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.NO,KC.NO,KC.NO,KC.NO], 
[KC.NO,KC.NO,KC.AT,KC.HASH,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.BSPC,KC.NO,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.NO,KC.PLUS,KC.NO,KC.NO,KC.PIPE,KC.TRNS,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.TRNS,KC.TRNS,KC.HOME,KC.END,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.NO,KC.NO,KC.NO,KC.NO] ] 
# keymap
if __name__ == '__main__': 
    keyboard.go(hid_type=HIDModes.USB)
