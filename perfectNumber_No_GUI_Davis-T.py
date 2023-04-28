# A program that tells what numbers are perfect numbers
# between (negative infinity and (n numbers)-given by the user) 
# and also tell how much all the perfect numbers add up to 
# this is done with the programmer exercising the functional
# higher order functions 
#
#
#@Creator Tyon Davis
#
#
import threading
from tkinter import*
from functools import reduce
from multiprocessing import Process, Queue



#(Function: create_list_of)  creates a list && filling it with element of 0 to(n-1)
# with the help of using the built in range function. 
def create_list_of(n):
    list_creation=[item for item in range(0,n)]
    return list_creation

    
#(Function: add_one) adds 1 to the number that is passed
def add_one(n):
    return n+1


#(Function: is_perfect) checks if (n) is a perfect number
def is_perfect(n):
    summ=0
    for low in range(n):
            
            #(Safty) stops error from happening given low s always going to start from 0
            low=low+1
                
            if(n%low==0 ):
                summ=summ+low
                        
            if ((low==n-1)&(summ == n)):
                return True

            if((low==n-1)&(summ != n)):
                 return False

 
#(Function: sum_list)adding each element in the list                    
def sum_list(a, b):
     result = a + b
     return result 
        

#(findPerfect finction)- controls what happens when the user clicks the button           
def findPerfect(num):
    
    #(Security)- do not let user put in a non number value before 
    # checking if the value is big enough
    while True:
        try:
           
            user=num
            break
        except:
            print("Pick a positive (WHOLE NUMBER)!!") 
            


    #(calling function) in this case this wasnt really needed but if I was
    # to change (create_list_of) to C_L and wanted to create many list of different elements
    # it could become useful
    new_list=create_list_of(user)
    
    #debug code
    #print(new_list)

    #(map function) goes thruogh each element in the list and puts in through a function of liking
    #(function,list) only takes vales that it can iterate through
    new_list=map(add_one,new_list) 

    #(Updating)- using the (list) funtion which allows us to be able to view
    # the output from the mapping function
    new_list= list(new_list)

    #debug code
    #print (new_list)


    #(filter function)-take in a 
    # (function the returns a boolean, something it can iterate through like a list)
    # if true the filter keeps it else its drop
    new_list=filter(is_perfect,new_list)
    new_list= list(new_list)


    print("List of perfect numbers between (1-",user,"): ",new_list)

    #(secrity)- informs user to use numbers and stop program from crashing
    # by calling  try - except 
    try:
    #(Reduce function)- gives the programmer the ability to combine
    # elementsin the list in a way that they want.
        sum_of_perfect=reduce(sum_list,new_list)
        print("The perfect numbers sum up to: ",new_list)
    except:
        print('No perfect number exist before this number ')
       
    if(user>5):

        print("Perefect Numbers: ",new_list,"Sums up to: ",sum_of_perfect)
        try:
            start()
        except:
                exit()

#(Function)start program-stop unwanted inputs
def start():
    try:
        user=int(input("Find Perfect Numbers Up to (Enter number): "))
        findPerfect(user)
    except:
            print("Enter a whole number!!")
            start()

#(main line)-START

if __name__ == '__main__':
    start()
    
           
    
#(main line)-END 