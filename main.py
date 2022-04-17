from tkinter import *

top = Tk()

top.geometry("800x650")


Q1 = Label(top, text="Q1 Please select your gender.").place(x=30, y=50)
R1 = Radiobutton(top, text="Male").place(x=30,y=80)
R1 = Radiobutton(top, text="female").place(x=30,y=120)
R1 = Radiobutton(top, text="don't want to specify").place(x=30,y=160)

Q2 = Label(top, text="Q2 What is your highest education?").place(x=30, y=200)
e1 = Entry(top).place(x=30,y=230)

Q3 = Label(top, text="Q3 Do you like meeting new people?").place(x=30, y=270)
e2 = Entry(top).place(x=30,y=320)

Q4 = Label(top, text="Q4 How often do you meet your friends?").place(x=30, y=360)
e3 = Entry(top).place(x=30,y=410)

Q5 = Label(top, text="Q5 what is your long term & short-term goals?").place(x=30, y=450)
e4 = Entry(top).place(x=30,y=490)

Q6 = Label(top, text="Q6 What are your technical interests?").place(x=30, y=530)
e5 = Entry(top).place(x=30,y=570)


def fun():
    tops = Tk()
    tops.geometry("800x650")
    Q7 = Label(tops, text="Q7 What are your hobbies?").place(x=30, y=50)
    e6 = Entry(tops).place(x=30,y=80)

    Q8 = Label(tops, text="Q8 How often do you sit relax and meditate?").place(x=30, y=120)
    e7 = Entry(tops).place(x=30, y=160)

    Q9 = Label(tops, text="Q9 How much time do you spend on social media?").place(x=30, y=200)
    e8 = Entry(tops).place(x=30, y=230)

    Q10 = Label(tops, text="Q10 Do you feel like you can lead a group of people?").place(x=30, y=270)
    e9 = Entry(tops).place(x=30, y=310)

    Q11 = Label(tops, text="Q11 When you speak to people you tend to:").place(x=30, y=360)
    Q11a = Label(tops, text="     a) Stand with arms folded?").place(x=30, y=380)
    e11ea = Entry(tops).place(x=50, y=410)

    Q11b = Label(tops, text="     b) Stand with hands in your pocket?").place(x=30, y=450)
    e11eb = Entry(tops).place(x=50, y=470)

    Q11c = Label(tops, text="     c) Stand while adjusting you hair?").place(x=30, y=510)
    e11ec = Entry(tops).place(x=50, y=530)

    def funinner():
        innertops = Tk()
        innertops.geometry("800x650")
        Q12 = Label(innertops, text="Q12 What do you think? you can work best in team or you can work best alone?").place(x=30, y=50)
        e12 = Entry(innertops).place(x=30, y=80)

        Q13 = Label(innertops, text="Q13 Rate your communication skill feom 1 to 5?").place(x=30, y=120)
        e13 = Entry(innertops).place(x=30, y=160)

        Q14 = Label(innertops, text="Q14 Are you easily offended?").place(x=30, y=200)
        e14 = Entry(innertops).place(x=30, y=230)

        Q15 = Label(innertops, text="Q15 Are you Generally passionate about social causes?").place(x=30, y=270)
        e15 = Entry(innertops).place(x=30, y=310)

        def showresults():
            intops = Tk()
            intops.geometry("800x650")

        b2 = Button(innertops, text="Show Result", command=showresults).place(x=30, y=400)



    b2 = Button(tops, text="Next Question", command=funinner).place(x=30, y=580)




b1 = Button(top, text="Next Question", command=fun).place(x=30,y=610)


top.mainloop()