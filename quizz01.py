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

    def __init__(self, master):
        self.master = master
        self.master.title('Game Programme')
        self.master.geometry('800x620')
        self.frame = Frame(self.master)
        self.frame.grid()

        # self.menu = Menu(self.rt)
        # self.rt.config(menu=self.menu)
        # self.subm1 = Menu(self.menu)
        # self.menu.add_cascade(Label='Home')
        # self.subm1.add_command(Label='exit')

        self.labeltitle = Label(self.frame, text='QUIZZ COMPETITION PROGRAM', fg='blue', relief=RIDGE, bd=13,
                                font=('arial', 25, 'bold')) \
            .grid(column=0, row=0, padx=120, pady=20, )
        self.label1 = Label(self.frame, text='This is a quizz competition,\n that contains three courses. \n '
                                             'Please register if you do not have an account.', font=15, relief='groove',
                            bd=7) \
            .grid(column=0, row=1, padx=20, pady=30)

        self.loginframe1 = Frame(self.frame, width=600, height=300, bd=3, relief=RIDGE).grid(column=0, row=2, padx=0,
                                                                                             pady=50)
        self.label2 = Label(self.frame, text='For single candidate', bg='black', fg='white',
                            font=('arial', 13, 'bold'),
                            width=20, relief='solid'). \
            place(x=130, y=320)
        self.single_login = Button(self.frame, text='login', width=8,command=self.singlelogin, fg='white', bg='brown',
                                   font=('arial', 10, 'bold')). \
            place(x=380, y=320)
        self.label3 = Label(self.frame, text='For free trial', bg='black', fg='white',
                            font=('arial', 13, 'bold'),
                            width=20, relief='solid'). \
            place(x=130, y=420)
        self.free_trial_btn = Button(self.frame, text='Login', width=8, fg='white', bg='brown',
                                  font=('arial', 10, 'bold')). \
            place(x=380, y=420)
        self.label4 = Label(self.frame, text='For registration', bg='black', fg='white',
                            font=('arial', 13, 'bold'),
                            width=20, relief='solid'). \
            place(x=130, y=520)
        self.registration = Button(self.frame, text='signup',command=self.reg, width=8, fg='white', bg='red',
                                    font=('arial', 10, 'bold')). \
            place(x=380, y=520)

    def singlelogin(self):
        self.master.withdraw()
        self.newtab2 = Toplevel(self.master)
        self.app = SingleLogin(self.newtab2)

    def reg(self):
        self.master.withdraw()
        self.newtab = Toplevel(self.master)
        self.app = Signup(self.newtab)

class Signup:
    def __init__(self, signupwindow ):

        self.signupwindow = signupwindow
        self.signupwindow.geometry('400x400+0+0')

        # self.signupwindow = Toplevel(self.master)
        # self.signupwindow.geometry('800x620')
        # self.master.withdraw()
        #
        self.fullname1 = StringVar()
        self.password1 = StringVar()
        self.DOB1 = StringVar()
        self.country_list1 = StringVar()
        self.country_list = ['Nigeria', 'Ghana', 'South Africa', 'Cameroon', 'USA', 'UK', 'Sweden']

        self.label5 = Label(self.signupwindow, text='Signup to create an account', font=('arial', 12, 'bold')) \
            .place(x=50, y=12)
        self.fullname = Label(self.signupwindow, text='User Name', fg='blue', relief='solid', bd=3, width=13).place(x=20,
                                                                                                                      y=70)
        self.password = Label(self.signupwindow, text='Password', fg='blue', relief='solid', bd=3, width=13).place(x=20,
                                                                                                                    y=120)
        self.DOB = Label(self.signupwindow, text='Date of Birth', fg='blue', relief='solid', bd=3, width=13).place(x=20,
                                                                                                                   y=170)
        self.country = Label(self.signupwindow, text='Country', fg='blue', relief='solid', bd=3, width=13).place(x=20,
                                                                                                                 y=220)

        self.firstnameinput = Entry(self.signupwindow, width=22, textvar=self.fullname1, relief=SUNKEN, bd=6) \
            .place(x=150, y=70)
        self.lastnameinput = Entry(self.signupwindow, width=22, textvar=self.password1, relief=SUNKEN, bd=6) \
            .place(x=150, y=120)
        self.DOBinput = Entry(self.signupwindow, width=22, textvar=self.DOB1, relief=SUNKEN, bd=6) \
            .place(x=150, y=170)
        self.countryinput = OptionMenu(self.signupwindow, self.country_list1, *self.country_list)
        self.country_list1.set('select country')
        self.countryinput.config(width=13)
        self.countryinput.place(x=150, y=215)
        self.signup_done = Button(self.signupwindow, text='Done', fg='blue',command=self.done_signup, bd=8,
                                     relief=GROOVE,
                                     font=('arial', 12, 'bold')).place(x=70, y=270)
        self.exit_signup = Button(self.signupwindow, text='exit', fg='blue',command=self.exit_signup, bd=8, width=7, relief=GROOVE,
                                  font=('arial', 12, 'bold')).place(x=180, y=270)

    def done_signup(self):
        self.newtab1 = Toplevel(self.signupwindow)
        self.app = HomePage(self.newtab1)
        self.signupwindow.withdraw()
        self.signup_done_msgbox = msgbox.showinfo('Signup', 'You have successfully \n signed up')



    def exit_signup(self):

        self.newtab = Toplevel(self.signupwindow)
        self.app = HomePage(self.newtab)
        self.signupwindow.withdraw()


class SingleLogin:

    def __init__(self, loginwindow):
        self.loginwindow = loginwindow
        self.loginwindow.geometry('350x350')
        self.username1 = StringVar()
        self.password1 = StringVar()
                     
        self.label = Label(self.loginwindow, text='Kindly input your Username\n and Password', font=('arial', 12, 'bold')) \
            .place(x=50, y=12)
        self.username = Label(self.loginwindow, text='User Name', fg='blue', relief='solid', bd=3, width=13).place(x=30, y=80)
        self.password = Label(self.loginwindow, text='Password', fg='blue', relief='solid', bd=3, width=13).place(x=30,y=170)
        self.usernameinput = Entry(self.loginwindow, width=22, textvar=self.username1, relief=SUNKEN, bd=6) \
            .place(x=150, y=80)
        self.passwordinput = Entry(self.loginwindow, width=22, textvar=self.password1, relief=SUNKEN, bd=6) \
            .place(x=150, y=170)

        self.done_login = Button(self.loginwindow, text='Done', fg='blue', bd=8,relief=GROOVE,font=('arial', 12, 'bold'))\
            .place(x=60, y=270)
        self.back_btn = Button(self.loginwindow, text='exit', fg='blue',command=self.exit,  bd=8, width=7, relief=GROOVE,
                                  font=('arial', 12, 'bold')).place(x=180, y=270)


    def exit(self):
        self.newtab = Toplevel(self.loginwindow)
        self.app = HomePage(self.newtab)
        self.loginwindow.withdraw()


if __name__ == '__main__':
        main()
