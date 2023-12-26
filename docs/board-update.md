It's inevitable that you will eventually need to update your board when peg
updates. Let's make it easy to get you up and running on the latest and greatest
software! Peg is built to keep you as up to date as it can. You should be able
to have it auto update for you in most cases. When things change too far, you
may need to give it a hand to get all of the latest code.

# Getting in bootloader

The first step in getting up to date is to get your device into the bootloader.
This will be different for every device, but the board specific docs cover it.
Normally it's either flipping a switch or holding the boot button, not to be
confused with the reset button. Guides for getting into bootloader mode can be
found below for several devices.

- [Blok](./blok.md)
- [Lulu](https://boardsource.xyz/help/6306d4840b62f46fa9448c0b)


# Confirming you are in bootloader

Most computers should show you a flash drive appear. It will be named "RPI-RP2".
If it is named something else, you aren't in the bootloader unless your device
specific docs tells you it's named something else. Windows and Mac this will
show up as any flash drive. Some distrobutions of Linux may require you to mount
it manually, but the most popular distros should work out of the box.

# Getting the latest bs-python

If your device is supported by bs-python, you will want to download the latest
release for your device
[HERE](https://github.com/boardsource/bs-python/releases). If you don't see your
device listed there, you will need the latest release of Circuitpython. That can
be found [HERE](https://circuitpython.org/downloads). If you aren't sure which
version to download, make sure the device name matches. If you aren't sure, you
won't harm anything if you accidentally get the wrong one and can always try
again, or ask support. If there's multiple matches for your device, such as
`boardsouce_lulu.uf2 ` and `boardsouce_lulu_full.uf2`, they will both work for
the listed device though the "full" version also contains all of KMK. When
updating, we recommend trying the not "full" version first, or if flashing a new
device, or that causes any issues, use the "full" version if avaliable. There
are no "full" verisons for Circuitpython, only bs-python.


# Flashing the file

All you have to do in most cases is to drop the uf2 file onto the RPI-RP2 "flash
drive" that we found earlier. That's all there is to it! 

# Confirming that it worked

The device should automatically reboot, and the "flash drive" should be gone. In
many cases, it should be ready to type. If it's not typing, we have some
troubleshooting steps below.


# Troubleshooting

## It's not working on Mac

There may still be a bug in Mac's "Finder" that casuse it to hang or not copy.
You'll need to copy it to `/Volumes/RPI-RP2` with a terminal. This is not a bug
with any keyboard software, but a bug in Mac itself. Apple's documentation on
how to do this can be found
[HERE](https://support.apple.com/guide/terminal/manage-files-apddfb31307-3e90-432f-8aa7-7cbc05db27f7/mac).

## It's not typing and I have a split keyboard

Split keyboards are 2 seperate devices pretending to be one keyboard. Each side
has it's own "brain". Just repeat the steps for the other side and you should be
back up and running.

## I still can't type and I've read everything above.

Make sure you have the latest version of peg and restart the program after you
update. That can help in some cases. If that fails, you can back up the files on
the "flash drive", but this one will be named more similar to your keyboard and
not named "RPI-RP2". For a corne, it could be "CRKBDL" or "CRKBDR", or Lulu
could be "LULUL" or "LULUR". If it's a split keyboard, remember to back up both
sides if you wish to do so. After your optional backup, delete all files on all
parts of a keyboard. Make sure to empty the trash. Once you open peg, it should
see it as a brand new keyboard and get you going again.

## None of the advice has worked and I still can't type!

Fear not! Reach out to us in our [Discord](https://discord.gg/2SkMcMxFA9) and
we'll do what we can to get you up and running!
