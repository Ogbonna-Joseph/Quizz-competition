from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msgbox


def exit(name):
    name.destroy()


def main():
    root = Tk()
    app = HomePage(root)
    root.mainloop()

class HomePage:
    def __init__(self,master):
        self.master = master
        self.master.title('Quizz Competition Program')
        self.master.geometry('800x620')
        self.frame = Frame(self.master)
        self.frame.grid()


        # self.menu = Menu(self.rt)
        # self.rt.config(menu=self.menu)
        # self.subm1 = Menu(self.menu)
        # self.menu.add_cascade(Label='Home')
        # self.subm1.add_command(Label='exit')

        self.labeltitle = Label(self.frame, text='QUIZZ COMPETITION PROGRAM',fg='blue',relief=RIDGE,bd=13, font=('arial', 25, 'bold'))\
            .grid(column=0, row=0, padx=120, pady=20, )
        self.label1 = Label(self.frame, text='This is a quizz competition,\n that contains three courses. \n '
                                             'Please register if you do not have an account.', font=15, relief='groove',bd=7 )\
            .grid(column=0, row=1, padx=20,pady=30 )


        self.loginframe1 = Frame(self.frame, width=600, height=300, bd=3, relief=RIDGE).grid(column=0, row=2, padx=0, pady=50)
        self.label2 = Label(self.loginframe1, text='For single candidate',bg='black',fg='white', font=('arial',13, 'bold'),
                            width=20,relief='solid').\
            place(x=130, y=320)
        self.single_login = Button(self.loginframe1, text='login', width=8, fg='white', bg='brown', font=('arial',10, 'bold')).\
            place(x=380, y=320)
        self.label3 = Label(self.loginframe1, text='For multiple candidates', bg='black', fg='white',
                            font=('arial', 13, 'bold'),
                            width=20, relief='solid'). \
            place(x=130, y=420)
        self.multi_login = Button(self.loginframe1, text='login', width=8, fg='white', bg='brown',
                              font=('arial', 10, 'bold')). \
            place(x=380, y=420)
        self.label4 = Label(self.loginframe1, text='For registration', bg='black', fg='white',
                            font=('arial', 13, 'bold'),
                            width=20, relief='solid'). \
            place(x=130, y=520)
        self.registration = Button(self.loginframe1, text='signup', width=8, fg='white', bg='red',
                              command=self.signup,font=('arial', 10, 'bold')). \
            place(x=380, y=520)


    def signup(self):

        self.signupwindow = Toplevel(self.master)
        self.signupwindow.geometry('800x620')
        self.master.withdraw()


        self.firstname1 = StringVar()
        self.lastname1 = StringVar()
        self.DOB1 = StringVar()
        self.country_list1 = StringVar()
        self.country_list = ['Nigeria','Ghana','South Africa', 'Cameroon','USA','UK','Sweden']

        self.label5 = Label(self.signupwindow, text='Signup to create an account', font=('arial',12,'bold'))\
            .place(x=50, y=12)
        self.firstname = Label(self.signupwindow, text='First Name',fg='blue', relief='solid', bd=3, width=13).place(x=20, y=70)
        self.lastname = Label(self.signupwindow, text='Last Name',fg='blue', relief='solid', bd=3, width=13).place(x=20, y=120)
        self.DOB = Label(self.signupwindow, text='Date of Birth',fg='blue', relief='solid', bd=3, width=13).place(x=20, y=170)
        self.country = Label(self.signupwindow, text='Country',fg='blue', relief='solid', bd=3, width=13).place(x=20, y=220)


        self.firstnameinput = Entry(self.signupwindow, width=22, textvar=self.firstname1, relief=SUNKEN,bd=6)\
            .place(x=150, y=70)
        self.lastnameinput = Entry(self.signupwindow, width=22, textvar=self.lastname1, relief=SUNKEN, bd=6) \
            .place(x=150, y=120)
        self.DOBinput = Entry(self.signupwindow, width=22, textvar=self.DOB1, relief=SUNKEN, bd=6) \
            .place(x=150, y=170)
        self.countryinput = OptionMenu(self.signupwindow, self.country_list1, *self.country_list)
        self.country_list1.set('select country')
        self.countryinput.config(width=13)
        self.countryinput.place(x=150, y=215)
        self.continuesignup = Button(self.signupwindow, text='continue',fg='blue',bd=8,command=self.continue_signup, relief=GROOVE,
                                     font=('arial',12,'bold')).place(x=70, y=270)
        self.exit_signup = Button(self.signupwindow, text='exit', fg='blue', bd=8,width=7, relief=GROOVE,
                                     font=('arial', 12, 'bold'), command=self.signup_exit).place(x=180, y=270)




    def signup_exit(self):
        self.signupwindow.destroy()
        self.master.deiconify()



    def continue_signup(self):
        self.account_detail = Toplevel(self.master)
        self.account_detail.geometry('260x260')

        self.username1 = StringVar()
        self.password1 = StringVar()
        self.confirm_password1 = StringVar()

        self.label_accnt = Label(self.account_detail, text='Please enter the username and \n password of your choice',
                                 font=('arial', 10, 'bold'), fg='blue').place(x=25, y=5)
        self.username = Label(self.account_detail, text='Username', fg='blue', relief='solid', bd=3, width=15).place(
            x=10, y=70)
        self.password = Label(self.account_detail, text='Password', fg='blue', relief='solid', bd=3, width=15).place(
            x=10, y=120)
        self.confirm_password = Label(self.account_detail, text='Confirm Password', fg='blue', relief='solid', bd=3, width=15).place(
            x=10, y=170)

        self.input_username = Entry(self.account_detail, textvar=self.username1, width=16, relief=SUNKEN, bd=5).place(x=140, y=70)
        self.input_password = Entry(self.account_detail, textvar=self.password1, width=16, relief=SUNKEN, bd=5).place(x=140, y=120)
        self.input_confirm_password = Entry(self.account_detail, textvar=self.confirm_password1, width=16, relief=SUNKEN, bd=5)\
            .place(x=140, y=170)

        self.signup_done_botton = Button(self.account_detail, text='DONE', relief=RIDGE,command=self.signup_done,
                                         bd=3, fg='white', bg='blue').place(x=50, y=210)
        self.exit_accnt_detail = Button(self.account_detail, text='EXIT',command=self.account_detail.destroy,
                                        relief=RIDGE, bd=3, fg='white', bg='blue').place(x=130, y=210)


    def signup_done(self):

        self.signupwindow.destroy()
        self.account_detail.destroy()
        self.master.deiconify()

        self.msgbox = msgbox.showinfo('Signup Info', 'You have successfully signed up ')

    # def exit(self,):
    #     if name == self.signupwindow or self.account_detail:
    #         self.name.destry()
    #     else:
    #         self.msgbox1 = msgbox.showerror('error', 'Invalid window name')








if __name__ == '__main__':
    main()
