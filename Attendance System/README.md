# Attendance System
In the `images` folder there are images of students and the code written inside `Attendance System.py` file matches the face detected in real time and compares with the the images inside the `images` folder. If the face matches then it marks the attendance else display a message "Unknown". It creates a DataFrame of attendance and keeps appending the attendance of matched students. 
**.load_image_file() :-** we can load the RGB image of the students.
**.encodings() :-**  encodes the image.
**.face_landmarks() :-** give the landmarks of the face.
**.face_location() :-** will give the location of the face on the image.
**.compare_face() :-** it will compare the encodings of faces.
