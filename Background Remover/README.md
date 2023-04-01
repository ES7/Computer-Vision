Using the mediapipe library I have written a python script to remove the background in the real time. It also access the images from the 'Images' folder and
replace the background with that image, we can change the image in the background by pressing 'd' key to put the next image or 'a' key to put the previous image.
We can improve the finishing of the removed part by adjusting the threshold value in `segmentor.removeBG()` function. Note that the dimensions of the images
that we are passing here from the Images folder should be same as the window dimension, here the window dimension is `640x480` pixels.
