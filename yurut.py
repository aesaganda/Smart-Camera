from operator import index
from os import name
import time
import cv2
import face_recognition as FR
from numpy.core.getlimits import _KNOWN_TYPES
import pickle
import datetime

class yurut:
    def camera():
        isName = ""
        print(cv2.__version__)
        font = cv2.FONT_HERSHEY_SIMPLEX

        # set camera window size
        width = 1280
        height = 720

        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        cam.set(cv2.CAP_PROP_FPS, 10)
        cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
        ### Fps filter ##
        # Low Pass Filter logic applies here
        # calculates t2
        tLast = time.time()
        fpsFILTER = 10
        time.sleep(0.1)

        # Add newly trained data to this array
        """
                    knownEncodings = [aesFaceEncode, donFaceEncode,
                                    nancyFaceEncode, penceFaceEncode]
                    names = ["Aziz Eren Saganda", "Donald Trump", "Nancy Pelosi", "Mike Pence"]
                    """

        with open("train.pkl", "rb") as f:
            names = pickle.load(f)
            knownEncodings = pickle.load(f)

        while True:
            # dT = t2 - t1
            # t1 is measured with time.time()
            dT = time.time() - tLast
            print(dT)
            fps = 1 / dT
            fpsFILTER = fpsFILTER * 0.75 + fps * 0.25
            print(fps)
            tLast = time.time()

            # Detect and skip bad frames
            ignore, unknownFace = cam.read()
            # use BGR with cv2 commands
            unknownFace = cv2.resize(unknownFace, (0, 0), fx=0.35, fy=0.35)
            unknownFaceRGB = cv2.cvtColor(unknownFace, cv2.COLOR_BGR2RGB)
            faceLocations = FR.face_locations(unknownFaceRGB)
            unknownEncodings = FR.face_encodings(unknownFaceRGB, faceLocations)

            for faceLocation, unknownEncoding in zip(faceLocations, unknownEncodings):
                top, right, bottom, left = faceLocation
                print(faceLocation)
                cv2.rectangle(unknownFace, (left, top), (right, bottom), (255, 0, 0),
                                        3)
                name = "Unknown Person"
                matches = FR.compare_faces(knownEncodings, unknownEncoding)
                print(matches)

                if True in matches:
                    matchIndex = matches.index(True)
                    print(matchIndex)
                    print(names[matchIndex])
                    name = names[matchIndex]

                    if(isName != name):
                        noww = datetime.datetime.now()
                        date = datetime.datetime.strftime(noww, "%c")
                        
                        isName =  name

                        nameWrite = name + "        " + date + "\n" 
                        with open("simple.txt", "a") as f:
                            f.write(nameWrite)

                cv2.putText(unknownFace, name, (left, top), font, 0.75, (0, 0, 255), 2)
            cv2.rectangle(unknownFace, (0, 0), (120, 40), (0, 0, 0), -1)
            cv2.putText(unknownFace,str(int(fpsFILTER)) + " FPS", (0, 25), font, 1, (0, 255, 0), 2)

            # Press q to exit program
            cv2.imshow("My Faces", unknownFace)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cam.release()
        cv2.destroyAllWindows()
                