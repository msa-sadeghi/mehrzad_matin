# def getChessSquareColor(row, col):
#     # if (row % 2 == 0 and col % 2 == 0) or (row % 2 == 1 and col % 2 == 1):
#     if row % 2 == col % 2:
#         return "White"
#     else:
#         return "Black"
    
# print(getChessSquareColor(1, 1))
# print(getChessSquareColor(2, 1))
# print(getChessSquareColor(1, 2))
# print(getChessSquareColor(8, 8))
# print(getChessSquareColor(0, 8))
# print(getChessSquareColor(2, 9))


# x = "firefox"
# print(x.index("fox"))
# print(x.find("fox"))
# print(x.replace("fox", "dog"))


# def findAndReplace(text, oldText, newText):
#     final_text = ""
#     i = 0
#     while i < len(text):
#         if text[i:i+len(oldText)] == oldText:
#             final_text += newText
#             i += len(oldText)
#         else:
#             final_text += text[i]
#             i += 1
#     return final_text
# print(findAndReplace("firefox", "fox","dog"))
# print(findAndReplace('The fox', 'fox', 'dog'))
# print(findAndReplace('fox', 'fox', 'dog'))
# print(findAndReplace('Firefox', 'fox', 'dog'))
# print(findAndReplace('foxfox', 'fox', 'dog'))
# print(findAndReplace('The Fox and fox.', 'fox', 'dog'))     


def get_time(sec):
    if sec == 0:
        return "0s"
    
    hours = 0
    while sec >= 3600:
        hours += 1
        sec -= 3600
        
    minutes = 0
    while sec >= 60:
        minutes += 1
        sec -= 60
        
    seconds = sec
    
    return f"{hours}h : {minutes}m : {seconds}s"

print(get_time(3601))
print(get_time(360000001))
print(get_time(360406001))