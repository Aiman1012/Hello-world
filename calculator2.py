# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 12:02:47 2020

@author: User
FOR LOOP 

WHILE LOOP 

while #condition == True:
    do this
    break
"""





loop = True

while loop:
    num1 = float(input("Insert you first number here:\n "))
    operations = input("Enter operator (+,-,*,/,power,%[division with remainder]):\n ")
    num2 = float(input("Insert you second number here (if you chose power this will be your power/insert 0.5 if you wanna do squareroot):\n "))


    if operations == "+" :
         print(str(num1 + num2) +" is the answer")
    elif operations == "-" :
        print(str(num1 - num2) +" is the answer")
    elif operations == "*" :
        print(str(num1 * num2) +" is the answer")
    elif operations == "/": 
        print(str(num1 / num2) +" is the answer")
    elif operations == "%" :
        print(str(num1 % num2) +" is the remainder")
    elif operations == "power":
        print(str(pow(num1, num2)) +" is the answer")
    else:
        print("pi tekan sendiri pakai calculator " + "is the answer.")

    reaction = input("is it accurate?:\n ")
    Quit = input("press enter to continue or press q to quit\n ")
    if Quit =="q":
            loop = False
            break
            
    
    
    
    