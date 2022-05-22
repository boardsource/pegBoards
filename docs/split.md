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
no configuration is parsed in your main.py.

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
