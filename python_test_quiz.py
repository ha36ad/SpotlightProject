

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "Have you felt chest pain in the past week?\n(a) Yes\n(b) No\n",
     "Have you experienced dizziness in the past week?\n(a) Yes\n(b) No\n",
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "a"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1

     if score == 2:
          print("You are potentially at high risk. Please contact a medical professional immediately.")
     elif score == 1:
          print("You are potentially at risk. Please contact a medical professional in the near future.")
     else:
          print("You are not at risk. Contact a medical professional for a more reliable diagnosis.")

run_quiz(questions)