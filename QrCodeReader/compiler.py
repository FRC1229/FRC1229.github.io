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

Teams = {}
for team in teamlist:
    Teams[team] = {
        f"Match #": 0,
        f"Auto Coral L1": 0, 
        f"Auto Coral L2": 0,
        f"Auto Coral L3": 0,
        f"Auto Coral L4": 0,
        f"Teleop Coral L1": 0,
        f"Teleop Coral L2": 0,
        f"Teleop Coral L3": 0,
        f"Teleop Coral L4": 0,
        f"Auto Remove Algae #": 0,
        f"Missed #": 0,
        f"Processor #": 0,
        f"Net #": 0,
        f"Algae left in reef": 0
    }

if((os.path.exists("Teams"))):
    for i in teamlist:
        if((os.path.exists(f"Teams\\{i}.csv"))):
             with open(f"Teams\\{i}.csv", "r", encoding='UTF8') as r:
                data = list(csv.reader(r, delimiter=","))
                for row in data:
                    try:
                        Teams[i]["Match #"] += int(str(row[5]).lstrip("0"))
                        # Teams[i]["Auto Coral L1"] += int(row[8])
                        # Teams[i]["Auto Coral L2"] += int(row[9])
                        # Teams[i]["Auto Coral L3"] += int(row[10])
                        # Teams[i]["Auto Coral L4"] += int(row[11])
                        # Teams[i]["Teleop Coral L1"] += int(row[16])
                        # Teams[i]["Teleop Coral L2"] += int(row[17])
                        # Teams[i]["Teleop Coral L3"] += int(row[18])
                        # Teams[i]["Teleop Coral L4"] += int(row[19])
                        # Teams[i]["Auto Remove Algae #"] += int(row[15])
                        # Teams[i]["Missed #"] += int(row[23])
                        # Teams[i]["Processor #"] += int(row[21])
                        # Teams[i]["Net #"] += int(row[22])
                        # Teams[i]["Algae left in reef"] += int(row[27])
                        
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

al1 = "Auto Coral L1"
al2 = "Auto Coral L2"
al3 = "Auto Coral L3"
al4 = "Auto Coral L4"
tc1 = "Teleop Coral L1"
tc2 = "Teleop Coral L2"
tc3 = "Teleop Coral L3"
tc4 =  "Teleop Coral L4"
ara = "Auto Remove Algae #"
m = "Missed #"
p = "Processor #"
n = "Net #"
alr = "Algae left in reef"

open(f"Compile\\{mNumber}.csv", "a").close()
with open(f"Compile\\{mNumber}.csv", "a", encoding='UTF8') as f:
    w = csv.writer(f)
    w.writerow(["Teams", al1, al2, al3, al4, tc1, tc2, tc3, tc4, ara, m, p, n, alr])
    for i in teamlist:
        w.writerow([f"{i}", f"{Teams[i][al1]}", f"{Teams[i][al2]}", f"{Teams[i][al3]}", f"{Teams[i][al4]}", f"{Teams[i][tc1]}", f"{Teams[i][tc2]}", f"{Teams[i][tc3]}", f"{Teams[i][tc4]}", f"{Teams[i][ara]}", f"{Teams[i][m]}", f"{Teams[i][p]}", f"{Teams[i][n]}", f"{Teams[i][alr]}"])

