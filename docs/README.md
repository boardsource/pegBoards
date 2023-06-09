# Documentation

Below you will find information going over each part of your keymap.

* [layout.json](./layout.md)
* [keymap](./keymap.md)
* [ledmap](./per-key-led.md)
* [oled](./oled.md)
* [encoders](./encoders.md)
* [splits](./split.md)
* [Contributing](./contributing.md)
* [Peg Client docs](./Peg_Client/README.md)


## 0.9 Beta Warning
Currently Peg is at version 0.9 and in open beta.  Please be understanding that
we are working to make it the best we can but you will find bugs.  When / if you
find any bugs please report them
[here](https://github.com/boardsource/pegBoards/issues), after checking if they
are already reported.  If there are bugs in any parts of [this
repo](https://github.com/boardsource/pegBoards) you can also fix them and make a
pr.

## Broad Strokes

### main.py

Main.py should be a functional main.py from kmk. With the configurable parts
wrapped in the correct comments.

Example:

 `# keymap` keymap code... `# keymap`

Comments like that tell the Peg client pull out those parts and load them into
the app to be changed.  With out  a comment wrapping something it will at best
be over written and at worst stop your keymap from loading into the Peg client.

### layout.json

Layout.json are like settings for the app and let the client know how to save
the keymap in the future.
