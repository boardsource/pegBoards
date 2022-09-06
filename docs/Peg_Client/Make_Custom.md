# Make Custom

Make Custom is a more advanced section of the Peg client, it allows you to add
onto your keycode selection. The peg client supports any keycode you could want
to do but the client may not let you make it inside the client. In the client
you can make simple macros, eg: push one key and type out "Hello my name is
Cole".To do more advanced keycodes supported by KMK or to backup your custom
keycodes you can click the "Show export Keycodes" button. This will first let
you copy all of your current keycodes for safe keeping and give you a template
to edit to make more.

## Note
If you just want to make one or two advanced custom keycodes you can turn on "dev" mode in options. This will let you put any keycode you want in the code section. Please be aware that dev mode will let you make keycodes that don't work. Please test your keycodes before adding them it can be hard to debug a broken keycode.

If you want to add a lot of custom codes it will probably be faster to use the json import feature, being that you can import as many as you want at the same time.

You can make custom key codes by taking the exported json:

```json
[{"code":"send_string('test')",
"display":"t",
"keybinding":"",
"canHaveSub":false,
"canHaveSubNumber":false,
"subNumber":0,
"Description":"test"
}]
```

and editing it to do what you want:

```json
[{"code":"KC.LT(1, KC.ENT)",
"display":"L1-ENT",
"keybinding":"",
"canHaveSub":false,
"canHaveSubNumber":false,
"subNumber":0,
"Description":"Pushes layer 1 if held and enter if tapped"
}]
```

Now press the "Show import Keycodes" Button and paste in your new json array,
and push the "Import" button below the test field. Now you should be able to see
your new keycode under the Custom tab in your keymap.

[Return to main page](./README.md)
