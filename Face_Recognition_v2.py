import cv2
import face_recognition as FR
import glob

i=-1

known = FR.load_image_file("D:\AI\loop\Screenshot 2024-04-07 120013.png")
knownC = cv2.cvtColor(known,cv2.COLOR_RGB2BGR)
knownFace = FR.face_encodings(knownC)[0]

j=0

li = []

folder_path = "D:\AI\loop"
image = glob.glob(folder_path + '/*.png')

while True:
    
    i = i+1
    
    v = FR.load_image_file(image[j])

    vc = cv2.cvtColor(v,cv2.COLOR_RGB2BGR)

    m = FR.face_locations(vc)
    print(m)
    #print(len(m))
    if m == [0]:
        i=-1
        j=j+1
    else:    

        nthface = [m[i]]

        #print(i)
        unk_Face = FR.face_encodings(vc)[i]
        results = FR.compare_faces([knownFace],unk_Face)
        print(unk_Face)
        if results[0]:
            li.append(image[j])
            for(x,y,w,h) in  nthface:
                cv2.rectangle(vc,(h,x),(y,w),(0,255,0),2)
        else:
            for(x,y,w,h) in  nthface:
                cv2.rectangle(vc,(h,x),(y,w),(0,0,255),2)


        #print(unknownFace)
        #cv2.imshow("new",vc)
        #cv2.waitKey(10)
        if i == len(m)-1:
            i=-1
            j=j+1

    if j == len(image)-1:
        print(li)
        print("The above array displayed contains path to the images only with the known faces....")
        print("There are total ", len(li)," number of images found containig the known face.")
        break
        