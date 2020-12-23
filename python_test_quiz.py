class Question:
    def __init__(self, prompt, questions, options, answer_values):
        self.prompt = prompt
        self.questions = questions
        self.options = options
        self.answer_values = answer_values

prompt = ["Have you felt chest pain in the past week?",
          "Have you experienced dizziness in the past week?"]

questions = ["Yes, on multiply occasions", "Yes, sometimes", "Yes, but rarely", "No"]

options = ["a", "b", "c", "d"]

answer_values = ["1", "0.75", "0.5", "0"]

q1 = Question(prompt[0], questions, options, answer_values)
q2 = Question(prompt[1], questions, options, answer_values)

question_list = [q1, q2]




def get_answer(question):
    print(question.prompt)
    i = 0
    for question_option in questions:
        text = "(" + options[i] + ") " + question_option
        print(text)
        i += 1

    answer = input()
    try:
         option_index = options.index(answer)
         return answer_values[option_index]
    except:
         print("\"" + answer + "\" is an invalid option. Please try again")
         return try_q(question)



def run_quiz(questions):
    print("Please enter the lowercase letter specified for each option")
    print("For example, if your chosen option is \"(a)\", enter \"a\"\n")

    score = 0

    for question in questions:
        score += float(get_answer(question))

    risk_score = (score * 100) / len(questions)

    print("Your risk score is " + str(risk_score) + "%")

    if risk_score >= 75:
        print("You are potentially at high risk. Please contact a medical professional immediately.")
    elif 25 < risk_score < 75:
        print("You are potentially at risk. Please contact a medical professional in the near future.")
    else:
        print("You are not at risk. Contact a medical professional for a more reliable diagnosis.")


run_quiz(question_list)