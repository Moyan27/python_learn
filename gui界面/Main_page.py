import tkinter as tk
from menu_modify import About_frame,Add_frame,Select_frame,Delect_frame,Update_frame

class Main_page(object):
    def __init__(self,master):
        self.root = master
        self.root.resizable(0,0)
        self.root.geometry('900x600+400+180')
        self.root.title('Mainpage')
        #self.root.iconbitmap('/sdcard/pycode/gui界面/1.ico')
        self.create_menu_page()

    def create_menu_page(self):
        menubar=tk.Menu(self.root)
        menubar.add_command(label='添加',command=self.add_data)
        self.add_frame=Add_frame(self.root)
        menubar.add_command(label='查询',command=self.select_data)
        self.select_frame = Select_frame(self.root)
        menubar.add_command(label='删除',command=self.delect_data)
        self.delect_frame = Delect_frame(self.root)
        menubar.add_command(label='修改',command=self.update_data)
        self.update_frame = Update_frame(self.root)
        menubar.add_command(label='关于',command=self.show_about)
        self.about_frame = About_frame(self.root)
        self.root['menu']= menubar

    def show_about(self):
        self.about_frame.pack()
        self.update_frame.pack_forget()
        self.add_frame.pack_forget()
        self.delect_frame.pack_forget()
        self.select_frame.pack_forget()
    def update_data(self):
        self.update_frame.pack()
        self.add_frame.pack_forget()
        self.delect_frame.pack_forget()
        self.select_frame.pack_forget()

    def delect_data(self):
        self.about_frame.pack_forget()
        self.update_frame.pack_forget()
        self.add_frame.pack_forget()
        self.delect_frame.pack()
        self.select_frame.pack_forget()

    def select_data(self):
        self.about_frame.pack_forget()
        self.update_frame.pack_forget()
        self.add_frame.pack_forget()
        self.delect_frame.pack_forget()
        self.select_frame.pack()

    def add_data(self):
        self.about_frame.pack_forget()
        self.update_frame.pack_forget()
        self.add_frame.pack()
        self.delect_frame.pack_forget()
        self.select_frame.pack_forget()








if __name__ == '__main__':
    root = tk.Tk()
    myqq =Main_page(root)
    root.mainloop()
