# Keymap

## Kmk Part

Almost nothing needs to be changed here if you keyboard works it takes no extra
configuration to bring to peg.

## Peg part

Main.py:

 In main.py add your keymap python code (example below) Peg does not support a
 dynamic amount of layers you need to have 8 layer. You do not need  to come up
 with uses for them but they should be there. Peg does not support variables as
 keycodes So swap `LOWER` for `KC.MO(1)` and anything along those lines. Also
 for your PR to be accepted your keymap should have no custom keycodes in it as
 the Peg client wont pick them up and will swap them for KC.NO. There should be
 no un-needed spaces or returns the code needs to be read by a computer not by
 us. Only return after a layer and one space before the first layer and after
 the last before the closing `]`.

 ```python
# keymap
keyboard.keymap = [ [layer 0...],
[layer 1...],
[layer 2...],
[layer 3...],
[layer 4...],
[layer 5...],
[layer 6...],
[layer 7...] ]
# keymap
```

`# keymap` Is just like any other wrapping comment in Peg, letting the client know that it should parse this code as a keymap configuration.
You need one comment above and below your keymap code.

Layout.json:

No part of your keymap is configured by layout.json

[Return to main page](./README.md)
