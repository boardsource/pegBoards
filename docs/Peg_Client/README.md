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
