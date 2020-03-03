from Question import Question

#An array of question prompts
questions_prompt = [
    "What color are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are Strasberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
    "What color are Cherry?\n(a) Black\n(b) Yellow\n(c) Red\n\n",
]

#Creating an array of questions. Start creating question objects inside it.
questions = [
    Question(questions_prompt[0], "a"),
    Question(questions_prompt[1], "c"),
    Question(questions_prompt[2], "b"),
    Question(questions_prompt[3], "c"),
]

def run_test(questions): #The parameter questions is the list of question objects that we want to ask the user.
    score = 0
    for question in questions: #For each question object inside of this questions array, I want to do something.
        answer = input(question.prompt) #ask the question to the user and store it in answer (objects)
        if answer == question.answer: #check if they have got it right, (objects)
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)