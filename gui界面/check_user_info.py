from Link_database import Link_database
from tkinter import messagebox


class Check_info(Link_database):
    def __init__(self):
        super().__init__()
        self.user_name_list = []
        self.user_psd_list = []
        sql = 'select * from user_info;'
        self.cur.execute(sql)
        datas = self.cur.fetchall()
        for i in datas:
            self.user_name_list.append(list(i)[0])
            self.user_psd_list.append(list(i)[1])
        self.commit()

    def check_info(self, name, password):
        if name:
            if name in self.user_name_list:
                index = self.user_name_list.index(name)
                if password == self.user_psd_list[index]:
                    return True, '登入成功'
                else:
                    return False, '密码错误，请重新输入'
            else:
                return False, '用户名不存在，您可以先注册'
        else:
            return False,'用户名不能为空'


if __name__ == '__main__':
    check = Check_info()
