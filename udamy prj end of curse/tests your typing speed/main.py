import tkinter as tk
import random
import time

# Sample sentences for typing test
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "I love coding and building new projects.",
    "Tkinter makes it easy to create desktop applications.",
    "Artificial intelligence is revolutionizing the world."
]


# Function to start the typing test
def start_test():
    global start_time
    text_input.delete(1.0, tk.END)
    text_input.config(state="normal")
    label_result.config(text="")
    start_time = time.time()


# Function to calculate typing speed and accuracy
def end_test():
    global start_time
    end_time = time.time()

    # Get the user input and calculate time taken
    typed_text = text_input.get(1.0, tk.END).strip()
    time_taken = end_time - start_time

    # Calculate words per minute
    word_count = len(typed_text.split())
    wpm = round(word_count / (time_taken / 60))

    # Calculate accuracy
    original_text = label_sentence["text"]
    correct_chars = sum(1 for i, c in enumerate(typed_text) if i < len(original_text) and c == original_text[i])
    accuracy = round(correct_chars / len(original_text) * 100, 2)

    # Display results
    label_result.config(text=f"Time: {round(time_taken, 2)}s | WPM: {wpm} | Accuracy: {accuracy}%")
    text_input.config(state="disabled")


# Initialize main window
root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("600x400")

# Choose a random sentence
sentence = random.choice(sentences)

# Instruction label
label_instruction = tk.Label(root, text="Type the following sentence as fast and accurately as you can:",
                             font=("Helvetica", 14))
label_instruction.pack(pady=10)

# Sentence label
label_sentence = tk.Label(root, text=sentence, font=("Helvetica", 16), wraplength=500)
label_sentence.pack(pady=10)

# Text input box for typing
text_input = tk.Text(root, height=5, width=60, font=("Helvetica", 14), wrap=tk.WORD)
text_input.pack(pady=10)

# Button to start the test
button_start = tk.Button(root, text="Start", command=start_test, font=("Helvetica", 12), bg="green", fg="white")
button_start.pack(pady=5)

# Button to end the test
button_end = tk.Button(root, text="End Test", command=end_test, font=("Helvetica", 12), bg="red", fg="white")
button_end.pack(pady=5)

# Label to display the results
label_result = tk.Label(root, text="", font=("Helvetica", 14))
label_result.pack(pady=10)

# Start the main loop
root.mainloop()
