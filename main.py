from tkinter import *

top = Tk()

top.geometry("850x650")


Q1 = Label(top, text="Q1 Please select your gender.").place(x=30, y=50)
R1 = Radiobutton(top, text="Male").place(x=30,y=80)
R1 = Radiobutton(top, text="female").place(x=30,y=120)
R1 = Radiobutton(top, text="don't want to specify").place(x=30,y=160)

Q2 = Label(top, text="Q2 What is your highest education?").place(x=30, y=200)
e1 = Entry(top).place(x=30,y=230)

Q3 = Label(top, text="Q3 what is your long term & short-term goals?").place(x=30, y=270)
e2 = Entry(top).place(x=30,y=320)

Q4 = Label(top, text="Q4 what are your Hobbies?").place(x=30, y=360)
e3 = Entry(top).place(x=30,y=410)

Q5 = Label(top, text="Q5 What are your technical interests?").place(x=30, y=450)
R1 = Radiobutton(top, text="java").place(x=30,y=500)
R1 = Radiobutton(top, text="python").place(x=140,y=500)
R1 = Radiobutton(top, text="C++").place(x=30,y=550)
R1 = Radiobutton(top, text="javaScript").place(x=140,y=550)





def fun():
    tops = Tk()
    tops.geometry("850x650")
    Q7 = Label(tops, text="Q6 Do you feel like you can lead a group of people?").place(x=30, y=50)
    R1 = Radiobutton(tops, text="yes").place(x=30, y=80)
    R1 = Radiobutton(tops, text="no").place(x=140, y=80)

    Q8 = Label(tops, text="Q7 Define Accomplisments and volunteer work?").place(x=30, y=120)
    e7 = Entry(tops).place(x=30, y=160)

    Q9 = Label(tops, text="Q8 Define any 4 co-curricular?").place(x=30, y=200)
    e8 = Entry(tops).place(x=30, y=230)
    e9 = Entry(tops).place(x=30, y=270)
    e10 = Entry(tops).place(x=30, y=310)
    e11 = Entry(tops).place(x=30, y=350)

    Q10 = Label(tops, text="Q9 On Which social media platforms you are active").place(x=30, y=410)
    R1 = Radiobutton(tops, text="Facebook").place(x=30, y=460)
    R12 = Radiobutton(tops, text="Snapchat").place(x=140, y=460)
    R13 = Radiobutton(tops, text="Whatsapp").place(x=30, y=500)
    R14 = Radiobutton(tops, text="Twitter").place(x=140, y=500)

    def funinner():
        innertops = Tk()
        innertops.geometry("850x650")
        Q5 = Label(innertops, text="Q10 In which skill you are good?").place(x=30, y=50)
        R1 = Radiobutton(innertops, text="Problem Solving Skills").place(x=30, y=80)
        R1 = Radiobutton(innertops, text="Flexibility").place(x=200, y=80)
        R1 = Radiobutton(innertops, text="communication Skills").place(x=30, y=120)
        R1 = Radiobutton(innertops, text="Teamwork").place(x=200, y=120)



        def showresult():
            intops = Tk()
            intops.geometry("850x650")

        b2 = Button(innertops, text="Show Result", command=showresult).place(x=30, y=250)

    b2 = Button(tops, text="Next Question", command=funinner).place(x=30, y=560)













b1 = Button(top, text="Next Question", command=fun).place(x=30,y=610)


top.mainloop()