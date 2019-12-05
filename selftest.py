import random

def parse_file(questions_file, answers_file):
    questions = []
    answers = []
    questions_and_answers = []
    with open(questions_file) as f:
        for question in f:
            questions.append(question)
    with open(answers_file) as g:
        for answer in g:
            answers.append(answer)

    for i in range(0,len(questions)):
        entry = (questions[i], answers[i])
        questions_and_answers.append(entry)

    return questions_and_answers

def give_quiz(questions):
    while len(questions) > 0:
        pos = random.randint(0, len(questions)-1)
        q,a = questions[pos]    
        print(q)
        reply = input(" ")
        print(a)
        reply = input(" ")
        if reply == '1':
            questions.remove((q,a))
        else:
            continue

def main():
    questions = parse_file("./phil_questions.txt", "./phil_answers.txt")
    give_quiz(questions) 

main()