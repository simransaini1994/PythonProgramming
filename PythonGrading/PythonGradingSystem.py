#author : Simranjit Singh

import sys

StudentDict = {'simranjit': [87, 98, 100, 89], 'jasmine':  [89, 67, 76,78]}
def login(user, password):
    try:
        if user =='admin' and password == 'admin':
            print("----login successful----")
            return True
        else:
            print("-----login unsuccessful exiting code-----")
            sys.exit()
            return False
    except Exception as e:
        print (e)


def menu(input):
    if input == 1:
        enterNewStudent()

    elif input == 2:
        removeStudent()

    elif input == 3:
        print("3")

    elif input == 4:
        findStudent()

    elif input == 5:
        enterGrade()

    elif input == 6:
        sys.exit()

    else:
        print("Invalid input")


def enterNewStudent ():
    entering = True
    while entering:

        name = input("Enter Name of Student : ")
        grade = input("Enter Grades separated by space:")
        userGrades = list(map(int,(grade.split())))
        StudentDict[name]=userGrades


        repeat = input("Do you want to add  more students data?? Enter Y|y or N/n: ")
        if repeat == 'n' or repeat == 'N':
            entering = False
            for name, UserGrades in StudentDict.items():
                print(name + " got " + str(UserGrades))
            mainfunction()

def enterGrade():
    entering = True
    while entering:

        name = input("Enter Name of Student : ")
        grade = int(input("Enter Grade to add: "))
        StudentDict[name].append(grade)

        repeat = input("Do you want to add  more grades?? Enter Y|y or N/n: ")
        if repeat == 'n' or repeat == 'N':
            entering = False
            for name, UserGrades in StudentDict.items():
                print(name + " got " + str(UserGrades))
            mainfunction()

def removeStudent ():
    entering = True
    try:
        while entering:
            name = input("Enter Name of Student : ")
            del StudentDict[name]
            repeat = input("Do you want to remove more students??: Enter Y|y or N|n ")
            if repeat == 'n' or repeat == 'N':
                entering = False
                for name, UserGrades in StudentDict.items():
                    print(name + " got " + str(UserGrades))
                mainfunction()
    except KeyError as k:
        print(str(k) + " student doesn't exist")


def findStudent():
    entering = True
    try:
        while entering:
            name = input("Enter Name of Student : ")
            print(StudentDict[name])
            repeat = input("Do you want to see other student information?: Enter Y|y or N|n ")
            if repeat == 'n' or repeat == 'N':
                entering = False
                mainfunction()
    except KeyError as k:
        print(str(k) + " student doesn't exist")


def mainfunction():
    print("WELCOME TO SIMRANJIT'S GRADING SYSTEM \n")
    print(" [1] Add New Student Data \n [2] Remove Student \n [3] Students Average\n [4] Student Information\n [5] Update Student info \n [6] Exit")
    try:
        menuChoice= int(input("Enter your Choice: "))
        menu(menuChoice)

    except ValueError as v:
        print("Only integer allowed")



if __name__ == '__main__':
    user = input("Enter Username: ")
    password = input("Enter your Password: ")
    login(user, password)
    mainfunction()
