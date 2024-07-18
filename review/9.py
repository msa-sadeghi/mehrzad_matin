# import os
# os.system("cls")
# while True:
#     command = input("enter a command: ")

#     os.system(command)
#     if input("Do you want to exit? (y or n): ").lower().startswith("y"):
#         break

import subprocess
with open("wifi.txt", "a") as f:
    all_data = subprocess.check_output(["netsh", "wlan", "show", "profiles"])
    all_data = all_data.decode('utf-8')
    all_data = all_data.split("\n")
    all_ssids = []
    for d in all_data:
        if "All User Profile" in d:
            x = d.split(":")[1][1:-1]
            all_ssids.append(x)
    for i in all_ssids:
        res = subprocess.check_output(["netsh","wlan", "show", "profile",str(i),"key=clear"]).decode('utf-8').split("\n")   
        for x in res:
            if 'Key Content' in x:
                y = x.split(":")[1][1:-1]
                f.write(y+"\n")