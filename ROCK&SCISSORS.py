import random
import tkinter as tk
def get_computer_choice():
    """Randomly selects and returns the computer's choice."""
    return random.choice(["Rock", "Paper", "Scissors"])
def determine_winner(user_choice, computer_choice):
    """Determines the winner based on choices made by the user and computer."""
    if user_choice == computer_choice:
        return "It's a tie! Try again."
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "🎉 You win this round!"
    else:
        return "😞 Computer wins this round. Try again!"
def play_round(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    user_choice_label.config(text=f"🧑 Your Choice: {user_choice}")
    computer_choice_label.config(text=f"💻 Computer's Choice: {computer_choice}")
    result_label.config(text=result)
    if "win" in result:
        user_score += 1
    elif "Computer wins" in result:
        computer_score += 1
    score_label.config(text=f"🏆 Score - You: {user_score} | Computer: {computer_score}")
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="🧑 Your Choice: ")
    computer_choice_label.config(text="💻 Computer's Choice: ")
    result_label.config(text="🔄 Ready to play?")
    score_label.config(text="🏆 Score - You: 0 | Computer: 0")
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("420x500")
root.resizable(False, False)
root.config(bg="#B3E5FC") 
user_score = 0
computer_score = 0
title_label = tk.Label(root, text="✊ Rock - 📄 Paper - ✂ Scissors", font=("Arial", 16, "bold"), bg="#B3E5FC")
title_label.pack(pady=10)
user_choice_label = tk.Label(root, text="🧑 Your Choice: ", font=("Arial", 12), bg="#B3E5FC")
user_choice_label.pack()
computer_choice_label = tk.Label(root, text="💻 Computer's Choice: ", font=("Arial", 12), bg="#B3E5FC")
computer_choice_label.pack()
result_label = tk.Label(root, text="🔄 Ready to play?", font=("Arial", 14, "bold"), bg="#B3E5FC")
result_label.pack(pady=10)
score_label = tk.Label(root, text="🏆 Score - You: 0 | Computer: 0", font=("Arial", 12), bg="#B3E5FC")
score_label.pack(pady=10)
button_frame = tk.Frame(root, bg="#B3E5FC")
button_frame.pack(pady=20)
rock_button = tk.Button(button_frame, text="✊ Rock", font=("Arial", 12), width=10, bg="#FFCCBC", command=lambda: play_round("Rock"))
rock_button.grid(row=0, column=0, padx=5)
paper_button = tk.Button(button_frame, text="📄 Paper", font=("Arial", 12), width=10, bg="#C8E6C9", command=lambda: play_round("Paper"))
paper_button.grid(row=0, column=1, padx=5)
scissors_button = tk.Button(button_frame, text="✂ Scissors", font=("Arial", 12), width=10, bg="#D1C4E9", command=lambda: play_round("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)
reset_button = tk.Button(root, text="🔄 Reset Game", font=("Arial", 12), bg="#FFEB3B", command=reset_game)
reset_button.pack(pady=20)
root.mainloop()