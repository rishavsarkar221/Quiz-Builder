# ANCHOR: A quiz builder app. You can add as many questions as u want and same for options.

quiz = []

is_valid = True

while True:
    question = input("\nEnter Question?\nType !break to end all: ")

    if question.lower() != "!break":
        quiz.append({})

        quiz[len(quiz) - 1]['Question'] = question
        
        while True:
            option = input("Enter Options. Type !break to end it: ")

            if option.lower() == "!break":
                break
            else:
                if 'options' not in quiz[len(quiz) - 1]:
                    quiz[len(quiz) - 1]['options'] = []
                    quiz[len(quiz) - 1]['options'].append(option.upper())
                else:
                    quiz[len(quiz) - 1]['options'].append(option.upper())
        
        correct_option = input("Enter Correct Option: ").upper()

        if correct_option.upper() in quiz[len(quiz) - 1]['options']:
            quiz[len(quiz) - 1]['correct'] = correct_option.upper()
        else:
            is_valid = False
            print("It is not there")
            break

        try:
            how_much_points = int(input("How many points you want to assign to this question? "))
            quiz[len(quiz) - 1]['points'] = how_much_points
        except ValueError:
            print("Enter only Integer Numbers")
            is_valid = False
            break
    
    else:
        break

if is_valid:
    total_points = 0

    for x in quiz:
        total_points += x['points']

    points = 0

    for i in range(len(quiz)):
        print(f"Question {i+1}) {quiz[i]['Question']}")
        
        for j in range(len(quiz[i]['options'])):
            print(f"    Option {j+1}) {quiz[i]['options'][j]}")
        
        correct_answer = input("Enter your Answer: ")

        if correct_answer.upper() == quiz[i]['correct']:
            print(f"Correct Answer!!!\nPoints Added: {str(quiz[i]['points'])}")
            points += quiz[i]['points']
        else:
            print("Wrong Answer!!!")
            break

    if points == total_points: print(f"\nYOU WON!!!!!\nYou got {str(points)}/{str(total_points)}")
    else: print(f"\nYOU LOST!!!!\nYou got {str(points)}/{str(total_points)}")
else:
    print("You did something wrong when making quiz. Run the Program again")