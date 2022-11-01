import random
from time import sleep
# f = open("database.txt", "r" ,encoding="utf-8")
# txt = f.read()
# f.close()
# if txt != "":
#     List = txt.split("\n+|+\n")
#     List.pop(List.__len__()-1)
#     text = List[random.randint(0 , List.__len__()-1)]
#     if List.__len__() > 0:
#         for i in range(10):
#             try:
#                 if 1 != 2:
#                     print(text)
#             except:
#                     pass
#         print("End")
#     else:
#         print("Empty")

while True:
    ListTime = [2 , 3 , 4]
    timeS = random.randint(0 , ListTime.__len__()-1)
    print("Timer " , ListTime[timeS])
    sleep(ListTime[timeS])
    f = open("database.txt", "r" ,encoding="utf-8")
    txt = f.read()
    f.close()

    if txt != "":
        List = txt.split("\n+|+\n")
        List.pop(List.__len__()-1)
        text = List[random.randint(0 , List.__len__()-1)]
        if List.__len__() > 0:
            for i in range(1):
                try:
                    if 1 != 2:
                        print(text)
                except:
                    pass
        else:
            print("detabase Empty")