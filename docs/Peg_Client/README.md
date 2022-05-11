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

## Broad Strokes
The Peg client will immediately start looking for a keyboard as soon as you launch the app. 
If it does not find one quickly it will assume your board has not been set up and prompt you to download one from this repo.
After you get into the app with a keyboard connected you will see the main keymapping page.
Here we will talk about everything around the main view, In the top right corner of the app you will see 2 things. 

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
    * You dont need to save each on each page you can stage all your changes and save at the end. 
    * This button will change color to notify you that changes have been made so dont leave without saving.