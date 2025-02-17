#Importing Packages
import glob
import cv2 as cv
import pathlib
import csv
import os
#Pit scouting check and normal scouting check
#Scan the QR code and get data
# each line input into Excel and put label next to the entered data

#Pit Scouting

# Scouting
lastValue = ""
values =[""]
text = ""
if(not (os.path.exists("Teams"))):
    os.mkdir("Teams")

if(not (os.path.exists("Teams\\PitScouting"))):
    os.mkdir("Teams\\PitScouting")
if(not (os.path.exists("Teams\\PitScouting\\PitScouting.csv"))):
    open(f"Teams\\PitScouting\\PitScouting.csv", "a").close()
    with open(f"Teams\\PitScouting\\PitScouting.csv", "a", encoding='UTF8') as f:
        w = csv.writer(f)
        w.writerow(["Pit Scouting (Do Not Change)","Team Number", "Width", "Weight", "Drivetrain", "Other Drivetrain","Swerve Ratio","Drivetrain Motor","# of Batteries", "Floor pickup Coral","Floor Pickup Algae","Autos", "Scouting Method", "Comments"])  

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    
    exit()    

while True:

    ret, frame = cap.read()
    detect = cv.QRCodeDetector()
    value, points, stright_qr=detect.detectAndDecode(frame)
    value = value.replace("false", "No")
    value = value.replace("true", "Yes")

    if (len(value) > 0  and lastValue != value):
        lastValue = value
        
        V1 = value.split("\t")

        values = V1

        if (V1[0] == "Pit Scouting"):
            text=V1[1]
            print(f"Team {V1[1]} Pit Scouting data has been scanned")
            if(os.path.exists(f"Teams\\PitScouting\\PitScouting.csv")):
                with open(f"Teams\\PitScouting\\PitScouting.csv", "a", encoding='UTF8') as f:
                    w = csv.writer(f)
                    w.writerow(V1[1:])

        else:
            text=V1[0]
            print(f"Team {V1[0]} match {V1[0]} has been scanned")

            if(os.path.exists(f"Teams\\{V1[0]}.csv")):
                with open(f"Teams\\{V1[0]}.csv", "a", encoding='UTF8') as f:
                    w = csv.writer(f)
                    w.writerow(V1)
            else:
                open(f"Teams\\{V1[0]}.csv", "a").close()
                with open(f"Teams\\{V1[0]}.csv", "a", encoding='UTF8') as f:
                    w = csv.writer(f)
                    w.writerow(["Scouter", "Team #", "Not Important","Not Important","Match #", "Not Important", "Auto Start Position", "Starting Position",
                                "Auto Coral L1", "Auto Coral L2", "Auto Coral L3", "Auto Coral L4", "Leave", "Remove Algae #", "Auto Failed Algae #", "Auto Scoring Position", "Teleop Coral L1"
                                , "Teleop Coral L2", "Teleop Coral L3", "Teleop Coral L4", "Able to Remove Algae",
                                "Processor Score", "Net Score", "Miss #", "Defense slider", "Final Robot Status", "Endgame Comments",
                                "Algae Left In Reef", "Driver skill", "Defense Rating", "Sped Rating", "Died", "Tippy", "Dropped Coral (>2)",
                                "Dropped Algae (>2)", "Dropped Algae (<2)", "Postmatch comments"])
                    w.writerow(V1)

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    font = cv.FONT_HERSHEY_SIMPLEX
    fontScale = 1.25
    color = (255,255,255)
    thickness = 1
    frame=cv.flip(frame, 1)
    cv.putText(frame, f"Scanned:", (25,30), font, fontScale, (0,0,0), 3, cv.LINE_AA)
    cv.putText(frame, f"Scanned:", (25,30), font, fontScale, color, 2, cv.LINE_AA)
    cv.putText(frame, f"{text}", (25,60), font, fontScale, (0,0,0), 3, cv.LINE_AA)
    cv.putText(frame, f"{text}", (25,60), font, fontScale, color, 2, cv.LINE_AA)
    cv.imshow('frame', frame)
    
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

