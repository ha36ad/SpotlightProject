'''
New Python Quiz without explicit dictionary

'''

from question_database import question_list

rounding_decimal = 2

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
        print("\"" + answer + "\" is not a valid option. Please try again.\n")
        return get_answer(question)

def run_quiz(questions):
    print("Please enter the lowercase letter specified for each option")
    print("For example, if your chosen option is \"(a)\", please enter \"a\"\n")

    score = 0

    for question in questions:
        answer = get_answer(question)
        score += answer

    risk_score = (score * 100) / len(questions)

    print("Your risk score is " + str(round(risk_score,rounding_decimal)) + "%")

    if risk_score >= 90:
        print("You are at very high risk. Please contact a medical professional immediately.")
    elif 70 <= risk_score < 90:
        print("You are potentially at a high risk. Please contact a medical professional as soon as possible.")
    elif 25 <= risk_score < 70:
        print("You are potentially at risk. Please contact a medical professional in the near future.")
    else:
        print("You are not at risk. Contact a medical professional for a more reliable diagnosis.")

run_quiz(question_list)
