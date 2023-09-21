# Attendance System
In the `images` folder there are images of students and the code written inside `Attendance System.py` file matches the face detected in real time and compares with the the images inside the `images` folder. If the face matches then it marks the attendance else display a message "Unknown". It creates a DataFrame of attendance and keeps appending the attendance of matched students. <br>
**.load_image_file() :-** we can load the RGB image of the students.<br>
**.encodings() :-**  encodes the image.<br>
**.face_landmarks() :-** give the landmarks of the face.<br>
**.face_location() :-** will give the location of the face on the image.<br>
**.compare_face() :-** it will compare the encodings of faces.<br>
