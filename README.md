# Turn Your smFRET Chromatogram Into a Movie

Takes a simple chromatogram image, iterates over it to find x & y positions and writes a .py script that will create
frames of a pymol animation. 

Only takes .png as empty pixels are required.

### Inputs

Inputs required will be:
1. Number of frames in your animation.
2. Height in pixels of your chromatogram image.

### What it does
Iterares through the image, goes down each line of pixels until it finds the first data and logs the y position.

Taking this data, prints a .txt file with the format "mset *frame* x3".

### Pymol
Pasting this text file into pymol console, with animation with 100 frames.


