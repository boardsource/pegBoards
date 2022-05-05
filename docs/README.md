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

## Broad Strokes
### main.py
Main.py should be a functional main.py from kmk. With the configurable parts wrapped in the correct comments.

Example: 

 `# keymap` keymap code... `# keymap` 

Comments like that tell the Peg client pull out those parts and load them into the app to be changed. 
With out  a comment wrapping something it will at best be over written and at worst stop your keymap from loading into the Peg client.
### layout.json
Layout.json are like settings for the app and let the client know how to save the keymap in the future.
