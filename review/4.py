# x = 612
# print(x % 10)
# print(x % 100)

# x = str(x)
# print(x[-1])
# print(x[-2:])

def writeToFile(filename, text):
    # Open the file in write mode:
    with open(filename, "w") as fileObj:
        # Write the text to the file:
        fileObj.write(text)

writeToFile("my_file.txt", "artin and sara are friends")