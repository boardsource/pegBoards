# OLED

## Kmk Part

Peg Supports Oleds configured using the
[peg_oled_display](https://github.com/KMKfw/kmk_firmware/blob/master/docs/peg_oled_display.md)
extension. This extension and there for peg only support 32x128 OLEDS.

## Peg part

Main.py:

In main.py add your oled python code (example below) They should only be set to
`toDisplay=OledDisplayMode.TXT` because the client only downloads
main.py,layout.json and kb.py to the cpy drive so images would lead to a non
working keymap. There should be no un-needed spaces or returns the code needs to
be read by a computer not by us.

```python
# oled
oled_ext = Oled(OledData(corner_one={0:OledReactionType.STATIC,1:["layer"]},corner_two={0:OledReactionType.LAYER,1:["","","","","","","",""]},corner_three={0:OledReactionType.LAYER,1:["","","","","","","",""]},corner_four={0:OledReactionType.LAYER,1:["","","","","","","",""]}),toDisplay=OledDisplayMode.TXT,flip=False)
# oled
```

`# oled` Is just like any other wrapping comment in Peg, letting the client know
that it should parse this code as a OLED configuration. So you need one comment
above and below your OLED code.

Layout.json:

Like we go over in the [layout docs](./layout.md)
Oled has 1 field in the `"features":{` object.

```json
"oled": true,
 ```

* `oled`
  * bool

[Return to main page](./README.md)
