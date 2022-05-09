# per key LED
## Kmk Part
Peg Supports RGB LEDS configured using the [peg_rgb_matrix](https://github.com/KMKfw/kmk_firmware/blob/master/docs/peg_rgb_matrix.md) extension. 




## Peg part
Main.py:

 In main.py add your rgb_ext python code (example below) this extension has one large difference when configuring for peg.
Pass one large array of colors to `ledDisplay` perkey LED colors first then underglow LED colors directly after. 
Do not use the `Rgb_matrix_data` class.
  There should be no un-needed spaces or returns the code needs to be read by a computer not by us. 

Kmk way:
```python 
rgb_ext = Rgb_matrix(ledDisplay=Rgb_matrix_data(
    keys=[
    [255,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],                        [55,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[255,55,55],
    [255,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],                        [55,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[255,55,55],
    [255,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],                        [55,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[255,55,55],
    [255,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[255,55,55],[255,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[255,55,55],
                                     [255,55,55],[55,55,55],[55,55,55],[255,55,55],[255,55,55],[55,55,55],[55,55,55],[255,55,55]],
                                    
    underglow=[ 
             [0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55]]
             ),
    split=True,
    rightSide=True,
    disable_auto_write=True)
```
Peg way:
```python
rgb_ext = Rgb_matrix(ledDisplay=[colors array...],split=True,rightSide=False,disable_auto_write=True)
```
in peg map:
 ```python
# ledmap
rgb_ext = Rgb_matrix(ledDisplay=[colors array...],split=True,rightSide=False,disable_auto_write=True)
# ledmap
 ```
 `# ledmap` Is just like any other wrapping comment in Peg, letting the client know that it should parse this code as a led configuration.
 You need one comment above and below your LED code.

 Layout.json:

 Like we go over in the [layout docs](./layout.md)
 LEDs have 4 fields in the `"features":{` object.
 ```json
"perkey": true,
"underglow": true,
"perkeyCount": 58,
"underglowCount": 12,
 ```
 * `perkey`
    * bool
 * `underglow`
    * bool
* `perkeyCount`
    * int
* `underglowCount`
    * int

As well as `"underglow":[`array in the main object. This is configured in the same way as keys. x/y cords of where the underglow LEDS are on your board as if you were looking though the board.  

[Return to main page](./README.md)