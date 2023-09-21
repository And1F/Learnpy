# lets you import some data and learn the data like flashcards
import pandas as pd
import os
import sys
import time
import random

def import_data(filename, row):
    folder_path = r"C:\Users\YourFolderPath"
    data = list(pd.read_excel(os.path.join(folder_path,filename))[row])
    data = [x.lower() for x in data if type(x) == str]
    return data

def leave(slur):
    print(slur)
    time.sleep(2)
    sys.exit()

def showing(ordr,data):
    while data != []:
        if ordr == "_": indx = random.randint(0,len(data)-1)
        else: indx = int(ordr)
        print(data[indx][0])
        answer = input("")
        if answer.lower() == "restart": return ""
        print(data[indx][1])
        del data[indx]
        time.sleep(2)
        print("")

def inputting(ordr,data):
    fails, wrong = 0,False
    while data !=[]:
        if ordr == "_": 
            if wrong == False:indx = random.randint(0,len(data)-1)
        else: indx = int(ordr)
        print(data[indx][0])
        answer = input("")
        if answer.lower() == "restart": return ""
        elif answer.lower() == data[indx][1]:
            print(f"Correct, {len(data)} to go")
            fails, wrong = 0,False
            del data[indx]
        elif fails == 2:
            print(f"The correct Answer is {data[indx][1].title()}, {len(data)} to go")
            while True:
                answer = input("Repeat this One: ")
                if answer.lower() == data[indx][1]: break
            print("Next One")
            fails, wrong = 0,False
            del data[indx]
        else:
            fails += 1
            wrong = True
            print("Wrong, have another guess")
    print("Well done!")
   
def main():
    #select dataset
    filename = input("Please name the wanted TrainSet from the DataFolder ")
    if not os.path.isfile(os.path.join(r"C:\Users\AND1\Documents\Private_Code\Learnpy\Data", filename)): leave("File does not exist")
    #select repetition:
    rep = input("How many times do you wanna learn the set? ")
    if not rep.isnumeric() or not int(rep) >0:leave("Isches so schwer e positive zahl izgeh, du lappi")
    
    #select mode
    mode = input("With which mode do you want to learn? \n 1 - Just showing the answers\n 2 - Input the answers\nPlease enter the desired number: ")
    if mode not in ["1", "2"]: leave("Isches so schwer 1,2 oder 3 izgeh, du retard")
    # select order
    ordr = input("In what particluar order do you want to learn? \n 1 - First to Last \n 2 - Last to First \n 3 - Mixed \nPlease enter the desired Number: ")
    if ordr not in ["1", "2", "3"]: leave("Isches so schwer 1,2 oder 3 izgeh, du retard")

    #showing
    if mode == "1":
        purpose = import_data(filename, "Purpose")[0]
        print(f"You need to input {purpose.title()}")
        for i in range(int(rep)):
            print(f"{i+1} Session") 
            front = import_data(filename, "Front")
            back = import_data(filename, "Back")
            data = [(front[i].lower(),back[i].lower()) for i in range(len(front))]
            if ordr == "1": ordr = 0
            elif ordr == "2": ordr = -1
            else: ordr = "_" 
            showing(ordr,data)
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
            if ordr == "1": ordr = 0
            elif ordr == "2": ordr = -1
            else: ordr = "_" 
            inputting(ordr,data)
        leave("You're finished")


if __name__ == "__main__":main()