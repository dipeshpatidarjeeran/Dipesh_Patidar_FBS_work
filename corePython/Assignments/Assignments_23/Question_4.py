# Quiz Game: Create an interactive quiz game with multiple-choice questions. Display
# questions one at a time and allow the user to select an answer. Provide feedback on
# whether the selected answer is correct or incorrect.
from tkinter import *

quiz_data = [
    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "Mumbai", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "Java", "PHP", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "Who is the father of Python?",
        "options": ["Guido van Rossum", "Dennis Ritchie", "James Gosling", "Ken Thompson"],
        "answer": "Guido van Rossum"
    }
]
que_no = 0
score = 0

def load_question():
    question_label.config(text=quiz_data[que_no]['question'])
    var.set(None)
    for i in range(4):
        options[i].config(text=quiz_data[que_no]["options"][i])

def next_question():
    global que_no, score
    selected = int(var.get())
    selected_option = quiz_data[que_no]["options"][selected]
    
    if selected_option == quiz_data[que_no]["answer"]:
        result_label.config(text="✅ Correct!", fg="green")
        score += 1
    else:
        result_label.config(text=f"❌ Incorrect! Correct: {quiz_data[que_no]['answer']}", fg="red")

    que_no += 1
    if que_no < len(quiz_data):
        window.after(1000, load_question)
        window.after(1000, lambda: result_label.config(text=""))
    else:
        window.after(1000, show_score)

def show_score():
    question_label.config(text="Quiz Completed!")
    for btn in options:
        btn.pack_forget()
    next_button.pack_forget()
    result_label.config(text=f"🎉 Your score: {score}/{len(quiz_data)}", fg="blue")

if __name__ == "__main__":
    window = Tk()
    window.title("Quiz Game")
    window.geometry("400x300")

    question_label = Label(window, text="", font=("Arial", 14), wraplength=350)
    question_label.pack(pady=20)

    var = StringVar()

    options = []
    for i in range(4):
        btn = Radiobutton(window, text="", variable=var, value=f"{i}", font=("Arial", 12))
        btn.pack(anchor="w", padx=20)
        options.append(btn)

    next_button = Button(window, text="Next",command=next_question)
    next_button.pack(pady=10)
    result_label = Label(window, text="", font=("Arial", 12))
    result_label.pack()

    load_question()

    window.mainloop()