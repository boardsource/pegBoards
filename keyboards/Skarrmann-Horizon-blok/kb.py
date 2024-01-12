

import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.boardsource_blok import pinout as pins
from kmk.quickpin.pro_micro.avr_promicro import translate as avr

from kmk.scanners import DiodeOrientation
from kmk.scanners import intify_coordinate as ic


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        pins[avr["F5"]],
        pins[avr["F6"]],
        pins[avr["F7"]],
        pins[avr["B1"]],
        pins[avr["B3"]],
        pins[avr["B2"]],
        pins[avr["B6"]],
        pins[avr["B5"]],
        pins[avr["B4"]],
        pins[avr["E6"]],
        pins[avr["D7"]],
        pins[avr["C6"]],
        pins[avr["D4"]],
        pins[avr["D0"]],

    )
    row_pins = (
        pins[avr["D3"]],
        pins[avr["D2"]],
        pins[avr["D1"]],
        pins[avr["F4"]],
    )
    diode_orientation = DiodeOrientation.COLUMNS
    i2c = board.I2C
    coord_mapping = [0 ,1 ,2 ,3 ,4 ,5       ,8 ,9 ,10,11,12,13,
                     14,15,16,17,18,19      ,22,23,24,25,26,27,
                     28,29,30,31,32,33,34,35,36,37,38,39,40,41,
                     42,43,44,45,46,47,48,49,50,51,52,53,54,55,]
