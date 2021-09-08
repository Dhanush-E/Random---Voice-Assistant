import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random

def main():
	root = tk.Tk()
	root.title('Guess Me')
	root.geometry('400x300')
	num = random.randint(1,10)
	global attempts

	attempts = 3
	def check_ans():
		global attempts
		attempts -= 1

		guess = int(num_entry.get()) 

		if num == guess:
			label_win = Label(root,text="--> You win Congrats!").pack()
			btn_check.pack_forget()
		elif attempts == 0:
			label_out = Label(root,text="--> You are out of attempts!").pack()
			btn_check.pack_forget()
		elif guess < num:
			label_big = Label(root,text="--> I am Bigger than your guess!"+f" {attempts} attempts are left").pack()

		elif guess > num:
			label_small = Label(root,text = "--> I am smaller than your guess! "+f" {attempts} attempts are left").pack()
		

	def quit():
		root.destroy()


	label = Label(root,text = "I am a number Between 1 to 10", fg = 'white',bg = 'teal')
	label.pack()

	num_entry = Entry(root, bd = 5, width = 40) 
	num_entry.pack()

	btn_check = Button(root,text = "Check",command = check_ans,bg = 'Black',activebackground='light blue',fg = 'white')
	btn_check.pack()

	btn_quit = Button(root,text = "Quit",command = quit,activebackground='light blue',bg = 'Black',fg = 'white')
	btn_quit.pack()

	label_at = Label(root,text = f'You have 3 attempts to guess me').pack()


	root.mainloop()
