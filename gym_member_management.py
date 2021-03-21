import datetime
def gym():
    def gettime():
        return datetime.datetime.now()
    def entry(name):
        if name == 1:
            chart =int(input("Please enter 1 for exercises chart Entry or enter 2 for food chart entry:- "))
            if(chart==1):
                value =input("Write Here\n")
                with open("mrinmoy_ex.txt","a") as op:
                    op.write(str([str(gettime())]) + ": " + value + "\n")
                print("successfully written")
                again()
            elif(chart==2):
                value = input("Write Here\n")
                with open("mrinmoy_food.txt", "a") as op:
                    op.write(str([str(gettime())]) + ": " + value + "\n")
                print("successfully written")
                again()

        if name == 2:
            chart =int(input("Please enter 1 for exercises chart Entry or enter 2 for food chart entry:- "))
            if(chart==1):
                value =input("Write Here\n")
                with open("manika_ex.txt","a") as op:
                    op.write(str([str(gettime())]) + ": " + value + "\n")
                print("successfully written")
                again()
            elif (chart == 2):
                value = input("Write Here\n")
                with open("manika_food.txt", "a") as op:
                    op.write(str([str(gettime())]) + ": " + value + "\n")
                print("successfully written")
                again()

        if name == 3:
            chart =int(input("Please enter 1 for exercises chart Entry or enter 2 for food chart entry:- "))
            if(chart==1):
                value =input("Write Here\n")
                with open("ratan_ex.txt","a") as op:
                    op.write(str([str(gettime())]) + ": " + value + "\n")
                print("successfully written")
                again()
            elif (chart == 2):
                value = input("Write Here\n")
                with open("ratan_food.txt", "a") as op:
                    op.write(str([str(gettime())]) + ": " + value + "\n")
                print("successfully written")
                again()
    def show(name):
        if name == 1:
            chart = int(input("Please enter 1 for exercises chart show or enter 2 for food chart show- "))
            if (chart == 1):
                with open("mrinmoy_ex.txt") as op:
                    for item in op:
                        print(item,end="")

                    again()
            elif (chart==2):
                with open("mrinmoy_food.txt") as op:
                    for item in op:
                        print(item,end="")
                    again()
        if name == 2:
            chart = int(input("Please enter 1 for exercises chart show or enter 2 for food chart show- "))
            if (chart == 1):
                with open("manika_ex.txt") as op:
                    for item in op:
                        print(item,end="")
                    again()
            elif (chart==2):
                with open("manika_food.txt") as op:
                    for item in op:
                        print(item,end="")
                    again()

        if name == 3:
            chart = int(input("Please enter 1 for exercises chart show or enter 2 for food chart show- "))
            if (chart == 1):
                with open("ratan_ex.txt") as op:
                    for item in op:
                        print(item,end="")
                    again()
            elif (chart==2):
                with open("ratan_food.txt") as op:
                    for item in op:
                        print(item,end="")

                        again()




    print("Welcome to Mrinmoy Health Management System")
    entry_show =int(input("Write 1 for entry and 2 Show:- "))
    if entry_show==1:
        b= int(input("Press 1 for Mrinmoy Press 2 for Manika Press 3 Ratan:- "))
        entry(b)
    elif entry_show==2:
        b= int(input("Press 1 for Mrinmoy Press 2 for Manika Press 3 Ratan:- "))
        show(b)
    else:
        print("Please enter 1 or 2 ")



def again():
    cal_again = input('''
    Do you want to Run Programme  again?
    Please type y for YES or n for NO.
    ''')

    if cal_again == 'y':
        gym()
    elif cal_again == 'n':
        print("See You Later")
    else:
        again()


gym()