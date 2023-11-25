from tkinter import *
from tkinter import messagebox

value = ''


class Calci:

    def __init__(self):
        self.root = Tk()
        self.root.title('Calculator')
        self.root.config(background='black')
        self.root.protocol('WM_DELETE_WINDOW', self.on_close)
        self.root.wm_iconbitmap('cal.ico')

        self.root.geometry('300x280')
        self.root.resizable(False, False)

        self.root_ent = IntVar()
        self.Entry = Entry(textvariable=self.root_ent, width=11, font=('Terminal', 25))
        self.Entry.grid(row=0, columnspan=5, padx=15, pady=15)

        self.percent = Button(text='⇦', height=1, width=4, bg='black', fg='white', borderwidth=0, font=('Terminal', 16),
                              command=self.del_one)
        self.percent.grid(row=1, column=0, padx=8, pady=5)

        self.left = Button(text='(', height=1, width=4, bg='black', fg='white', borderwidth=0, font=('Terminal', 16),
                           command=lambda: self.add_value('('))
        self.left.grid(row=1, column=1, padx=8)

        self.right = Button(text=')', height=1, width=4, bg='black', fg='white', borderwidth=0, font=('Terminal', 16),
                            command=lambda: self.add_value(')'))
        self.right.grid(row=1, column=2, padx=8)

        self.back = Button(text='×', height=1, width=6, bg='black', fg='white', borderwidth=0,
                           font=('Terminal', 16, 'bold'),
                           command=lambda: self.add_value('*'))
        self.back.grid(row=1, column=3, padx=8)

        self.num_9 = Button(text='9', height=1, width=4, bg='black', fg='white', borderwidth=0, font=('Terminal', 16),
                            command=lambda: self.add_value('9'))
        self.num_9.grid(row=2, column=2, padx=8, pady=5)

        self.num_8 = Button(text='8', height=1, width=4, bg='black', fg='white', borderwidth=0, font=('Terminal', 16),
                            command=lambda: self.add_value('8'))
        self.num_8.grid(row=2, column=1, padx=8, pady=5)

        self.num_7 = Button(text='7', height=1, width=4, bg='black', fg='white', borderwidth=0, font=('Terminal', 16),
                            command=lambda: self.add_value('7'))
        self.num_7.grid(row=2, column=0, padx=8, pady=5)

        self.num_6 = Button(text='6', height=1, width=4, bg='black', fg='white', borderwidth=0, font=('Terminal', 16),
                            command=lambda: self.add_value('6'))
        self.num_6.grid(row=3, column=2, padx=8, pady=5)

        self.num_5 = Button(text='5', height=1, width=4, bg='black', fg='white', borderwidth=0, font=('Terminal', 16),
                            command=lambda: self.add_value('5'))
        self.num_5.grid(row=3, column=1, padx=8, pady=5)

        self.num_4 = Button(text='4', height=1, width=4, bg='black', fg='white', borderwidth=0, font=('Terminal', 16),
                            command=lambda: self.add_value('4'))
        self.num_4.grid(row=3, column=0, padx=8, pady=5)

        self.num_3 = Button(text='3', height=1, width=4, bg='black', fg='white', borderwidth=0, font=('Terminal', 16),
                            command=lambda: self.add_value('3'))
        self.num_3.grid(row=4, column=2, padx=8, pady=5)

        self.num_2 = Button(text='2', height=1, width=4, bg='black', fg='white', borderwidth=0, font=('Terminal', 16),
                            command=lambda: self.add_value('2'))
        self.num_2.grid(row=4, column=1, padx=8, pady=5)

        self.num_1 = Button(text='1', height=1, width=4, bg='black', fg='white', borderwidth=0, font=('Terminal', 16),
                            command=lambda: self.add_value('1'))
        self.num_1.grid(row=4, column=0, padx=8, pady=5)

        self.point = Button(text='.', height=1, width=4, bg='black', fg='white', borderwidth=0, font=('Terminal', 16),
                            anchor='n',
                            command=lambda: self.add_value('.'))
        self.point.grid(row=5, column=0, padx=8, pady=5)

        self.zero = Button(text='0', height=1, width=4, bg='black', fg='white', borderwidth=0, font=('terminal', 16),
                           command=lambda: self.add_value('0'))
        self.zero.grid(row=5, column=1)

        self.CE = Button(text='CE', height=1, width=4, bg='black', fg='white', borderwidth=0, font=('terminal', 16),
                         command=self.del_all)
        self.CE.grid(row=5, column=2)

        self.div = Button(text='÷', height=1, width=6, bg='black', fg='white', borderwidth=0,
                          font=('terminal', 16, 'bold'),
                          command=lambda: self.add_value('/'))
        self.div.grid(row=2, column=3)

        self.sub = Button(text='-', height=1, width=6, bg='black', fg='white', borderwidth=0,
                          font=('terminal', 16, 'bold'),
                          command=lambda: self.add_value('-'))
        self.sub.grid(row=3, column=3)

        self.plus = Button(text='+', height=1, width=6, bg='black', fg='white', borderwidth=0,
                           font=('terminal', 16, 'bold'),
                           command=lambda: self.add_value('+'))
        self.plus.grid(row=4, column=3)

        self.eql = Button(text='=', height=1, width=6, bg='black', fg='white', borderwidth=0,
                          font=('terminal', 16, 'bold'), command=self.Evaluate)
        self.eql.grid(row=5, column=3)

        self.root.mainloop()

    def add_value(self, Value):
        global value
        value += str(Value)
        self.Entry.delete(0, END)
        self.Entry.insert(1, value)

    def Evaluate(self):
        global value
        try:
            value = str(eval(value))
            self.Entry.delete(0, END)
            self.Entry.insert(0, value)
        except:
            self.del_all()
            messagebox.showerror('Error', 'Sorry Please Try Again')

    def del_all(self):
        global value
        value = ''
        self.Entry.delete(0, END)

    def del_one(self):
        global value
        new_value = self.Entry.get()
        if new_value:
            self.Entry.delete(len(new_value) - 1)
            value = new_value[:-1]

    def on_close(self):
        if messagebox.askyesno('Confirmation', 'Do You Want To Close The Application?'):
            self.root.destroy()


Calci()
