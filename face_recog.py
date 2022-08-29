import cv2
import face_recognition as ff
font=cv2.FONT_HERSHEY_SIMPLEX
Heston_image=ff.load_image_file("C:/Users/haast/OneDrive/Documents/Python/DemoImages/known/Charleton Heston.jpg")
Heston_loc=ff.face_locations(Heston_image)[0]
Heston_encode=ff.face_encodings(Heston_image)[0]

Paul_Image=ff.load_image_file("C:/Users/haast/OneDrive/Documents/Python/DemoImages/known/Paul McWhorter.jpg")
Paul_loc=ff.face_locations(Paul_Image)[0]
Paul_encode=ff.face_encodings(Paul_Image)[0]

Verma_image=ff.load_image_file("C:/Users/haast/OneDrive/Documents/Python/DemoImages/known/Seema Verma.jpg")
Verma_loc=ff.face_locations(Verma_image)[0]
Verma_encode=ff.face_encodings(Verma_image)[0]

Ronald_image=ff.load_image_file("C:/Users/haast/OneDrive/Documents/Python/DemoImages/known/Ronald Reagan.jpg")
Ronald_loc=ff.face_locations(Ronald_image)[0]
Ronald_encode=ff.face_encodings(Ronald_image)[0]

knownImages_encode=[Heston_encode,Paul_encode,Verma_encode,Ronald_encode]
names=["Charlton Heston","paul","Seema","Ronald Reagan"]

unknownImage=ff.load_image_file("C:/Users/haast/OneDrive/Documents/Python/DemoImages/unknown/u12.jpg")
unknownImage_locs=ff.face_locations(unknownImage)
unknownImage_BGR=cv2.cvtColor(unknownImage,cv2.COLOR_RGB2BGR)
unknownImage_encodes=ff.face_encodings(unknownImage_BGR,unknownImage_locs)
for unknownImage_loc,unknownImage_encode in zip(unknownImage_locs,unknownImage_encodes):
    print(unknownImage_loc)
    top,right,bottom,left=unknownImage_loc
    cv2.rectangle(unknownImage_BGR,(left,top),(right,bottom),(0,0,255),2)
    name="Unknown Image"
    matches=ff.compare_faces(knownImages_encode,unknownImage_encode)
    print(matches)
    if True in matches:
        matchesIndex=matches.index(True)
        print(matchesIndex)
        name=names[matchesIndex]
        print(name)
    cv2.putText(unknownImage_BGR,name,(left,top),font,1,(255,0,0),2)
cv2.imshow("Windows",unknownImage_BGR)



cv2.waitKey(10000)