# Encoders

## KMK Part

Peg Supports encoders configured using an [Rotary Encoder
Scanners](http://kmkfw.io/docs/scanners#rotary-encoder-scanners).
With this your keymap will hold your encoder keycodes and your keymap keycodes.
For your keyboard to be supported you need to configure it with the keycodes for
encoders after your keymap keycodes. Eg: 67 key keyboard with one encoder should
have 69 keycodes in each layer 67 for the main matrix and 2 for the single
encoder at the end of each layer array.

## Peg Part

The Peg client can not guarantee that main.py or layout.json will be loaded first.
Because of that we need to know the encoder count in both places.

Main.py:

 In main.py add these comments.

 ```python
# encodercount
# 2
# encodercount
 ```

 `# encodercount` Is just like any other wrapping comment in Peg, the only difference is that in this case we only wrap another comment.

 That comment being a space and number stating how many encoders this keymap has.

 Layout.json:

 Like we go over in the [layout docs](./layout.md)
 Encoders have 2 fields in the `"features":{` object.

 ```json
"encoders": true,
"encoderCount": 2,
 ```

* `encoders`
  * bool
* `encoderCount`
  * int

[Return to main page](./README.md)
