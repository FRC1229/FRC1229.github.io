
import glob
import cv2 as cv
import pathlib
import csv
import os
count = 0
total = 0
mNumber = input("Input Match Number: ")
team1 = input("Input Team 1: ")
# team2 = input("Input Team 2: ")
# team3 = input("Input Team 3: ")
# team4 = input("Input Team 4: ")
# team5 = input("Input Team 5: ")
teamlist = [team1]
if(not (os.path.exists("Compile"))):
    os.mkdir("Compile")

Teams = {}
for team in teamlist:
    Teams[team] = {
        f"Match #": 0,
        f"Scouter": "",
        f"Robot name": "",
        f"Auto Coral L1": 0,
        f"Auto Coral L2": 0,
        f"Auto Coral L3": 0,
        f"Auto Coral L4": 0,
        f"Auto Remove Algae #": 0,
        f"Auto Failed Algae #": 0,
        f"Teleop Coral L1": 0,
        f"Teleop Coral L2": 0,
        f"Teleop Coral L3": 0,
        f"Teleop Coral L4": 0,
        f"Able to remove algae": 0,
        f"Attained Coopertition": 0,
        f"Processor Score": 0,
        f"Net Score": 0,
        f"Miss #": 0,
        f"Defense Slider": "",
        f"Final Robot Status": "",
        f"Algae Left in Reef": 0,
        f"Defense Rating": "",
        f"Speed Rating": "",
        f"Tippy": 0,
        f"Dropped Coral (>2)": 0,
        f"Dropped Algae (>2)": 0
    }


if((os.path.exists("Teams"))):
    for i in teamlist:
        if((os.path.exists(f"Teams\\{i}.csv"))):
             with open(f"Teams\\{i}.csv", "r", encoding='UTF8') as r:
                data = list(csv.reader(r, delimiter=","))
                for row in data:

                    try:
                        Teams[i]["Match #"] += int(row[4])
                        Teams[i]["Scouter"] += str(row[1])
                        Teams[i]["Robot name"] += str(row[5])
                        Teams[i]["Auto Coral L1"] += int(row[7])
                        Teams[i]["Auto Coral L2"] += int(row[8])
                        Teams[i]["Auto Coral L3"] += int(row[9])
                        Teams[i]["Auto Coral L4"] += int(row[19])
                        Teams[i]["Auto Remove Algae #"] += int(row[12])
                        Teams[i]["Auto Failed Algae #"] += int(row[13])
                        Teams[i]["Teleop Coral L1"] += int(row[14])
                        Teams[i]["Teleop Coral L2"] += int(row[15])
                        Teams[i]["Teleop Coral L3"] += int(row[16])
                        Teams[i]["Teleop Coral L4"] += int(row[17])
                        Teams[i]["Able to remove algae"] += int(row[18])
                        Teams[i]["Attained Coopertition"] += int(row[19])
                        Teams[i]["Processor Score"] += int(row[20])
                        Teams[i]["Net Score"] += int(row[21])
                        Teams[i]["Miss #"] += int(row[22]) 
                        Teams[i]["Defense Slider"] += str(row[23])
                        Teams[i]["Final Robot Status"] += str(row[24])
                        Teams[i]["Algae Left in Reef"] += int(row[26])
                        Teams[i]["Defense Rating"] += str(row[27])
                        Teams[i]["Speed Rating"] += str(row[28])
                        Teams[i]["Tippy"] += int(row[30])
                        Teams[i]["Dropped Coral (>2)"] += int(row[32])
                        Teams[i]["Dropped Algae (>2)"] += int(row[33])
                        
                        
                        
                        
                    except:
                        # print("")
                        pass
                        # print(total)
                        # print(count)
                # Teams[i]["Auto Coral L1"] /= count
                # Teams[i]["Auto Coral L2"] /= count
                # Teams[i]["Auto Coral L3"] /= count
                # Teams[i]["Auto Coral L4"] /= count
                # Teams[i]["Teleop Coral L1"] /= count
                # Teams[i]["Teleop Coral L2"] /= count
                # Teams[i]["Teleop Coral L3"] /= count
                # Teams[i]["Teleop Coral L4"] /= count
                # Teams[i]["Auto Remove Algae #"] /= count
                # Teams[i]["Missed #"] /= count
                # Teams[i]["Processor #"] /= count
                # Teams[i]["Net #"] /= count
                # Teams[i]["Algae left in reef"] /= count
else:          
    print("ERROR: No Teams Folder found")

print(Teams)

if(not (os.path.exists("Compile"))):
    os.mkdir("Compile")
mn = "Match #"
sn = "Scouter"
rn = "Robot name"
ac1 = "Auto Coral L1"
ac2 = "Auto Coral L2"
ac3 = "Auto Coral L3"
ac4 = "Auto Coral L4"
ara = "Auto Remove Algae #"
arf = "Auto Failed Algae #"
tc1 = "Teleop Coral L1"
tc2 = "Teleop Coral L2"
tc3 = "Teleop Coral L3"
tc4 = "Teleop Coral L4"
atra = "Able to remove algae"
ac = "Attained Coopertition"
p = "Processor Score"
ns = "Net Score"
m = "Miss #"    
ds = "Defense Slider"
frs = "Final Robot Status"
alir = "Algae Left in Reef"
dr = "Defense Rating"
sr = "Speed Rating" 
t = "Tippy"
dc = "Dropped Coral (>2)"
da = "Dropped Algae (>2)"

open(f"Compile\\{mNumber}.csv", "a").close()
with open(f"Compile\\{mNumber}.csv", "a", encoding='UTF8') as f:
    w = csv.writer(f)
    w.writerow(["Teams", mn, sn, rn,ac1,ac2,ac3,ac4,ara,arf,tc1,tc2,tc3,tc4,atra,ac,p,ns,m,ds,frs,alir,dr,sr,t,dc,da])
    for i in teamlist:
        w.writerow([f"{i}", f"{Teams[i][mn]}", f"{Teams[i][sn]}", f"{Teams[i][rn]}", f"{Teams[i][ac1]}", f"{Teams[i][ac2]}", 
                    f"{Teams[i][ac3]}", f"{Teams[i][ac4]}", f"{Teams[i][ara]}",f"{Teams[i][arf]}",
                    f"{Teams[i][tc1]}" ,f"{Teams[i][tc2]}",f"{Teams[i][tc3]}",f"{Teams[i][tc4]}",f"{Teams[i][atra]}",
                    f"{Teams[i][ac]}",f"{Teams[i][p]}",f"{Teams[i][ns]}",f"{Teams[i][m]}",f"{Teams[i][ds]}",f"{Teams[i][frs]}",
                    f"{Teams[i][alir]}",f"{Teams[i][dr]}",f"{Teams[i][sr]}",f"{Teams[i][t]}",f"{Teams[i][dc]}",f"{Teams[i][da]}"])
print("Done")




