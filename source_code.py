# Quiz program 
# import all required libraries to call ready functions 
from collections import namedtuple
from tkinter.messagebox import QUESTION
import random
import emoji 

# Present all the questions in tuples with multiple answers and specify the correct answer.
Question= namedtuple("Question", ["question", "answers", "correct_answer"])

# Welcoming message that will be used later. 
Welcoming = """Hello {name}, welcome to the Quiz ! 
Enter the answer number to proceed to the next question
You will be asked {n} questions.
Best of luck! \U0001f600 """

# This function will be called when the current user finishes the quiz to ask if someone else wants to take the quiz afterwards. 
def competitor():
            new_user = input("Anybody else wants to take the quiz?(yes or no): ")
            # Returns a string after converting all characters to upper case
            new_user = new_user.upper()
            if new_user =="YES":
                return True
                
            else:
                return False


# Declaring a dictionary that will be used in the program later. 
myDict = {} 

# Creating a function to take the number of questions that the user wants to take and present it
# The program will stop when the specified number of questions is reached 
# Return questions at random each time the quiz is taken
def user_questions(questions_num):
    questions_num = min(questions_num, len(questions))
    return random.sample(questions, k=questions_num)

# Function to run the quiz 
def play_quiz(name, questions):

    # The function will only run through a specific number of questions the user has selected.
    questions = user_questions(
    questions_num=quiz_questions 
    )
    
    score = 0

     # For Loop that runs through questions and their answers 
    for question in questions:
        print(question.question)
        for i, answer in enumerate(question.answers, start=1):
            print(f"{i}. {answer}")

        answers=["1","2","3","4"]

        # The user will enter his/her answer here.   
        response = input("Your answer is: ")

        # if user enter different answer not listed in the option, the program will raise error and ask for corrent entry.  
        while response not in answers:
             print("you need to enter one of the answers 1,2,3 or 4")
             response=input()

        # After the user answers the question, the program will raise a message saying whether the answer is correct or not.
        # The program will not add a score if the answer is incorrect. Instead, it will print the correct answer and pass it to the next question.
        # If the answer is correct, the program will add a score.

        if response != question.correct_answer:
            print(emoji.emojize(f"Sorry, that is incorrect :zipper-mouth_face: , the correct answer is {answer}"))
        else:
            print(emoji.emojize(f'Well done :thumbs_up: {response} is correct '))
            # Counter to calculate the score. 
            score += 1 

        # When the user finishes the quiz, the program will save the user name and score in a dictionary that has been declared before.
        # This way will make the data easily accessible for later use and can be called all at once. 
        myDict[name]=int((score/10)*100)

        # Print the current score while the quiz is running 
        print(f"Your current score is {int((score/10)*100)}% out of {int(len(questions)*10)}%")

    # Print the final score for the user.
    print(f"Your final score is {int((score/10)*100)}% out of {int(len(questions)*10)}%")
    print(f"Thank you {name} for playing the quiz, goodbye! \U0001f600")




# The if-statement is used here to run the code only if our program is executed. 
if __name__ == "__main__": 
    questions = [Question("Which planet has the most moons ? ",
                          ["Saturn", "Mercury", "Venus", "Uranus"], "1"),
                 Question("Where is the smallest bone in human ? ",
                          ["Back", "Ear", "Finger", "Leg"], "2",),
                          Question("How many hearts does an octopus have ? ",
                          ["7", "1", "2", "3"], "4",),
                          Question("Which city had the first ever fashion week ? ",
                          ["New York", "Paris", "France", "Italy"], "1",),
                          Question("What is the smallest country in the world ? ",
                          ["Monaco", "Nauru", "Southern France", "Vatican City"], "4",),
                          Question("Which london underground line has the most stations ? ",
                          ["Bond Street", "Westminster", "Central", "District line"], "4",),
                          Question("Which UK city is banksy from ? ",
                          ["Bristol", "London", "Birmingham", "Manchester"], "1",),
                          Question("What is the smallest unit of memory ? ",
                          ["Megabytes", "Gigabyte", "kilobytes", "Terabyte"], "3",),
                          Question("Which animal can be seen on the porshe logo ? ",
                          ["zebra", "moose", "horse", "Okapi"], "3",),
                          Question("What is your body's largest organ ",
                          ["brain", "liver", "spleen", "Skin"], "4",)
                 ]

    # Asks the player to enter the username.       
    name = input("What is your name? ").title()

    numbers=[1,2,3,4,5,6,7,8,9,10]

    # Check if the name is empty, has digits, or less than three characters. If one of these condition occurs, the program will ask the user for valid name.
    # if the name is valid, then welcoming msg will be preseted and the quiz will start.  
    while len(name)== 0 or len(name)< 3 or name.isdigit(): 
        print("Enter correct name to proceed to the quiz")
        name=input()
    else:
        # Asks the number of question that user wants to take and convert it from string to int so it can be used later
        quiz_questions = int(input("How many questions would you like to answer ? the maximum number of questions  is 10 "))
        # Check input if valid
        while quiz_questions not in numbers:
                print("you need to enter correct number of questions between 1-10")
                quiz_questions = int(input("How many questions would you like to answer ? "))
        else:
            print(Welcoming.format(name=name, n=(quiz_questions)))
            play_quiz(name, questions)

    # Running the ready function, which asks if someone else wants to take the quiz. 
    # if yes the program will repeat the process for taking the quiz again. 
    # if no the results will be displayed and the program will end.
    # The system check for the next users as well their names and their input for the number of questions the want to answer 
   
    while competitor():
        name = input("What is your name? ").title()
        while len(name)== 0 or len(name)< 3 or name.isdigit(): 
            print("Enter correct name to proceed to the quiz")
            name=input()
        else:
            quiz_questions = int(input("How many questions would you like to answer ? "))
            while quiz_questions not in numbers:
                print("you need to enter correct number of questions between 1-10")
                quiz_questions = int(input("How many questions would you like to answer ? "))
            else:
                print(Welcoming.format(name=name, n=(quiz_questions)))  
                play_quiz(name,questions)
    print("The Quiz has end")

# Print each user name with the score.
print("Users Scores")
for key,value in myDict.items():
            print('Username:', key, ',','score:',value,"%")

# Find the user with the highest score.
find_max =max(myDict, key=myDict.get)
print("User with Maximum score is", find_max, "with score", myDict[find_max],"%")

# Find the average score. 
average= myDict.values()
average_score= sum(average)/len(average)
print("Average score=", int(average_score),"%")

