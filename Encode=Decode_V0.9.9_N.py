import re
import tkinter as tk

root = tk.Tk()
root.geometry("300x190")
root.title("code or decode")

alphabet = list('0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x  y z'.replace(" ", ""))

string_for_copy = ""
key = ""
name = 0


def start() -> None:
    global name
    global string_for_copy
    global key
    if b2_start["text"] == "":
        l4_info["foreground"] = "red"
        return None
    out = tk.Tk()
    out.geometry()
    out.title("out result")
    up_1 = tk.Frame(out)
    up_2 = tk.Frame(out)
    l5_mode = tk.Label(out, text="mode: " + rename(1))
    ge_1 = e1_string.get()
    ge_2 = e2_code.get()
    if ge_2 == "" or ge_2 == "":
        l1_string["foreground"] = "red"
        l2_code["foreground"] = 'red'
        out.destroy()
        return None
    text = [ge_1, ge_2]
    """if text[1].find("#") == -1:
        text[1] = "10#" + text[1]"""
    if name == 1:
        key = e2_code.get()
        co_text = coding(text)
        string_for_copy = co_text
        l6_string = tk.Label(up_1, text="coded text: " + string_for_copy)
        l7_code = tk.Label(up_2, text="key code: " + key)
        if len(string_for_copy) < 32:
            out.geometry("256x120")
    else:
        de_text = decoding(text)
        error = tk.Tk()
        er = tk.Label(error, text=str(text))
        er.pack()
        error.mainloop()
        string_for_copy = (de_text)
        l6_string = tk.Label(up_1, text="decoded text: " + string_for_copy)
        l7_code = tk.Label(up_2, text="")
        if len(string_for_copy) < 32:
            out.geometry("256x120")
    l5_mode.pack()
    l6_string.pack(side=tk.LEFT)
    l7_code.pack(side=tk.LEFT)
    up_1.pack()
    up_2.pack()
    root.destroy()
    out.mainloop()


def help_window():
    help_frame = tk.Tk()
    help_frame.geometry()
    help_frame.title("Help")
    tk.Label(help_frame, text="В поле 'введите ключ' находятся числа и #.").pack()
    tk.Label(help_frame, text="").pack()
    tk.Label(help_frame, text="Все числа кроме последнего не должны").pack()
    tk.Label(help_frame, text="быть не больше 10, но больше 1,").pack()
    tk.Label(help_frame, text="а последнее не больше 36").pack()
    tk.Label(help_frame, text="").pack()
    help_frame.mainloop()


def rename(fi=0) -> str | None:
    global name
    l4_info["text"] = " "
    if fi == 0:
        if name == 0:
            b1_mode["text"] = "code"
            b2_start["text"] = "start coding"
            name = 1
        elif name == 1:
            b1_mode["text"] = "decode"
            b2_start["text"] = "start decoding"
            name = 0
        return None
    else:
        if name == 0:
            return "Decode"
        elif name == 1:
            return "Code"


def clean(before: str) -> str:
    return re.sub('[\W_]+', '', before)


def load(before: str) -> list[int]:
    """error = tk.Tk()
    er = tk.Label(error, text=str(before))
    er.pack()
    error.mainloop()"""
    before = str(before)
    return list(map(int, before.split('#')))


def decoding(a):
    a[0] = clean(a[0])
    a[1] = load(a[1][::-1])
    for i in a[1]:
        a[0] = str(int(a[0], i))
    return a[0]


def up(before, system):
    global alphabet
    system -= 0
    a, b = '', before
    while b > 0:
        x = int(b) % system
        a += alphabet[x]
        b = b // system
    return a[::-1]


def coding(a):
    a[0] = a[0] = clean(a[0])
    a[1] = load(a[1])
    for i in a[1]:
        a[0] = up(int(a[0]), i)
    return a[0]


string = tk.Frame(root)
code = tk.Frame(root)
mode = tk.Frame(root)

e1_string = tk.Entry(string)
e2_code = tk.Entry(code)
b1_mode = tk.Button(mode, text=" ", command=rename, width=8)
b2_start = tk.Button(text="", width=16, command=start)
b3_code = tk.Button(root, text="help", command=help_window)

l1_string = tk.Label(string, text="    enter string: ")
l2_code = tk.Label(code, text="enter key code: ")
l3_mode = tk.Label(mode, text="choose mode: ")

l1_string.pack(side=tk.LEFT)
l2_code.pack(side=tk.LEFT)
l3_mode.pack(side=tk.LEFT)
l4_info = tk.Label(text="chose mod to start:", foreground="black")

e1_string.pack(side=tk.RIGHT)
e2_code.pack(side=tk.RIGHT)
b1_mode.pack(side=tk.RIGHT)

string.pack(pady=2)
code.pack(pady=2)
b3_code.pack()
mode.pack(pady=2)

tk.Label(text=" ").pack()
l4_info.pack()

b2_start.pack()

root.mainloop()
