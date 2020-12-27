'''
Question Database File
'''
#Constants
rounding_decimal = 2

class Question:
    def __init__(self, prompt, options):
        self.prompt = prompt
        self.options = options

prompt = ["Have you felt chest pain in the past week?",
          "Have you experienced dizziness in the past week?",
          "Have you experienced shortness of breath in the past week?",
          "Do you have any pre-existing conditions?"]

options = [("Yes, on multiple occasions.", "1"), 
            ("Yes, sometimes.", "0.75"),
            ("Yes, but rarely.","0.5"),
            ("No","0")]

two_options = [("Yes","1"),( "No", "0")]

q1 = Question(prompt[0], options)
q2 = Question(prompt[1], options)
q3 = Question(prompt[2], options)
q4 = Question(prompt[3], two_options)

#Calculate risk score
def risk_print(risk_score):
    print("Your risk score is " + str(round(risk_score, rounding_decimal)) + "%")

    if risk_score >= 90:
        print("You are at very high risk. Please contact a medical professional immediately.")
    elif 70 <= risk_score < 90:
        print("You are potentially at a high risk. Please contact a medical professional as soon as possible.")
    elif 50 <= risk_score < 70:
        print("You are potentially at moderate risk. "
              "Please contact a medical professional as soon as it is convenient.")
    elif 25 <= risk_score < 50:
        print("You are potentially at risk. Please contact a medical professional in the near future.")
    else:
        print("You are not at risk. Contact a medical professional for a more reliable diagnosis.")
        
question_list = [q1, q2, q3, q4]

