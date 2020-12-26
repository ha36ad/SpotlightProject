import tkinter as tk
import os
from question_database import question_list

#constants
HEIGHT= 800
WIDTH = 800
rounding_decimal = 2

#Questions class
class Question:
    def __init__(self, prompt, options):
        self.prompt = prompt
        self.options = options
        
prompt = ["Have you felt chest pain in the past week?",
          "Have you experienced dizziness in the past week?",
          "Have you experienced shortness of breath in the past week?"]

options = [
    ("Yes, on multiple occasions", "1"),
    ("Yes, sometimes", "0.75"),  
    ("Yes, but rarely", "0.5"),
    ("No","0"), 
    ]


#Questions
q1 = Question(prompt[0], options)
q2 = Question(prompt[1], options)
q3 = Question(prompt[2], options)
question_list = [q1, q2, q3]

root=tk.Tk()

#canvas
canvas=tk.Canvas(root,height=HEIGHT, width= WIDTH)
canvas.pack()

#frame
frame = tk.Frame(root,bg='gray')
frame.place(relx=0.1,rely=0.1, relwidth=0.8, relheight=0.8)

#Intialization of variables
answer_list = []
next_question = 1

#Click function
def onClick(answer):
    global answer_list
    global question
    global next_question

    answer_list.append(float(answer))
    if next_question < len(question_list):
        question.config(text=question_list[next_question].prompt)
        next_question += 1
    else:
        risk_score = (sum (answer_list) * 100) / len(question_list)

        print("Your risk score is " + str(round(risk_score,rounding_decimal)) + "%")

        if risk_score >= 90:
            print("You are at very high risk. Please contact a medical professional immediately.")
        elif 70 <= risk_score < 90:
            print("You are potentially at a high risk. Please contact a medical professional as soon as possible.")
        elif 25 <= risk_score < 70:
            print("You are potentially at risk. Please contact a medical professional in the near future.")
        else:
            print("You are not at risk. Contact a medical professional for a more reliable diagnosis.")
    


#Question
question= tk.Label(frame,text=question_list[0].prompt) 
question.pack()

#Buttons
index = tk.StringVar()
for text, option in options:
    tk.Radiobutton(frame, text=text, variable=index, value= option).pack()

#Next Button
next_button=tk.Button(frame,text="Next",command=lambda: onClick(index.get()))
next_button.pack()

root.mainloop()


