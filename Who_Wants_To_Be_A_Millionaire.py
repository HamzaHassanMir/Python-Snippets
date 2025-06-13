# Create a program capable of displaying questions to user like TV show Who wants to be a millionaire
# Use List datatype to store questions and their correct answers
# Display the final amount the person is taking home after playing the game.

questions=["What is Which animal is known as the \'Ship of the Desert\'?",
           "How many letters are there in the English alphabet?",
           "Rainbow consist of how many colours?",
           "Baby frog is known as...",
           "How many consonants are there in the English alphabet?"] 

answers= ["Camel","26 letters","7 Colors","Tadpole","21 Consonants"]
price = 0
levels = [1000,2000,3000,5000,10000]

length = len(questions)
loop_iterater = 0

while(loop_iterater < length):
    print(f"Your next question is for Rs.{levels[loop_iterater]} \n") 
    print(questions[loop_iterater])
    print("Apkay options yeh rahay ap ki computer screen par :")
    print(f"a.{answers[0]}                b.{answers[1]}")
    print(f"c.{answers[2]}              d.{answers[3]}" )  
    print (f"e.{answers[4]}")

    user_answer = input("Enter your answer or Enter 0 to quit: ")
    if(user_answer == 0):
        break
        print("Your home take away money is Rs. ",levels[loop_iterater-1])
    elif(user_answer.lower() == answers[loop_iterater].lower()):
        print("Correct answer! You earn RS ",levels[loop_iterater],"\n")
        price += levels[loop_iterater]
        loop_iterater = loop_iterater + 1 
    else:
        print("Incorrect answer! \n Game Over!!!!!")
        break   
print("Final Amount ",price)  

