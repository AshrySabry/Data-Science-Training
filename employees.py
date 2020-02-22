
import sys 
#define a function thar sort and display list
path = '../data/users.txt'

def get_dict(file) :
    thedict = {}
    for line in open(file) :
        # split the string
        items = line.strip().split(':')
        # add items to dictionary
        thedict[items[1]] = [items[0], items[1], items[2], items[3], items[4]]
    return thedict

#define a function that sort and display list
def display(data) :
    for k in sorted(list(data)):
        print(data[k][0].ljust(5), " ",
              data[k][1].ljust(10), " ",
              data[k][2].ljust(5), " ",
              data[k][3].ljust(15), " ",
              data[k][4])
            
#define a function that returns a list
def get_list(file, sortedby) :
    users = list()
    ID, FIRST, MIDDLE, LAST, DEPT = range(5)
    for line in open(file) :
        ID, FIRST, MIDDLE, LAST, DEPT = line.strip().split(':')
        #add to users list
        users.append([ID, FIRST, MIDDLE, LAST, DEPT])

    #sort the list
    sorted_users = sorted(users, key=lambda x : x[sortedby])
    return sorted_users    

def print_list(data) :
    print()
    print("ID".ljust(5),"First".ljust(15), "Middle".ljust(10),"Last".ljust(15), "Dept")
    print()

    for user in data :
        print(user[0].ljust(5), user[1].ljust(15), user[2].ljust(10), user[3].ljust(15),user[4])

#define a menu
def print_menu() :
    print(10 * '-', "SORT BY", 10 * '-')
    print("1. ID")
    print("2. First Name")
    print("3. Middle Name")
    print("4. Last name")
    print("5. DEPT")
    print("Hit enterkey to exit")
    print(30 * "-")

#main method
if __name__ == "__main__" :
    # check if arguments supplied
    if(len(sys.argv) == 1) :
        print("[USAGE] python employees.py filename")
    else :
        # mydata = get_dict(path)
        # display(mydata)
        while True:
            print_menu()
            line = input("Your choice: ")
            if line :
                # chcek if input valid
                [1,2,3,4,5].index(int(line))
                mydata = get_list(sys.argv[1], int(line) - 1)
                print_list(mydata)
                continue
            else :
                print("BYE"); break