from tkinter import *
from requests import *

root=Tk()
root.title("Motivational quotes")
root.geometry("1000x500+100+100")
f=("Arial",40,"bold")

def save():
	try:
		wa="http://api.quotable.io/random"
		res=get(wa)
		data=res.json()
		info=data["content"]
		lab.configure(text=info)
	except Exception as e:
		lab.configure(text="issue"+str(e))


btn=Button(root,text="Get msg",font=f,command=save)
btn.pack()
lab=Label(root,font=f,wraplength=700)
lab.pack()

root.mainloop()
