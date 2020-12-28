import tkinter as tk
from tkinter import ttk
import question_database_tuples as qd

#constants
HEIGHT= 800
WIDTH = 800

root=tk.Tk()

#Click function
def onClick(answer):
    global answer_list
    global question
    global next_question

    answer_list.append(float(answer))
    if next_question < len(qd.question_list):
        #clear second frame so new options are generated
        for child in frame2.winfo_children():
            child.destroy()

        #Display next question
        question.config(text=qd.question_list[next_question].prompt)

        #Recreate options, next button, and progress bar showing progress
        create_options(next_question)
        create_next()
        next_question += 1
        show_progress(next_question/len(qd.question_list)*100)

    else:
        risk_score = (sum (answer_list) * 100) / len(qd.question_list)
        qd.risk_print(risk_score)

        # clear second frame so new options are generated
        for child in frame2.winfo_children():
            child.destroy()

        # Display next question
        question.config(text=qd.return_risk_text(risk_score))

        suggestion_text = tk.Label(frame2, font=("Gotham", 16), width=500, justify="center", wraplength=400,
                                 text=qd.return_risk_suggestion(risk_score))
        suggestion_text.pack()

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
index = tk.StringVar(value = "1")

#Next Button
def create_next():
    next_button=tk.Button(frame2, font = ("Gotham", 16), text="Next",command=lambda: onClick(index.get()))
    next_button.pack()

#Question
question= tk.Label(frame, font = ("Gotham", 16), width = 500,justify = "center", wraplength = 400, text = qd.question_list[0].prompt)
question.pack()

#Progress bar
def show_progress(number):
    progress_bar = tk.ttk.Progressbar(frame2, orient = tk.HORIZONTAL, length = 500, mode ='determinate', value = number)
    progress_bar.pack(pady=20,padx = 10)
    progress_text = tk.Label(frame2, font=("Gotham", 16), width=500, justify="center", wraplength=400,
                         text="Progress: " + str(next_question) + " out of " + str(len(qd.question_list)))
    progress_text.pack()


#Create options
def create_options(i):
    for text, option in qd.question_list[i].options:
        tk.Radiobutton(frame2, text = text ,font = ("Gotham",14),background = 'gray',padx = 10, pady = 10, variable = index, value = option).pack()

#Create the progres bar,  the first question's options, and the progress bar
create_options(0)
create_next()
show_progress(1/len(qd.question_list)*100)


root.mainloop()


