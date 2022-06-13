# Aruco-Placement-Section
ID detector :- It will detect the IDs of all four aruco markers.

Atulya :- Here first I have imported all the necessary libraries 
and images, then I have made a list of aruco markers and its ids,
I have made a function "findArucoMarkers" which will return IDs and
then I have appended IDs list w.r.t the return value of above function.
Then I have made a function arucocoordinates which will find the coordinates
of aruco markers, cropimg function will crop the markers and remove its
white padding, fixaruco function will find the angle of marker and will rotate
it such that angle becomes zero so it will be easy to crop.findColor function
will check  the color of squares and return its corresponding ID value.
In for loop I have first find the contours and stored it in approx, then I have
detected squares using boundingRect function, the if statment wil check the
angle of each square and its height and width. The next if statments will check
the color of each square by calling findColor function, then it will fill the
square with black color, it will resize the corresponding aruco marker and rotate
with the same angle as of square and then it will replace the square with marker.
For loop will iterate four times as we have four squares and the final image is
saved as new.jpg.
