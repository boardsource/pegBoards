# auto generated
import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    row_pins = (board.GP12,board.GP13,board.GP16,board.GP17,board.GP18)
    col_pins = (
        board.TX,
        board.RX,
        board.GP02,
        board.GP03,
        board.GP04,
        board.GP05,
        board.GP06,
        board.GP07,
        board.GP08,
        board.GP09,
        board.GP10,
        board.GP11
   
    )
    diode_orientation = DiodeOrientation.COLUMNS
    i2c = board.I2C
    SCL=board.SCL
    SDA=board.SDA
    brightness_limit = 0.6
    num_pixels = 58
    rgb_pixel_pin = board.GP21
    buzzer_pin = board.GP29
    spi_dc=board.GP20
    spi_CS=board.GP25
    spi_SCK=board.GP26
    spi_TX=board.GP27
    spi_RX=board.GP28
    led_key_pos =[10,11,12,13,14,15,16,17,18,19,20,21,
                 22,23,24,25,26,27,28,29,30,31,32,33,
                 34,35,36,37,38,39,40,41,42,43,44,45,
                 46,47,48,49,50,51,52,53,54,55,56,57,
                 0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ]
