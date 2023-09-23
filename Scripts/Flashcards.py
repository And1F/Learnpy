# lets you import some data and learn the data like flashcards
import pandas as pd
import os
import sys
import time
import random

def import_data(filename, row):
    folder_path = r"yourFilepath"
    data = list(pd.read_excel(os.path.join(folder_path,filename))[row])
    data = [x.lower() for x in data if type(x) == str]
    return data

def leave(slur):
    print(slur)
    time.sleep(2)   
    sys.exit()

def showing(ordr,side,data):
    side = 0 if side == "1" else 1
    while data != []:
        if ordr == "3": indx = random.randint(0,len(data)-1)
        else: indx = 0 if ordr == "1" else -1
        print(data[indx][side if side == 0 else 1].title())
        answer = input("")
        if answer.lower() == "restart": return ""
        print(data[indx][1 if side == 0 else 0].title())
        del data[indx]
        time.sleep(1)
        print("")


def inputting(ordr,side,data):
    side = 0 if side == "1" else 1
    fails, wrong = 0,False
    while data !=[]:
        if ordr == "3": 
            if not wrong :indx = random.randint(0,len(data)-1)
        else: indx = 0 if ordr == "1" else -1
        print(data[indx][side if side == 0 else 1].title())
        answer = input("")
        if answer.lower() == "restart": return ""
        elif answer.lower() == data[indx][1 if side == 0 else 0]:
            print(f"Correct, {len(data)} to go")
            fails, wrong = 0,False
            del data[indx]
        elif fails == 2:
            print(f"The correct Answer is {data[indx][1 if side == 0 else 0].title()}, {len(data)} to go")
            while True:
                answer = input("Repeat this One: ")
                if answer.lower() == data[indx][1 if side == 0 else 0]: break
            print("Next One")
            fails, wrong = 0,False
            del data[indx]
        else:
            fails += 1
            wrong = True
            print("Wrong, have another guess")
    print("Well done!")


def select_range(ordr, data):
    rnge = input("Please enter a starting Number to begin \nPress Enter to start at the beginning ")
    if rnge.isnumeric() and 0 < int(rnge) < len(data): 
        print(f"The last you skipped was {data[-int(rnge)][0].title() if ordr == '2' else data[int(rnge)-1][0].title()}")
        data = data[:-int(rnge)] if ordr == '2' else data[int(rnge):]
    else: pass
    return data

def main():
    #select dataset
    filename = input("Please name the wanted TrainSet from the DataFolder ")
    if not os.path.isfile(os.path.join(r"C:\Users\AND1\Documents\Private_Code\Learnpy\Data", filename)): leave("File does not exist")
    #select repetition:
    rep = input("How many times do you wanna learn the set? ")
    if not rep.isnumeric() or not int(rep) >0:leave("Isches so schwer e positive zahl izgeh, du Lappi")
    
    #select mode
    mode = input("With which mode do you want to learn? \n 1 - Just showing the answers\n 2 - Input the answers\nPlease enter the desired number: ")
    if mode not in ["1", "2"]: leave("Isches so schwer 1 oder 2 izgeh, du Retard")

    #select side
    side = input("Which side do you want to learn?\n 1 - Front\n 2 - Back\nPlease enter the desired number: ")
    if mode not in ["1", "2"]: leave("Isches so schwer 1 oder 2 izgeh, du Spasst")

    #select order
    ordr = input("In what particluar order do you want to learn? \n 1 - First to Last \n 2 - Last to First \n 3 - Mixed \nPlease enter the desired Number: ")
    if ordr not in ["1", "2", "3"]: leave("Isches so schwer 1,2 oder 3 izgeh, du Retard")

    #showing
    if mode == "1":
        purpose = import_data(filename, "Purpose")[0]
        print(f"If you press enter you see {purpose.title()}")
        for i in range(int(rep)):
            print(f"{i+1} Session") 
            front = import_data(filename, "Front")
            back = import_data(filename, "Back")
            data = [(front[i].lower(),back[i].lower()) for i in range(len(front))]
            data = select_range(ordr,data)
            showing(ordr,side,data)
        leave("You're finished")

    #inputting
    if mode == "2":
        purpose = import_data(filename, "Purpose")[0]
        print(f"You need to input {purpose.title()}")
        for i in range(int(rep)):
            print(f"{i+1} Session") 
            front = import_data(filename, "Front")
            back = import_data(filename, "Back")
            data = [(front[i].lower(),back[i].lower()) for i in range(len(front))]
            data = select_range(ordr,data)
            inputting(ordr,side,data)
        leave("You're finished")


if __name__ == "__main__":main()
