from tkinter import *
from PIL import ImageTk


def check():
    your_name=yourentry.get()
    part_name=partentry.get()
    x=your_name.lower().replace(' ','')
    y=part_name.lower().replace(' ','')

    for i in x:
        for i in y:
            x=x.replace(i,'')
            y=y.replace(i,'')
    count=len(x)+len(y)

    result=count%6
    if result==0:
        msg="You two are good friends!!!"
    elif result==1:
        msg="You two are good lovers!!!"
    elif result==2:
        msg="It's just an affection!!!"
    elif result==3:
        msg="You will end up in marriage <3"
    elif result==4:
        msg="So sad....You two are enemies!!!"
    elif result==5:
        msg="You two are sisters/brothers!!!"
    else:
        pass

    res_entry.insert(result,msg)


def clear():
    yourentry.delete(0,END)
    partentry.delete(0,END)
    res_entry.delete(0,END)

love=Tk()
love.resizable(0,0)
love.title("Love Meter <3!!!")

bgImage=ImageTk.PhotoImage(file='heart.jpg')
canvas=Canvas(love,width=1357,height=750)
canvas.pack(fill='both',expand=True)
canvas.create_image(0, 0, image=bgImage, anchor="nw")
canvas.create_text(670,25,text="LOVE METER",fill='#A53927',
                font=('Source Sans Pro',35,'bold'))
canvas.create_text(660,80,text="check your compatibility with your partner",fill='#A53927',
                font=('Source Sans Pro',20,'bold'))
'''
image1=ImageTk.PhotoImage(file='')
image1label=Label(love,image=image1)
image1label.place(x=640,y=40)
'''

#frame
frame=Frame(love,width=50,height=20,bg='#A53927')
frame.place(x=850,y=250)


#your name
your_name=Label(frame,text='Enter your name:',font=('Source Sans Pro',12,'bold'),bg='#A53927',fg='white')
your_name.grid(row=0,column=0,sticky='w',pady=(10,0),padx=25)
yourentry=Entry(frame,width=37,font=('Source Sans Pro',12,'bold'),bg='white',fg='#A53927')
yourentry.grid(row=1,column=0,padx=(25,25),pady=5)

#partner_name
part_name=Label(frame,text="Enter your partner's name:",font=('Source Sans Pro',12,'bold'),bg='#A53927',fg='white')
part_name.grid(row=2,column=0,sticky='w',pady=(10,0),padx=25)
partentry=Entry(frame,width=37,font=('Source Sans Pro',12,'bold'),bg='white',fg='#A53927')
partentry.grid(row=3,column=0,padx=(25,25),pady=5)

#submit
sub_button=Button(frame,text='SUBMIT',font=('Source Sans Pro',12,'bold'),bd=0,bg='#F64067',
                 fg='white',activebackground='#F64067',activeforeground='white',cursor='hand2',
                 command=check)
sub_button.grid(row=4,column=0,padx=25,pady=10)

#result
result=Label(frame,text="Status of your relationship",font=('Source Sans Pro',12,'bold'),bg='#A53927',fg='white')
result.grid(row=5,column=0,sticky='w',pady=(10,0),padx=25)
res_entry=Entry(frame,width=37,font=('Source Sans Pro',12,'bold'),bg='white',fg='#A53927')
res_entry.grid(row=6,column=0,padx=(25,25),pady=5)

#clear
clear_button=Button(frame,text='CLEAR',font=('Source Sans Pro',12,'bold'),bd=0,bg='#F64067',
                 fg='white',activebackground='#F64067',activeforeground='white',cursor='hand2',
                 command=clear)
clear_button.grid(row=7,column=0,padx=25,pady=10)



love.mainloop()




    
