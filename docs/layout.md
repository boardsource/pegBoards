# Layout

Layout.json is the biggest part of a keyboards support with the Peg client, The
settings you set here determine everything. Please look at other examples and
load it up in the peg client to make sure everything is working as intended.

## Features

`features` Is an object with 16 fields all of them need to be set even if the
value is 0 or false.
The spelling is important but the order is not.

* `name`
  * String
    * The name of the keyboard eg: CRKBD
* `creator`
  * String
    * The designer of the keyboard
* `ble`
  * Boolean
    * Is the keyboard BLE first due to a limitation in kmk at the time of
          making this you need on config for BLE and one for wired with the same
          controller.
* `split`
  * Boolean
    * Is the keyboard split using 2 controllers?
* `rightSide`
  * Boolean
    * Is the keyboard split and is this layout.json on the right side (off
          side) Peg does not support ee hands the left side must be plugged in.
* `rx_tx`
  * Boolean
    * Is the keyboard split and is it configured for 2 wire communication?
* `uartFlip`
  * Boolean
    * Is the keyboard split and is it configured for 2 wire communication
          and needs Uart Flipped?
* `splitPico`
  * Boolean
    * Do you need to use `use_pio=True` in your split? this does it
* `oled`
  * Boolean
    * Is the keyboard wired to have a OLED?
* `perkey`
  * Boolean
    * Is the keyboard configured for per key LEDs?
* `underglow`
  * Boolean
    * Is the keyboard configured for underglow LEDs?
* `perkeyCount`
  * Int
    * number of per key LEDs
* `underglowCount`
  * Int
    * number of underglow LEDs
* `encoders`
  * Boolean
    * Is the keyboard configured for one or more encoders
* `encoderCount`
  * Int
    * How many encoders are configured? (for splits add up all encoders 1 on
          each side = encoderCount:2)
* `bootSize`
  * Int
    * Leave at 0 unless you need a boot.py in that case then it should be one of the 2 numbers eg: 4096  will come out as `supervisor.set_next_stack_limit(4096 + 4096)` if included the client will generate the file if its not there.

## Layout

`layout` is an array of keys This was inspired by qmk's layout.json and should
be easy to convert. The keys should be in this array in the same order as they
are in your keymap. There are [on-line tools](https://qmk.fm/converter/) that
can be used to get you close.

Each key is a object with 3 fields

* `w`
  * Int
    * Width of key
* `x`
  * Int
    * x position
* `y`
  * Int
    * y position

Height is not supported at this time.

## Underglow

`underglow` is an array of underglow LEDs.
This is configured in the same way as Layout. x/y cords of where the underglow
LEDS are on your board as if you were looking though the board.

Each LED is a object with 3 fields

* `w`
  * Int
    * Width of LED (1 99% of the time)
* `x`
  * Int
    * x position
* `y`
  * Int
    * y position

[Return to main page](./README.md)
