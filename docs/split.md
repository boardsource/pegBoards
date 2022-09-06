# Splits

## Kmk Part

Peg Supports Splits with only one thing changed. If your keyboard uses 2 wire
configuration you need to add rx and tx to your kb.py

``` python
    rx = board.RX
    tx = board.TX
```

## Peg part

Main.py:

No changes need / can to be made to your main.py for splits every time the
keymap is saved the code is re-generated from the data in layout.json. There for
no configuration is parsed in your main.py. The only requirement is that your keymap is setup for EE-Hands see example below.
```python
split = Split(use_pio=True)
```
Notice how no side is passed. This will be parsed by the split module based on the name of the controller.
To make that work when your keymap is installed on the keyboard the first time we generate a boot.py that will rename your controller from "CIRCUITPY" to "KEYBOARD_NAME-L or R" based on the info given in your layout.json

 Layout.json:

 Like we go over in the [layout docs](./layout.md)
 splits have 5/6s fields in the `"features":{` object.

```json
"rx_tx": true,
"uartFlip": false,
"split": true,
"rightSide": false,
"splitPico":false,
"ble": false,
```

* `rx_tx`
  * bool
* `uartFlip`
  * bool
* `split`
  * bool
* `rightSide`
  * bool
* `splitPico`
  * bool
* `ble`
  * bool

[Return to main page](./README.md)
