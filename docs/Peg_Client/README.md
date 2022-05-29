# Peg Client Documentation

Below you will find information going over each part of the Peg client and what it can do.

* [Keymap](./Keymap.md)
* [Encoder](./Encoder.md)
* [LED](./LED.md)
* [OLED](./OLED.md)
* [Make Custom](./Make_Custom.md)
* [Code Block](./Code_Block.md)
* [Options](./Options.md)
* [Peg dev docs](../README.md)

## Quick Start and Testing

Using Peg is super simple. To get started all you need is a CircuitPython drive plugged into your computer. If your keyboard PCB has already been added to Peg, then you just have to plug in your book and select the correct PCB eg: Boardsource-Microdox_v2-blok-left. Then select the CIRCUITPY drive when prompted. Otherwise If your chosen PCB has not been added to Peg then you will need to add it [here](../README.md) are a link to the docs on how to do so. After Peg sets up your CircuitPython drive the UI will update and you will see your keymap. From there start dragging and dropping keycodes around to see how it feels.

### Testing It Out

If you want to test it out and see how it all works, you can do the same thing but just select a normal flash drive (back up any files on the flash drive). Then the same thing will happen the Peg client will pick it up and you can test out the client even without having a supported keyboard/controller. If you like it you can save those files on your flash drive and move them all to the micro-controller when you get it.

## Broad Strokes

The Peg client will immediately start looking for a keyboard as soon as you launch the app.
If it does not find one quickly it will assume your board has not been set up
and prompt you to download one from this repo. After you get into the app with a
keyboard connected you will see the main keymap page. Here we will talk about
everything around the main view. In the top right corner of the app you will see
2 things.

1. Your account status
2. Your current connected keyboard and if you have a good connection to the Peg server.

Then you will see the main views title and 3 buttons. These buttons are aware of what page you are currently on.

1. Share
    * Here you can share what ever you are currently configuring eg: on keymap view share your keymap
    * after you share your feature will be uploaded to this repo for everyone to be able to see and review.
2. Download
    * Here you can download new features again its aware of where you are in the app, eg: on keymap download a new keymap
    * after you download a feature it will automatically be added to your board wiping out any thing you had configured.
3. Save
    * This will save your current configuration.
    * You don't need to save each on each page you can stage all your changes and save at the end.
    * This button will change color to notify you that changes have been made so don't leave without saving.


## FaQ

### Can I "Eject" my keyboard drive?
* Yes you can to type on your keyboard but if you want to make any changes using Peg you will need the drive connected and mounted.

### Peg does not detect my keyboard running KmK.
* Much like other GUI flashing tools we need to be on the same page. You need to have a peg map on your keyboard to use it with Peg. 
* If your keyboard PCB has already been added to Peg, then you just have to plug in your book and select the correct PCB eg: Boardsource-Microdox_v2-blok-left. Then select the CIRCUITPY drive when prompted. Otherwise If your chosen PCB has not been added to Peg then you will need to add it [here](https://peg.software/docs/) are a link to the docs on how to do so.

### What do I do when I get an error installing libs or kmk?
* this is from the drive having some kind of problem best to start fresh.
back up your keymap (main.py) if you have made any changes.

* Now connect to a CircuitPython repl.
    * [Windows guide](https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-windows)
    * [MacOs guide](https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-mac-and-linux)
    * [Linux guide](https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-linux)
* Now wipe the CircuitPython drive 
    * Type `import storage` into the REPL.
    * Then, type `storage.erase_filesystem()` into the REPL.
    * The CIRCUITPY drive will be erased and the board will restart with an empty CIRCUITPY drive.
    * [Full Guide](https://docs.circuitpython.org/en/latest/docs/troubleshooting.html)


### My right side leds are not the right color on my split keyboard?
* Both sides need to be flashed for the colors to be correct. 
* When you make a change to your LEDS on a split keyboard you should see a modal pop up.
    * This modal will guide you through flashing the other side of your keyboard.
    * Do not click the close button just follow the steps 
        * Step 1) Unplug first side Then push the button saying its unplugged.
        * Step 2) Plug in the other side of the keyboard when prompted.
        * Step 3) Let the app flash the keyboard until you see a screen that says you can close it.


### RGB_TOG Does not toggle both sides of split keyboard.
* This can happen when your keyboards maps dont match up. 
* most of the time its ok if the keymaps are not in sync but for 1 or 2 keycodes like `RGB_TOG` the keycode needs to be on the same key on the same layer on both sides of the board.

### I installed a code block and not my keyboard does not type.
* Code blocks are user generated code and have no guarantee that they will work. The easiest thing to do is remove that code block
* If you want to dig in and figure out whats wrong and learn some things along the way connect to a CircuitPython repl and see what its saying. Kmk is very approachable and it could be an easy fix. If you get it working think about updating the code block in this repo so the next person doesn't have any problem's 

### My keymap has `ERR` keys in it.
* This almost always happens due to custom keycodes.
    * Make sure your custom keycode has a very simple name like "LT_1" or "GUI_MACRO_CTRL" 
    * if you are making custom keys you cant use any spaces or non letter characters other then "_" and "-" in your `display` 
* If you are not using custom codes in your keymap then the other thing that can happen is some kind of formatting error in your keymap make sure its formatted correctly. There should be
 no un-needed spaces or returns the code needs to be read by a computer not by
 us. Only return after a layer and one space before the first layer and after
 the last before the closing `]`.

### My Boardsource log in's don't work in peg.
* Log into your account on [Boardsource](https://boardsource.xyz/) and make sure you see `Peg: True` under your user name.

### My Blok does not show up as a CIRCUITPY Drive.
* Before you can use peg you need to flash your controller to use [CircuitPython](https://circuitpython.org/downloads) or [Bs-Python](https://github.com/boardsource/bs-python)
* If you are using a Blok you can download the [Bs-Python u2f here](https://peg.software/api/blok.uf2) 
* To flash  it you will just need to hold down the boot button ( or short boot pin to gnd) while you plug in the Blok. When you do that a new "drive" should pop up on your computer named "RPI-RP2" There you can drag and drop the blok.uf2 file. Your blok should now restart and show up as a CIRCUITPY Drive.



