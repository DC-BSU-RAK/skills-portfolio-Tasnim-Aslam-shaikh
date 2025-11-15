import tkinter as tk
import random

# ---------------------- REQUIRED FUNCTIONS ----------------------

def displayMenu():
    """Display the difficulty selection menu."""
    clear_window()

    title = tk.Label(root, text="DIFFICULTY LEVEL", font=("Arial", 18))
    title.pack(pady=15)

    tk.Button(root, text="1. Easy", width=20, command=lambda: start_quiz(1)).pack(pady=5)
    tk.Button(root, text="2. Moderate", width=20, command=lambda: start_quiz(2)).pack(pady=5)
    tk.Button(root, text="3. Advanced", width=20, command=lambda: start_quiz(3)).pack(pady=5)


def randomInt(level):
    """Return a random number based on the difficulty level."""
    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(1000, 9999)


def decideOperation():
    """Randomly decide between + and -."""
    return random.choice(["+", "-"])


def displayProblem():
    """Show the math problem to the user."""
    clear_window()

    global answer_entry, submit_btn, feedback_label

    # Display question number
    tk.Label(root, text=f"Question {current_question} of 10", font=("Arial", 14)).pack(pady=5)

    # Show the problem
    tk.Label(root, text=f"{num1} {operation} {num2} =", font=("Arial", 26)).pack(pady=15)

    # Recreate Entry each time
    answer_entry = tk.Entry(root, font=("Arial", 18), justify="center")
    answer_entry.pack(pady=10)

    # Recreate submit button
    submit_btn = tk.Button(root, text="Submit Answer", font=("Arial", 14), command=submit_answer)
    submit_btn.pack(pady=10)

    # Recreate feedback label
    feedback_label = tk.Label(root, font=("Arial", 12), fg="red")
    feedback_label.pack(pady=5)


def isCorrect(user_answer):
    """Check if user's answer is correct."""
    global score, attempt, current_question

    try:
        user_answer = int(user_answer)
    except:
        feedback_label.config(text="Please enter a valid number.")
        return

    # Calculate correct result
    correct = num1 + num2 if operation == "+" else num1 - num2

    if user_answer == correct:
        score += 10 if attempt == 1 else 5
        next_question()
    else:
        if attempt == 1:
            attempt = 2
            feedback_label.config(text="Incorrect! Try again.")
        else:
            feedback_label.config(text=f"Incorrect. Correct answer: {correct}")
            next_question()


def displayResults():
    """Show final results and grade."""
    clear_window()

    grade = (
        "A+" if score >= 90 else
        "A"  if score >= 80 else
        "B"  if score >= 70 else
        "C"  if score >= 60 else
        "D"  if score >= 50 else
        "F"
    )

    result_label = tk.Label(root, text=f"Quiz Complete!\nScore: {score}/100\nGrade: {grade}",
                            font=("Arial", 18))
    result_label.pack(pady=20)

    tk.Button(root, text="Play Again", width=15, command=displayMenu).pack(pady=5)
    tk.Button(root, text="Exit", width=15, command=root.quit).pack(pady=5)

# ---------------------- QUIZ LOGIC ----------------------

def start_quiz(level):
    """Initialize quiz settings and begin."""
    global difficulty, score, current_question
    difficulty = level
    score = 0
    current_question = 1
    next_question()


def next_question():
    """Generate a new math problem, or finish if complete."""
    global num1, num2, operation, attempt, current_question

    if current_question > 10:
        displayResults()
        return

    num1 = randomInt(difficulty)
    num2 = randomInt(difficulty)
    operation = decideOperation()

    # Prevent negative answers for easy/moderate levels
    if operation == "-" and num1 < num2:
        num1, num2 = num2, num1

    attempt = 1
    displayProblem()
    current_question += 1


def clear_window():
    """Remove all widgets from the window."""
    for widget in root.winfo_children():
        widget.destroy()


def submit_answer():
    value = answer_entry.get()
    answer_entry.delete(0, tk.END)
    isCorrect(value)

# ---------------------- GUI SETUP ----------------------

root = tk.Tk()
root.title("Maths Quiz")
root.geometry("450x350")
root.resizable(False, False)

# Start at menu
displayMenu()

root.mainloop()