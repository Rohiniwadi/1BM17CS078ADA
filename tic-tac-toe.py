from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("TIC_TAC_TOE")

flag=0
bclick=True
def disableButton():
    b1.configure(state=DISABLED)
    b2.configure(state=DISABLED)
    b3.configure(state=DISABLED)
    b4.configure(state=DISABLED)
    b5.configure(state=DISABLED)
    b6.configure(state=DISABLED)
    b7.configure(state=DISABLED)
    b8.configure(state=DISABLED)
    b9.configure(state=DISABLED)
    
def btnclk(buttons):
    global flag,bclick
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick=False
        check()
        flag+=1
    elif buttons['text']==" " and bclick==False:
        buttons['text']='O'
        bclick=True
        check()
        flag+=1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def check():
    if (b1['text']=='X'and b2['text']=='X' and b3['text']=='X'or
        b1['text']=='X'and b5['text']=='X' and b9['text']=='X' or
        b1['text']=='X'and b4['text']=='X' and b7['text']=='X' or
        b2['text']=='X'and b5['text']=='X' and b8['text']=='X' or
        b3['text']=='X'and b6['text']=='X' and b9['text']=='X' or
        b3['text']=='X'and b5['text']=='X' and b7['text']=='X' or
        b4['text']=='X'and b5['text']=='X' and b6['text']=='X' or
        b7['text']=='X'and b8['text']=='X' and b9['text']=='X' ):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", 'Player 1 Won!')
    elif([b1['text']=='X'and b2['text']=='X' and b3['text']=='X'] or
        [b1['text']=='X'and b5['text']=='X' and b9['text']=='X'] or
        [b1['text']=='X'and b4['text']=='X' and b7['text']=='X'] or
        [b2['text']=='X'and b5['text']=='X' and b8['text']=='X'] or
        [b3['text']=='X'and b6['text']=='X' and b9['text']=='X'] or
        [b3['text']=='X'and b5['text']=='X' and b7['text']=='X'] or
        [b4['text']=='X'and b5['text']=='X' and b6['text']=='X'] or
        [b7['text']=='X'and b8['text']=='X' and b9['text']=='X'] ):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", 'Player 1 Won!')
    elif (flag==8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "it's a TIE")
        

buttons = StringVar()
l1=Label(root,text='Player 1: X').grid(row=0,column=1)
l2=Label(root,text='Player 2: O').grid(row=0,column=3)

b1=Button(root,text=' ',font='Times 20 bold',bg='GREY',fg='WHITE',height=3,width=5,command=lambda: btnclk(b1))
b1.grid(row=1,column=1)
b2=Button(root,text=' ',font='Times 20 bold',bg='GREY',fg='WHITE',height=3,width=5,command=lambda:btnclk(b2))
b2.grid(row=1,column=2)
b3=Button(root,text=' ',font='Times 20 bold',bg='GREY',fg='WHITE',height=3,width=5,command=lambda:btnclk(b3))
b3.grid(row=1,column=3)
b4=Button(root,text=' ',font='Times 20 bold',bg='GREY',fg='WHITE',height=3,width=5,command=lambda:btnclk(b4))
b4.grid(row=2,column=1)
b5=Button(root,text=' ',font='Times 20 bold',bg='GREY',fg='WHITE',height=3,width=5,command=lambda:btnclk(b5))
b5.grid(row=2,column=2)
b6=Button(root,text=' ',font='Times 20 bold',bg='GREY',fg='WHITE',height=3,width=5,command=lambda:btnclk(b6))
b6.grid(row=2,column=3)
b7=Button(root,text=' ',font='Times 20 bold',bg='GREY',fg='WHITE',height=3,width=5,command=lambda:btnclk(b7))
b7.grid(row=3,column=1)
b8=Button(root,text=' ',font='Times 20 bold',bg='GREY',fg='WHITE',height=3,width=5,command=lambda:btnclk(b8))
b8.grid(row=3,column=2)
b9=Button(root,text=' ',font='Times 20 bold',bg='GREY',fg='WHITE',height=3,width=5,command=lambda:btnclk(b9))
b9.grid(row=3,column=3)

root.mainloop()
