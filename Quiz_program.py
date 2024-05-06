quiz = {
    "question1": {
        "question": "What is the capital of Andhra Pradesh?",
        "answer": "Amaravati"
    },
    "question2": {
        "question": "What is the capital of Tamilnadu?",
        "answer": "Chennai"
    },
    "question3": {
        "question": "What is the capital of Kerala?",
        "answer": "Thiruvananthapuram"
    },
    "question4": {
        "question": "What is the capital of Karnataka?",
        "answer": "Bengaluru"
    },"question5": {
        "question": "What is the capital of Maharastra?",
        "answer": "Mumbai"
    },"question6": {
        "question": "What is the capital of Bihar?",
        "answer": "Patna"
    },"question7": {
        "question": "What is the capital of Madhya Pradesh?",
        "answer": "Bhopal"
    },
}

score = 0

for key, value in quiz.items():
    print(value[ 'question' ])
    answer = input("Answer? ")

    if answer.lower() == value[ 'answer'] . lower():
        print('Correct')
        score = score + 1
        print("Your score is: " + str(score))
        print("")
        print("")
    else:
        print("Wrong!")
        print("The answer is : " + value['answer'])
        print("Your score is: " + str(score))
        print("")
        print("")

print("You got " + str(score) + " out of 7 questions correctly")
print("Your percentage is " + str(int(score/7 * 100)) + "%")