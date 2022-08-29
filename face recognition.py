from tkinter import font
import cv2
import face_recognition as ff
Font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
image1=ff.load_image_file("C:/Users/haast/OneDrive/Documents/Python/DemoImages/known/Donald Trump.jpg")
image1_loc=ff.face_locations(image1)[0]
image1_encode=ff.face_encodings(image1)[0]

image2=ff.load_image_file("C:/Users/haast/OneDrive/Documents/Python/DemoImages/known/Nancy Pelosi.jpg")
image2_loc=ff.face_locations(image2)[0]
image2_encode=ff.face_encodings(image2)[0]

image3=ff.load_image_file("C:/Users/haast/OneDrive/Documents/Python/DemoImages/known/Mike Pence.jpg")
image3_loc=ff.face_locations(image3)[0]
image3_encode=ff.face_encodings(image3)[0]

knownEncoding=[image1_encode,image2_encode,image3_encode]
names=["Trump","Pelosi","Pence"]

unknownImage=ff.load_image_file("C:/Users/haast/OneDrive/Documents/Python/DemoImages/unknown/u1.jpg")
unknownImage_BGR=cv2.cvtColor(unknownImage,cv2.COLOR_RGB2BGR)
unknownImage_locs=ff.face_locations(unknownImage_BGR)
unknownImage_encodes=ff.face_encodings(unknownImage_BGR,unknownImage_locs)

for unknownImage_loc,unknownImage_encode in zip(unknownImage_locs,unknownImage_encodes):
    print(unknownImage_loc)
    top,right,bottom,left=unknownImage_loc
    cv2.rectangle(unknownImage_BGR,(left,top),(right,bottom),(0,0,255),2)
    name="Unknown"
    matches=ff.compare_faces(knownEncoding,unknownImage_encode)
    print(matches)
    if True in matches:
        matchIndex=matches.index(True)
        print(matchIndex)
        print(names[matchIndex])
        name=names[matchIndex]
    cv2.putText(unknownImage_BGR,name,(left,top),Font,1,(255,0,0),2)
cv2.imshow("My face",unknownImage_BGR)



#cv2.imshow("Windows")
cv2.waitKey(10000)
