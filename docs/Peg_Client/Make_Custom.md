# Make Custom
Make Custom is a more advanced section of the Peg client, it allows you to add onto your keycode selection. T
he peg client supports any keycode you could want to do but the client may not let you make it inside the client. 
In the client you can make simple macros, eg: push one key and type out "Hello my name is Cole".
To do more advanced keycodes supported by KmK or to backup your custom keycodes you can click the "Show export Keycodes" button. This will first let you copy all of your current keycodes for safe keeping and give you a template to edit to make more.

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
Now press the "Show import Keycodes" Button and paste in your new json array, and push the "Import" button below the test field. Now you should be able to see your new keycode under the Custom tab in your keymap. 


[Return to main page](./README.md)