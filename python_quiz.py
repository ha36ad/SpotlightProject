'''
New Python Quiz without explicit dictionary

'''

class Question:
    def __init__(self, prompt, options, values):
        self.prompt = prompt
        self.options = options
        self.values = values


prompt = ["Have you felt chest pain in the past week?",
          "Have you experienced dizziness in the past week?",
          "Have you experienced shortness of breath in the past week?"]

options = ["Yes, on multiply occasions", "Yes, sometimes", "Yes, but rarely", "No"]

values = [1, 0.75, 0.5, 0]

q1 = Question(prompt[0], options, values)
q2 = Question(prompt[1], options, values)
q3 = Question(prompt[2], options, values)

question_list = [q1, q2, q3]

def get_answer(question):
    print(question.prompt)  # print question
    i = 0
    for option in question.options:
        text = "(" + str(i+1) + ") " + option
        print(text)
        i += 1

    try:
        answer = input()
        answer_index = int(answer) - 1
        #print (str(answer_index))
        #print(str(question.values[answer_index]))

        answer_value = question.values[answer_index]

        return answer_value

    except:
        print("\"" + answer + "\" is not a valid option. Please try again.")
        return get_answer(question)

def run_quiz(questions):
    print("Please enter the lowercase letter specified for each option")
    print("For example, if your chosen option is \"(a)\", please enter \"a\"\n")

    score = 0

    for question in questions:
        answer = get_answer(question)
        score += answer

    risk_score = (score * 100) / len(questions)

    print("Your risk score is " + str(round(risk_score,3)) + "%")

    if risk_score >= 90:
        print("You are at very high risk. Please contact a medical professional immediately.")
    elif 65 <= risk_score < 90:
        print("You are potentially at a high risk. Please contact a medical professional as soon as possible.")
    elif 25 <= risk_score < 65:
        print("You are potentially at risk. Please contact a medical professional in the near future.")
    else:
        print("You are not at risk. Contact a medical professional for a more reliable diagnosis.")

run_quiz(question_list)
