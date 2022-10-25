import tkinter as tk
from Link_database import Link_database
import Goin_page
import check_user_info
from tkinter import messagebox

class Made_user(Link_database):
    def __init__(self, mater):
        super().__init__()
        self.root = mater
        self.root.resizable(0, 0)
        self.root.geometry('700x400+500+300')
        self.root.title('Madeuser')
        #self.root.iconbitmap('/sdcard/pycode/gui界面/1.ico')
        self.user_name = tk.StringVar()
        self.password = tk.StringVar()
        self.page = tk.Frame(self.root)
        self.page.pack()

        tk.Label(self.page).grid(row=0, column=0)
        tk.Label(self.page, text='账号').grid(row=1, column=1, padx=20, pady=10)
        tk.Entry(self.page, textvariable=self.user_name).grid(row=1, column=2)
        tk.Label(self.page).grid(row=2)
        tk.Label(self.page, text='密码').grid(row=3, column=1, padx=20, pady=10)
        tk.Entry(self.page, textvariable=self.password, show='*').grid(row=3, column=2)
        tk.Label(self.page).grid(row=4)
        tk.Button(self.page, text='注册',command=self.made_info).grid(row=5, column=1, padx=10, pady=10)
        tk.Button(self.page, text='返回登入',command=self.reback).grid(row=5, column=2, padx=10, pady=10)
        #tk.Button(self.page, text='退出', command=self.page.quit).grid(row=5, column=3, padx=10, pady=10)

    def made_info(self):
        name = self.user_name.get()
        password = self.password.get()
        data1 =check_user_info.Check_info().user_name_list
        data2=check_user_info.Check_info().user_psd_list
        if name:
            if name not in data1:
                if password:
                    sql='insert into user_info values ("{}","{}");'.format(name,password)
                    self.cur.execute(sql)
                    self.commit()
                    messagebox.showinfo(title='提示',message='注册成功')
                else:
                    messagebox.showwarning(title='警告',message='密码不能为空')
            else:
                messagebox.showwarning(title='警告',message='用户名已存在，请重新注册')
        else:
            messagebox.showwarning(title='警告',message='用户名不能为空')



    def reback(self):
        self.page.destroy()
        Goin_page.Goin_page(self.root)


if __name__ == '__main__':
    master = tk.Tk()
    made_user = Made_user(master)
    master.mainloop()
