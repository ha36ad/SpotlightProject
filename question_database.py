'''
Question Database File
'''

class Question:
    def __init__(self, prompt, options, values):
        self.prompt = prompt
        self.options = options
        self.values = values

prompt = ["Have you felt chest pain in the past week?",
          "Have you experienced dizziness in the past week?",
          "Have you experienced shortness of breath in the past week?"]

options = ["Yes, on multiply occasions.", "Yes, sometimes.", "Yes, but rarely.", "No."]

values = [1, 0.75, 0.5, 0]

q1 = Question(prompt[0], options, values)
q2 = Question(prompt[1], options, values)
q3 = Question(prompt[2], options, values)
q4 = Question("Do you have any pre-existing conditions?", ["Yes", "No"], [1, 0])

question_list = [q1, q2, q3, q4]