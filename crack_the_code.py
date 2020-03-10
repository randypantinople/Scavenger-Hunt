
# -*- coding: utf-8 -*-


from Challenge import Challenge

#Create an object for the class
challenge = Challenge()

#Display the string representation of the object
print(challenge)

#Dsiplay the instructions
print("""
In this challenge, you will have 10 questions to answer. If you correctly answer 
a question, a letter will be  shown. These letters will form a word,
you will need to re-arrange it to crack the code. 
      """)

#Ask user to enter to start the challenge
input("Press ENTER to start ")
print()


#Create a list for the codes
code_list = []

#Set the correct code "AlGORITHMS
code = "ALGORITHMS"

#Iterate for 10 times
for i in range(10):
    
    while True:
        #Call the get_questions funtion and display each question
        print(challenge.get_questions()[i])
        
        while True:
            #Ask user for the answer
            user_answer = input("Please enter your answer as an integer: ")
            print()
            
            #Convert data type into an integer
            try:
                user_answer =int(user_answer)
                
            #Ask the user for correct input   
            except:
                print("Invalid answer! Your answer must be an integer.")
                print()
                continue
            else:
                break
            
        #Check the answer if it matches the answer key
        if user_answer ==challenge.get_answer_key()[i]:
            
            #add the letter in the code clues
            code_list.append(challenge._Challenge__get_code()[i])
            print()
            
            #Display the letters
            print("That was coreect! You unlocked the number {} clue.".format(i+1))
            print("Code clues : {0}".format(", ".join (str(i) for i in code_list)))
            print()
            break
        
        #Ask the user to try again 
        else:
            print("Your answer is incorrect. Please try again.")
            print()
            continue
        
#Display a message 
print("""
      Good Job! You unlocked all 10 clues!
      Now re-arrange the clues for the correct code.""")  
print()         


while True:      
    #Ask the user to enter the code        
    user_code = input("Enter the correct code :  ") 
    
    #Check if the user code mathces the right code
    if user_code.upper() == code:
        #Display conragtulations
        print('''
              **********CONGRATULATIONS*************
              YOU HAVE SUCCESSFULLY CRACKED THE CODE! ''')
        break
        
    # Ask the user to try again
    else:
        print("Oh no! That was not the code. Please try again. You can do it!")
        continue
        
    


