import tkinter as tk
from main import drowsy_detect

def add():
	result = 'a'
	result_label.configure(text = result)

window = tk.Tk()
window.title('Drowsiness Detector')
window.geometry('1024x768')
window.configure(background='white')

header_label = tk.Label(window, text='Drowsiness Detector')
header_label.pack()

result_label = tk.Label(window)
result_label.pack()
#check = tk.Button(window, text='Starting detection', command=add)

check = tk.Button(window, text='Starting detection', command=drowsy_detect)

check.pack()
#drowsy_detect()

window.mainloop()
