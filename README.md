# Peg Boards

This repo contains data that the server behind Peg interacts with. I will give you the over view here but look at the [docs](./docs/README.md) for more information.

## Docs

For details on the parts of your keymap or layout file look over the docs.

[Docs](./docs/README.md)

If you are looking to add your board to Peg look over the docs then the contributing page.

[Contributing](./docs/contributing.md)

## Over view and folders

### keyboards

This is where all keyboards are stored and you can put them on your CPY drive from here or after they are in this repo the Peg app will alow you to add them to your board.

### Peg shared features folders

The folders:

* codeBlocks
* keycodes
* keyMaps
* ledMaps
* oleds

Are all available to you if you want them and are stored here for all to see and review.
How helpful they are to you with out the Peg client is another story, some like keymap, codeBlock, ledMap can be very quick to convert to python code that you can run.
Others like oled are far less useful being that it is internal Peg data and would need the Peg client to convert it into bmp files.
