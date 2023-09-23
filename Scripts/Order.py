# lets you learn some data in a particular order or mixed
import pandas as pd
import os
import sys
import time

def import_data(filename):
    folder_path = r"C:\Users\AND1\Documents\Private_Code\Learnpy\Data"
    data = list(pd.read_excel(os.path.join(folder_path,filename))["Order"])
    data = [x.lower() for x in data]
    return data

def leave(slur):
    print(slur)
    time.sleep(2)
    sys.exit()

def not_mixed(ordr, data):
    fails = 0
    max_fails = 1
    print(f"Please enter the {'first' if ordr == 0 else 'last'} One")
    while data != []:
        answer = input("")
        if answer.lower() == data[ordr]:
            fails = 0
            print(f"Correct, {len(data)} to go")
            del data[ordr]
        elif answer.lower() == "restart": 
            return ""
        elif fails == max_fails:
            print(f"The correct Answer is {data[ordr].title()}")
            while True:
                answer = input("Repeat this One: ")
                if answer.lower() == data[ordr]: break
            print("Next One")
            fails = 0
            del data[ordr]
        else: 
            fails += 1
            print("Wrong, have another guess")
    print("Well done!")

def mixed(data):
    fails = 0
    max_fails = 4
    data = list(set(data))
    print("Please enter any One")
    while len(data) != 0:
        answer  = input("")
        if answer.lower() in data:
            fails = 0
            del data[data.index(answer.lower())]
            print(f"Correct, {len(data)} to go")
        elif answer.lower() == "restart": return ""
        elif fails == max_fails:
            print("Game Over, to many Fails")
            print("These are all the missing Ones")
            for i in data:
                print(i)
            time.sleep(10)
            sys.exit()
        else: 
            fails += 1
            print("Wrong, have another guess")
    print("Well done!")

def select_range(ordr, data):
    rnge = input("Please enter a starting Number to begin \nPress Enter to start at the beginning ")
    if rnge.isnumeric() and 0 < int(rnge) < len(data): 
        print(f"The last you skipped was {data[-int(rnge)].title() if ordr == '2' else data[int(rnge)-1].title()}")
        data = data[:-int(rnge)] if ordr == '2' else data[int(rnge):]
    else: pass
    return data

def main():
    # select dataset
    filename = input("Please name the wanted TrainSet from the DataFolder ")
    if not os.path.isfile(os.path.join(r"C:\Users\AND1\Documents\Private_Code\Learnpy\Data", filename)): leave("File does not exist")
    # select repetition:
    rep = input("How many times do you wanna learn the set? ")
    if not rep.isnumeric() or not int(rep) >0:leave("Isches so schwer e positive zahl izgeh, du lappi")

    # select 1 from front to back 2 back to front or 3 scrambled
    ordr = input("In what particluar order do you want to learn? \n 1 - First to Last \n 2 - Last to First \n 3 - Mixed \nPlease enter the desired Number: ")
    if ordr not in ["1", "2", "3"]: leave("Isches so schwer 1,2 oder 3 izgeh, du retard")

    # First to Last
    if ordr !="3":
        for i in range(int(rep)):
            print(f"{i+1} session")            
            data = import_data(filename)
            data = select_range(ordr, data)
            ordr = 0 if ordr == "1" else -1
            not_mixed(ordr, data)
        leave("You're finished")

    # Mixed
    if ordr == "3":
        for i in range(int(rep)):
            print(f"{i+1} session")
            data = import_data(filename)
            mixed(data)
        leave("You're finished")

        
if __name__ == "__main__":main()