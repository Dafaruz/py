import tkinter as tk

root = tk.Tk()

# יצירת Frame והוספתו לחלון הראשי
frame = tk.Frame(root)
frame.pack()

# יצירת כפתורים והוספתם ל-Frame
button1 = tk.Button(frame, text="Button 1")
button2 = tk.Button(frame, text="Button 2")
button3 = tk.Button(frame, text="Button 3")

button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.LEFT)

root.mainloop()



