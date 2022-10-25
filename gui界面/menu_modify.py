import tkinter as tk
from tkinter import ttk
import Link_database


class About_frame(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        tk.Label(self, text='本作品由ZY制作').pack()
        tk.Label(self, text='关于作品：这是一个数据管理系统').pack()
        tk.Label(self, text='版本：v1.0(不代表最终版本)').pack()


class Add_frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.name = tk.StringVar()
        self.chinese = tk.StringVar()
        self.math = tk.StringVar()
        self.english = tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()

    def create_page(self):
        tk.Label(self, text='这是添加界面').grid(row=0, column=1)
        tk.Label(self, text='姓名').grid(row=1, column=1, padx=20, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=1, column=2)
        tk.Label(self, text='语文').grid(row=2, column=1, padx=20, pady=10)
        tk.Entry(self, textvariable=self.chinese).grid(row=2, column=2)
        tk.Label(self, text='数学').grid(row=3, column=1, padx=20, pady=10)
        tk.Entry(self, textvariable=self.math).grid(row=3, column=2)
        tk.Label(self, text='英语').grid(row=4, column=1, padx=20, pady=10)
        tk.Entry(self, textvariable=self.english).grid(row=4, column=2)
        tk.Button(self, text='添加', command=self.add_data).grid(row=5, column=1, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=6, column=2, pady=10, stick=tk.E)
        #tk.Button(self, text='刷新', command=self.add_data).grid(row=5, column=2, padx=10, pady=10, stick=tk.E)

    def add_data(self):
        name = self.name.get()
        chinese = int(self.chinese.get())
        math = int(self.math.get())
        english = int(self.english.get())
        if name in Count_data().name_list:
            self.status.set('姓名已存在，请重新输入')
        else:
            db = Link_database.Link_database().db
            cur = db.cursor()
            sql = 'insert into students_info values ("{}",{},{},{});'.format(name, chinese, math, english)
            cur.execute(sql)
            db.commit()
            cur.close()
            db.close()
            self.status.set('导入数据成功')


class Delect_frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.tiaojian = tk.StringVar()
        self.status = tk.StringVar()
        tk.Label(self, text='这是删除界面').grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self, text='通过姓名删除').grid(row=1, column=1, padx=10, pady=10)
        tk.Entry(self, textvariable=self.tiaojian).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self, text='确认删除', command=self.delect_by_name).grid(row=3, column=1, padx=10, pady=10)
        # tk.Label(self, text='通过序号删除').grid(row=1, column=1, padx=10, pady=10)
        # tk.Entry(self, textvariable=self.tiaojian).grid(row=2, column=1, padx=10, pady=10)
        # tk.Button(self, text='确认删除', command=self.delect_data).grid(row=3, column=1, padx=10, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=4, column=1, stick=tk.E, padx=10, pady=10)
        #tk.Button(self, text='刷新', command=self.delect_by_name).grid(row=3, column=2, padx=10, pady=10, stick=tk.E)

    def delect_by_name(self):
        name = self.tiaojian.get()
        if name in Count_data().name_list:
            db = Link_database.Link_database().db
            cur = db.cursor()
            sql = 'delete from students_info where name="{}";'.format(name)
            cur.execute(sql)
            db.commit()
            cur.close()
            db.close()
            self.status.set('成功删除')
        else:
            self.status.set('姓名不存在，请重新输入')


class Update_frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.name = tk.StringVar()
        self.new_name = tk.StringVar()
        self.chinese = tk.StringVar()
        self.math = tk.StringVar()
        self.english = tk.StringVar()
        self.stutas = y = tk.StringVar()
        tk.Label(self, text='这是修改界面').grid(row=0, column=0)
        tk.Label(self, text='输入要修改前的姓名').grid(row=1, column=1, pady=10, padx=10)
        tk.Entry(self, textvariable=self.name).grid(row=1, column=2)
        tk.Label(self, text='输入要修改后的姓名').grid(row=2, column=1, pady=10, padx=10)
        tk.Entry(self, textvariable=self.new_name).grid(row=2, column=2)
        tk.Label(self, text='输入要修改后的语文').grid(row=3, column=1, pady=10, padx=10)
        tk.Entry(self, textvariable=self.chinese).grid(row=3, column=2)
        tk.Label(self, text='输入要修改后的数学').grid(row=4, column=1, pady=10, padx=10)
        tk.Entry(self, textvariable=self.math).grid(row=4, column=2, pady=10, padx=10)
        tk.Label(self, text='输入要修改后的英语').grid(row=5, column=1)
        tk.Entry(self, textvariable=self.english).grid(row=5, column=2, pady=10, padx=10)
        tk.Button(self, text='确认修改', command=self.update).grid(row=6, column=1, pady=10, padx=10)
        tk.Label(self, textvariable=self.stutas).grid(row=7, column=1, pady=10, stick=tk.E)
        #tk.Button(self, text='刷新', command=self.update).grid(row=6, column=2, padx=10, pady=10, stick=tk.E)

    def update(self):
        new_name = self.new_name.get()
        name = self.name.get()
        chinese = self.chinese.get()
        math = self.math.get()
        english = self.english.get()
        if name in Count_data().name_list:
            db = Link_database.Link_database().db
            cur = db.cursor()
            sql = 'update students_info set name="{}",chinese="{}",math="{}",english="{}" where name="{}";'.format(
                new_name, chinese, math, english, name)
            cur.execute(sql)
            db.commit()
            cur.close()
            db.close()
            self.stutas.set('修改成功')
        else:
            self.stutas.set('姓名不存在，请重新输入')


class Select_frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        tk.Label(self, text='这是查询界面').pack()
        self.table_view = tk.Frame()
        self.table_view.pack()
        self.create_page()

    def create_page(self):
        columns = ('name', 'chinese', 'math', 'english')
        # columns_values = ('姓名', '语文', '数学', '英语')
        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)
        self.tree_view.column('name', width=100, anchor='center')
        self.tree_view.column('chinese', width=100, anchor='center')
        self.tree_view.column('math', width=100, anchor='center')
        self.tree_view.column('english', width=100, anchor='center')
        self.tree_view.heading('name', text='姓名')
        self.tree_view.heading('chinese', text='语文')
        self.tree_view.heading('math', text='数学')
        self.tree_view.heading('english', text='英语')
        self.tree_view.pack(fill=tk.BOTH, expand=True)
        self.show_data()
        tk.Button(self, text='刷新', command=self.show_data).pack(anchor=tk.E, pady=5)

    def show_data(self):
        # 不断更新节点
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        db = Link_database.Link_database().db
        cur = db.cursor()
        sql = 'select * from students_info;'
        cur.execute(sql)
        datas = cur.fetchall()
        index = 0
        for i in datas:
            self.tree_view.insert('', index + 1, values=i)
        db.commit()


class Count_data(Link_database.Link_database):
    def __init__(self):
        super().__init__()
        self.name_list = []
        sql = 'select * from students_info '
        self.cur.execute(sql)
        data = self.cur.fetchall()
        for i in data:
            i=list(i)
            self.name_list.append(i[0])
