from tkinter import *

top = Tk()

top.geometry("800x650")

# creating label
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
e3 = Entry(top).place(x=30,y=490)
#
#
# # creating label
# Q6 = Label(top, text="Q6 What are your technical interests?").place(x=30, y=250)
#
# Q7 = Label(top, text="Q7 What are your hobbies?").place(x=30, y=290)
#
# # creating label
# Q8 = Label(top, text="Q8 How often do you sit relax and meditate?").place(x=30, y=330)
#
# Q9 = Label(top, text="Q9 How much time do you spend on social media?").place(x=30, y=370)
#
# # creating label
# Q10 = Label(top, text="Q10 Do you feel like you can lead a group of people?").place(x=30, y=410)
#
# Q11 = Label(top, text="Q11 When you speak to people you tend to:").place(x=30, y=450)
# # creating label
# Q12 = Label(top, text="Q12 What do you think? you can work best in team or you can work best alone?").place(x=30, y=490)
#
# Q13 = Label(top, text="Q13 Rate your communication skill feom 1 to 5?").place(x=30, y=530)
#
#
# Q14 = Label(top, text="Q14 Are you easily offended?").place(x=30, y=570)
#
#
# Q15 = Label(top, text="Q15 Are you Generally passionate about social causes?").place(x=30, y=610)



top.mainloop()