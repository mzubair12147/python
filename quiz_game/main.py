def newGame():
    guesses = []
    correctGusses = 0
    questionNumber = 0

    for key in questions:
        print("_"*20)
        print(key)
        for i in options[questionNumber]:
            print(i)
        guess = ""
        while guess not in [ 'A' , 'B' , 'C' , 'D' ]:
            guess = input("Enter your choice (A / B / C / D): ").upper()
        guesses.append(guess)
        correctGusses += checkAnswer(questions.get(key), guess)
        questionNumber += 1    
    
    displayScore(correctGusses, guesses)

def checkAnswer(answer, guess):
    if answer == guess:
        print('Correct')
        return 1
    print('Wrong')
    return 0

def displayScore(correctGusses, guesses):
    print('*'*20)
    print('{:^20}'.format('RESULTS'))
    print('*'*20)
    print('Answers: ', end="")
    for question in questions:
        print(questions.get(question), ' ', end="")
    print()

    print('Gusses: ', end="")
    for guess in guesses:
        print(guess, ' ', end="")
    print()

    score  = (correctGusses/len(guesses))*100
    print("Your score is: {:.1f}%\n\n".format(score))
    

def playAgain():
    response = input("Wanna play again ( yes / no )?: ").upper()
    if response == 'YES':
        return True
    else:
        return False

questions = {
    "Who created python?: " : 'A',
    'What year was python created?: ': 'B',
    'Python is tributed to which comedy group?: ': 'C',
    'Is the earth round: ': 'A'
}

options = [
    ['A. Guido Van Rossam', 'B. Elon Musk', 'C. Bill Gates', 'D. Mark ZuckerBurg'],
    ['A. 1989', 'B. 1991', 'C. 2000', 'D. 2016'],
    ['A. Lonely Island', 'B. Smosh', 'C. Monty Python', 'D. SNL'], 
    ['A. True', 'B. False','C. Sometimes', "D. what's Earth? "]
]

newGame()

while playAgain():
    newGame()

print("The game is terminated!")