import tkinter as tk
from question_database_tuples import question_list

def risk(risk_score):
    print("Your risk score is " + str(round(risk_score, rounding_decimal)) + "%")

    if risk_score >= 90:
        print("You are at very high risk. Please contact a medical professional immediately.")
    elif 70 <= risk_score < 90:
        print("You are potentially at a high risk. Please contact a medical professional as soon as possible.")
    elif 25 <= risk_score < 70:
        print("You are potentially at risk. Please contact a medical professional in the near future.")
    else:
        print("You are not at risk. Contact a medical professional for a more reliable diagnosis.")

#constants
HEIGHT= 800
WIDTH = 800
rounding_decimal = 2

root=tk.Tk()

#Click function
def onClick(answer):
    global answer_list
    global question
    global next_question

    answer_list.append(float(answer))
    if next_question < len(question_list):
        #clear second frame so new options are generated
        for child in frame2.winfo_children():
            child.destroy()

        #Display next question
        question.config(text=question_list[next_question].prompt)

        #Recreate options and next button
        create_options(next_question)
        create_next()

        next_question += 1

    else:
        risk_score = (sum (answer_list) * 100) / len(question_list)

        risk(risk_score)

#Canvas
canvas=tk.Canvas(root,height = HEIGHT, width = WIDTH)
canvas.pack()

#Frame
frame = tk.Frame(root,bg ='gray')
frame2 = tk.Frame(frame,bg ='gray')
frame.place(relx = 0.1,rely = 0.1, relwidth = 0.8, relheight = 0.8)
frame2.place (relx = 0.1,rely = 0.1, relwidth = 0.8, relheight = 0.8)

#Intialization of variables
answer_list = []
next_question = 1

#Next Button
def create_next():
    next_button=tk.Button(frame2,text="Next",command=lambda: onClick(index.get()))
    next_button.pack()

#Question
question= tk.Label(frame, font = ("Gotham", 16), width = 500,justify = "center", wraplength = 400, text = question_list[0].prompt) 
question.pack()

#Buttons
index = tk.StringVar(value = "1")

def create_options(i):
    for text, option in question_list[i].options:
        tk.Radiobutton(frame2, text = text ,font = ("Gotham",14),background = 'gray',padx = 10, pady = 10, variable = index, value = option).pack()

    
create_options(0)
create_next()

root.mainloop()


