from tkinter import *
import tkinter as tk
import random

def main():

	global target
	target = random.randint(1,30)
	global balls
	balls = 12
	global score
	score = 0

	def btn_next():
		global target
		global balls
		global score
		run  = int(run_entry.get())
		balls = balls - 1
		score = score + run

		if score>target and balls<=12:
			label_win = Label(root,text='Congrats! You won the Game')
			label_win.pack()
			next_but.pack_forget()

		elif score<target and balls == 0:
			label_loss = Label(root,text = 'You lost the game')
			label_loss.pack()
			next_but.pack_forget()

		elif score==target and balls == 0:
			label_tie = Label(root,text = 'The Game is tie')
			label_tie.pack()
			next_but.pack_forget()


	def quit():
		root.destroy()

	root = Tk()
	root.title('Numcrick')
	root.geometry('400x300')

	label = Label(root,text = f'Traget is {target} runs in {balls} balls',bg = 'teal')
	label.pack(fill=tk.X)

	label_en = Label(root,text = 'Hit your Runs below between 1 to 6: ',font=('halvatecia',15,'bold')).pack()
	run_entry = Entry(root,bd = 5, width = 40)
	run_entry.pack()

	next_but = Button(root,text='Next Ball',fg = 'white',bg = 'black',command = btn_next)
	next_but.pack()

	quit_but = Button(root,text = 'Quit',fg = 'white',bg = 'black',command = quit)
	quit_but.pack()
	root.mainloop()
