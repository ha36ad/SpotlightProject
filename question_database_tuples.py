'''
Question Database File
'''

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
            ("No","0"),]
two_options = [("Yes","1"),( "No", "0")]

q1 = Question(prompt[0], options)
q2 = Question(prompt[1], options)
q3 = Question(prompt[2], options)
q4 = Question(prompt[3], two_options)

question_list = [q1, q2, q3, q4]
