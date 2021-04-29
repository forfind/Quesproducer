from tkinter import *
from tkinter.simpledialog import *
import numpy as np
import tkinter.filedialog
import random
from PIL import ImageTk, Image

class OperationGenerator:
    '这是一个可以定值的计算题生成器'
    '账号：forfind 密码：123456'

    def __init__(self):
        self.num_of_qus = 20    # 题目数量，默认20
        self.max_num = 10       # 算式中出现的最大数,默认10
        self.flag_of_add = 1    # 加法标志，默认有
        self.flag_of_sub = 1    # 减法标志，默认有
        self.flag_of_mul = 0    # 乘法标志，默认无
        self.flag_of_div = 0    # 除法标志，默认无
        self.flag_of_prth = 0   # 括号标志，默认无
        self.flag_of_decm = 0   # 小数标志，默认无
        self.file_name = ''     # 文件路径
        return

    def login(self):
        global userName1, password1, errorNote
        key = userName1.get()
        value = password1.get()
        if key == 'forfind' and value == '123456':
            '消除登录页面'
            start.place_forget()
            userName.place_forget()
            userName1.place_forget()
            password.place_forget()
            password1.place_forget()
            confirm.place_forget()
            back.place_forget()
            errorNote.place_forget()

            '这里是显示定制化的页面'
            relx = 0.1
            rely = 0
            # 标题
            Label(root, text='练习题定制', bg='white', font=('仿宋', 20)).place(relx=0.35,rely=0.03,height=25, width=200)
            # 题目数量
            relx_of_num = relx
            rely_of_num = rely + 0.2
            lb_num = Label(root, text='题目数量', bg='white', font=('仿宋', 12))
            lb_num.place(relx=relx_of_num, rely=rely_of_num)
            inp_num = Entry(root)
            inp_num.focus()
            inp_num.place(relx=relx_of_num + 0.25, rely=rely_of_num, relwidth=0.18)

            # 最大数
            relx_of_max = relx
            rely_of_max = rely + 0.3
            lb_max = Label(root, text='题目难度', bg='white', font=('仿宋', 12))
            lb_max.place(relx=relx_of_max, rely=rely_of_max)
            maxvar = IntVar()

            max_10 = Radiobutton(root, text="10以内", bg='white', variable=maxvar, value=1, command=lambda: self.slec_max(10))
            max_10.place(relx=relx_of_max + 0.25, rely=rely_of_max)
            max_50 = Radiobutton(root, text="50以内", bg='white', variable=maxvar, value=2, command=lambda: self.slec_max(50))
            max_50.place(relx=relx_of_max + 0.35, rely=rely_of_max)
            max_100 = Radiobutton(root, text="100以内", bg='white', variable=maxvar, value=3, command=lambda: self.slec_max(100))
            max_100.place(relx=relx_of_max + 0.45, rely=rely_of_max)
            max_otr = Radiobutton(root, text="自定义:", bg='white', variable=maxvar, value=0, command=lambda: self.slec_max(0))
            max_otr.place(relx=relx_of_max + 0.57, rely=rely_of_max)

            inp_max = Entry(root)
            inp_max.place(relx=relx_of_max + 0.68, rely=rely_of_max, relwidth=0.1)

            lb_lim = Label(root, text='以内', bg='white')
            lb_lim.place(relx=relx_of_max + 0.78, rely=rely_of_max)

            # 选择运算符
            relx_of_opr = relx
            rely_of_opr = rely + 0.4

            lb_opr = Label(root, text='包含的运算符', bg='white', font=('仿宋', 12))
            lb_opr.place(relx=relx_of_opr, rely=rely_of_opr)

            addvar = IntVar()
            subvar = IntVar()
            mulvar = IntVar()
            divvar = IntVar()

            add = Checkbutton(root, text='＋', bg='white', font=16, variable=addvar, onvalue=1, offvalue=0)
            sub = Checkbutton(root, text='-', bg='white', font=22, variable=subvar, onvalue=1, offvalue=0)
            mul = Checkbutton(root, text='×', bg='white', font=16, variable=mulvar, onvalue=1, offvalue=0)
            div = Checkbutton(root, text='÷', bg='white', font=16, variable=divvar, onvalue=1, offvalue=0)

            add.place(relx=relx_of_opr + 0.25, rely=rely_of_opr + 0.02, relheight=0.03, relwidth=0.05)
            sub.place(relx=relx_of_opr + 0.35, rely=rely_of_opr + 0.02, relheight=0.03, relwidth=0.05)
            mul.place(relx=relx_of_opr + 0.45, rely=rely_of_opr + 0.02, relheight=0.03, relwidth=0.05)
            div.place(relx=relx_of_opr + 0.55, rely=rely_of_opr + 0.02, relheight=0.03, relwidth=0.05)

            # 括号
            relx_of_prth = relx
            rely_of_prth = rely + 0.5
            prthvar = IntVar()
            Label(root, text='是否包含括号', bg='white', font=('仿宋', 12)).place(relx=relx_of_prth, rely=rely_of_prth)
            prth_y = Radiobutton(root, text="是", bg='white', variable=prthvar, value=1, command=lambda: self.slec_prth(1))
            prth_y.place(relx=relx_of_prth + 0.25, rely=rely_of_prth + 0.02, relheight=0.03, relwidth=0.05)
            prth_n = Radiobutton(root, text="否", bg='white', variable=prthvar, value=0, command=lambda: self.slec_prth(0))
            prth_n.place(relx=relx_of_prth + 0.35, rely=rely_of_prth + 0.02, relheight=0.03, relwidth=0.05)

            # 小数
            relx_of_decm = relx
            rely_of_decm = rely + 0.6
            decmvar = IntVar()
            Label(root, text='是否包含小数', bg='white', font=('仿宋', 12)).place(relx=relx_of_decm, rely=rely_of_decm)
            decm_y = Radiobutton(root, text="是", bg='white', variable=decmvar, value=1, command=lambda: self.slec_decm(1))
            decm_y.place(relx=relx_of_decm + 0.25, rely=rely_of_decm + 0.02, relheight=0.03, relwidth=0.05)
            decm_n = Radiobutton(root, text="否", bg='white', variable=decmvar, value=0, command=lambda: self.slec_decm(0))
            decm_n.place(relx=relx_of_decm + 0.35, rely=rely_of_decm + 0.02, relheight=0.03, relwidth=0.05)

            # 生成题目
            relx_of_pdc = relx + 0.33
            rely_of_pdc = rely + 0.8
            '''self.max_num = inp_max.get()
            self.num_of_qus = inp_num.get()'''
            btn_pdc = Button(root, relief=GROOVE, text='生成题目', bg='white', font=('仿宋', 12), command=lambda: self.pdcqus(inp_num.get(),inp_max.get(),addvar.get(),subvar.get(),mulvar.get(),divvar.get()))
            btn_pdc.place(relx=relx_of_pdc, rely=rely_of_pdc)
        else:
            errorNote.config(text='账号或密码输入错误！')
            userName1.delete(0, END)
            password1.delete(0, END)
        return

    def slec_prth(self, x):
        self.flag_of_prth = x

    def slec_decm(self, x):
        self.flag_of_decm = x


    def slec_max(self, x):
        self.max_num = x



    def pdcqus(self,num_of_qus,max_num,add,sub,mul,div):
        self.num_of_qus = int(num_of_qus)

        if self.max_num == 0:
            self.max_num = int(max_num)

        self.flag_of_add = add
        self.flag_of_sub = sub
        self.flag_of_mul = mul
        self.flag_of_div = div

        self.printall()

        winNew = Toplevel(root)
        winNew['bg'] = 'white'
        winNew.geometry('600x200')
        winNew.title('生成题目')

        relx = 0.16
        rely = 0.15

        # 提示
        infostr = self.infostr()
        relx_of_info = relx
        rely_of_info = rely
        lb_info = Label(winNew,text=infostr, bg='white',font=('仿宋',12))
        lb_info.place(relx=relx_of_info,rely=rely_of_info)


        # 文件路径
        relx_of_file = relx
        rely_of_file = rely + 0.2
        lb_file = Label(winNew,text='选择文件：', bg='white', font=('仿宋', 12))
        lb_file.place(relx=relx_of_file,rely=rely_of_file)
        btnfile = Button(winNew, relief=GROOVE, text="浏览", bg='white', font=('仿宋', 12), command=lambda:self.file(lb_file))
        btnfile.place(relx=relx_of_file+0.6,rely=rely_of_file)

        # 文件保存提示
        relx_of_sav = relx
        rely_of_sav = rely + 0.4
        lb_sav = Label(winNew,text='', bg='white',font=('仿宋',12))
        lb_sav.place(relx=relx_of_sav,rely=rely_of_sav)

        # 确认、关闭按钮
        relx_of_sure = relx + 0.18
        rely_of_sure = rely + 0.6
        btnsure = Button(winNew, relief=GROOVE, text="确定", bg='white', font=('仿宋', 12), command=lambda:self.writeToFile(lb_sav))
        btnsure.place(relx=relx_of_sure,rely=rely_of_sure)
        btClose=Button(winNew, relief=GROOVE,text='关闭', bg='white', font=('仿宋', 12),command=winNew.destroy)
        btClose.place(relx=relx_of_sure+0.25,rely=rely_of_sure)



    def infostr(self):

        temp = "您将得到包含"
        flag = 0
        if self.flag_of_add == 1:
            flag = 1
            temp = "".join([temp,"加法"])
        if self.flag_of_sub == 1:
            if flag == 1:
                temp = "".join([temp,"、"])
            flag = 1
            temp = "".join([temp,"减法"])
        if self.flag_of_mul == 1:
            if flag == 1:
                temp = "".join([temp,"、"])
            flag = 1
            temp = "".join([temp,"乘法"])
        if self.flag_of_div == 1:
            if flag == 1:
                temp = "".join([temp,"、"])
            flag = 1
            temp = "".join([temp,"除法"])
        if self.flag_of_prth == 1:
            if flag == 1:
                temp = "".join([temp,"、"])
            flag = 1
            temp = "".join([temp,"括号"])
        if self.flag_of_decm == 1:
            if flag == 1:
                temp = "".join([temp,"、"])
            temp = "".join([temp,"小数"])
        temp = "".join([temp,"的" + str(self.max_num) + "以内的" + str(self.num_of_qus) + "道题!"])
        return temp



    def file(self, lb_file):
        self.file_name = tkinter.filedialog.askopenfilename()
        lb_file.config(text="文件路径：" + self.file_name)



    def generator(self):
        all_symbols = ["＋", "－", "×", "÷", "=", "\n"]
        symbols = []  # 符号库
        equation = [] # 算术表达式
        equations = ""
        if self.flag_of_add == 1:
            symbols.append("＋")
        if self.flag_of_sub == 1:
            symbols.append("－")
        if self.flag_of_mul == 1:
            symbols.append("×")
        if self.flag_of_div == 1:
            symbols.append("÷")
        # 生成算式
        i = 1
        while i <= self.num_of_qus:
            num_size = random.randint(2, 4) # 算式中包含2-4个数字
            for j in range(2 * num_size - 1):
                if j % 2 == 0:  # 生成数字
                    if(self.flag_of_decm == 0):  # 无小数
                        num = random.randint(1, self.max_num)
                    else:  # 有小数
                        if random.randint(0, 1) == 0:
                            num = random.randint(1, self.max_num)
                        else:
                            num = round(random.uniform(1, self.max_num), 1)
                    equation.append(str(num))
                else:  # 生成符号
                    equation.append(symbols[random.randint(0,len(symbols)-1)])
            if self.flag_of_prth == 1:  # 有括号
                if len(equation) >3:  # 只有两个数的运算就不加括号
                    if(random.randint(0,1) == 1):  # 0.5的可能性生成括号
                        symbol_idx = random.randint(0, len(equation)-1)
                        while equation[symbol_idx] not in symbols:
                            symbol_idx = random.randint(0, len(equation)-1)
                        equation.insert(symbol_idx-1, '(')
                        equation.insert(symbol_idx+3, ')')
            equation.append(" = \n")
            equations = equations + "".join(equation)
            equation.clear()
            i = i + 1
        return equations


    def writeToFile(self, lb_sav):
        with open(self.file_name, "w") as f:
            f.write(self.generator())
        lb_sav.config(text="保存成功！")


    def printall(self):
        print("num_of_qus=", self.num_of_qus,
              "max_num=", self.max_num,
              "flag_of_add", self.flag_of_add,
              "flag_of_sub", self.flag_of_sub,
              "flag_of_mul", self.flag_of_mul,
              "flag_of_div", self.flag_of_div,
              "flag_of_prth=", self.flag_of_prth,
              "flag_of_decm=", self.flag_of_decm,
              "file_name", self.file_name
              )


if __name__ == "__main__":
    OG = OperationGenerator()
    root = Tk()
    root["bg"] = "white"
    root.title("可定制的计算题生成器")
    root.geometry('600x400')

    #背景
    canvas = tkinter.Canvas(root,bd=0, width=800, height=400, highlightthickness=0)
    imgpath = 'bg.jpg'
    img = Image.open(imgpath)
    photo = ImageTk.PhotoImage(img)

    canvas.create_image(-340, 0,anchor=NW, image=photo)
    canvas.place(relx=0,rely=0)

    #canvas.create_window(100, 50, width=600, height=400)
    start = Label(root, text='登 录', bg="white", font=('仿宋', 30))
    start.place(relx=0.43, rely=0.15)
    userName = Label(root, text='账号：', bg='white', font=('仿宋', 12))
    userName.place(relx=0.35, rely=0.4)
    userName1 = Entry(root)
    userName1.focus()
    userName1.place(relx=0.43, rely=0.4)
    password = Label(root, text='密码：', bg='white', font=('仿宋', 12))
    password.place(relx=0.35, rely=0.49)
    password1 = Entry(root)
    password1.place(relx=0.43, rely=0.49)
    errorNote = Label(root, text='', bg='white', font=('仿宋', 12))
    errorNote.place(relx=0.7, rely=0.4)
    confirm = Button(root, relief=GROOVE, text='确认', bg='white', font=('仿宋', 12), command=OG.login)
    confirm.place(relx=0.43, rely=0.6)
    back = Button(root, relief=GROOVE, text='退出', bg='white', font=('仿宋', 12), command=root.destroy)
    back.place(relx=0.6, rely=0.6)

    root.mainloop()
