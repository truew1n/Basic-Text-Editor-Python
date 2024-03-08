from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Kinter Text Editor')
root.configure(background='#ff8c00')


def fileselection():
	global dir
	root.openfile = filedialog.askopenfilename(initialdir='C:/', title="Choose file", filetypes=(("TXT Files","*.txt"), ("HTML Files","*.html"), ("All Files","*.*")))
	dir = root.openfile
	if dir != '':
		with open(str(dir), 'r') as txtfile:
			t1.delete("1.0","end")
			t1.insert(END,txtfile.read())
			root.title(str(dir)+' - Kinter Text Editor')

def save():
	try:
		with open(str(dir), 'w') as txtfile:
			txtfile.write(t1.get("1.0","end"))
	except:
		save_as()

def clear():
	t1.delete("1.0","end")

def save_as():
	root.savefile = filedialog.asksaveasfilename(initialdir='C:/', title="Save file", filetypes = (("TXT Files","*.txt"), ("HTML Files","*.html"), ("All Files","*.*")))
	dir = root.savefile
	if dir != '':
		with open(str(dir), 'w') as txtfile:
			txtfile.write(t1.get("1.0","end"))
		

	
menu_frame = LabelFrame(root, background='#ff8c00', borderwidth=0) # , text="menu", borderwidth=2
menu_frame.grid(row=0, column=0 , sticky="W") # -sticky 
file_sel = Button(menu_frame, text="Choose File", command=fileselection)
file_sel.grid(row=0, column=0, sticky="WS")
save_file = Button(menu_frame, text="Save File", command=save)
save_file.grid(row=0, column=1, sticky="WS")
save_file_as = Button(menu_frame, text="Save File As", command=save_as)
save_file_as.grid(row=0, column=2, sticky="WS")
clear_file = Button(menu_frame, text="Clear File", command=clear)
clear_file.grid(row=0, column=3, sticky="WS")
t1 = Text(root, font=("Arial","14","bold"), width=80, height=40, bg='#2e293a', fg='#008000')
t1.grid(row=1,column=0)

root.mainloop()