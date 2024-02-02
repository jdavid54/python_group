
import tkinter as tk 
from time import strftime


# Function to update the time 
def update_time():
	string = strftime('%H:%M:%S %p') 
	time_label.config(text=string) 
	time_label.after(1000, update_time)

# Create the main window 
window = tk.Tk() 
window.title("Digital Clock")

# Create a label to display the time 
time_label = tk.Label(window,font=('calibri', 20, 'bold'),
background='black', foreground='white')
time_label.pack(anchor='center')

# Call the update_time function to display the time initially
update_time()

window.mainloop()