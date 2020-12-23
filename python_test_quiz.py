"""
Name: William Wang

Python Test Quiz where each answer has specified weights
"""



class Question:
    def __init__(self, prompt, questions, inputs, answer_values):
        self.prompt = prompt
        self.options = options
        self.inputs = inputs
        self.answer_values = answer_values

prompt = ["Have you felt chest pain in the past week?",
          "Have you experienced dizziness in the past week?"]

options = ["Yes, on multiply occasions", "Yes, sometimes", "Yes, but rarely", "No"]

inputs = ["a", "b", "c", "d"]

answer_values = ["1", "0.75", "0.5", "0"]

q1 = Question(prompt[0], options, inputs, answer_values)
q2 = Question(prompt[1], options, inputs, answer_values)

question_list = [q1, q2]

def get_answer(question):
    print(question.prompt)
    i = 0
    for option in options:
        text = "(" + inputs[i] + ") " + option
        print(text)
        i += 1

    answer = input()

    try:
         input_index = inputs.index(answer)
         return answer_values[input_index]
    except:
         print("\"" + answer + "\" is an invalid option. Please try again")
         return get_answer(question)

def run_quiz(questions):
    print("Please enter the lowercase letter specified for each option")
    print("For example, if your chosen option is \"(a)\", please enter \"a\"\n")

    score = 0

    for question in questions:
        score += float(get_answer(question))

    risk_score = (score * 100) / len(questions)

    print("Your risk score is " + str(risk_score) + "%")


    if risk_score >= 90:
         print("You are at very high risk. Please contact a medical professional immediately.")
    elif 65 <= risk_score < 90:
         print("You are potentially at a high risk. Please contact a medical professional as soon as possible.")
    elif 25 <= risk_score < 65:
         print("You are potentially at risk. Please contact a medical professional in the near future.")
    else:
         print("You are not at risk. Contact a medical professional for a more reliable diagnosis.")


run_quiz(question_list)