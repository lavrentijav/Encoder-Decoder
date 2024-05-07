import re
import tkinter as tk
import sys

sys.set_int_max_str_digits(5000000)
root = tk.Tk()
root.geometry("300x205")
root.title("Encode or Decode")

""" settings
    len string for read"""
l_string = 64

alphabet = list('0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x  y z'.replace(" ", ""))

string_for_copy = ""
key = ""
name_1 = 0
name_2 = 0


class Copy(object):

    @staticmethod
    def line() -> None:
        global string_for_copy
        copy_line = tk.Tk()
        copy_line.withdraw()
        copy_line.clipboard_clear()
        copy_line.clipboard_append(string_for_copy)
        copy_line.update()
        copy_line.destroy()

    @staticmethod
    def key() -> None:
        global key
        copy_key = tk.Tk()
        copy_key.withdraw()
        copy_key.clipboard_clear()
        copy_key.clipboard_append(key)
        copy_key.update()
        copy_key.destroy()


class Bottom(object):

    @staticmethod
    def start() -> None:
        global name_1
        global string_for_copy
        global key

        ge_1 = e1_string.get()
        ge_2 = e2_code.get()
        text = [ge_1, ge_2]
        key = e2_code.get()

        if ge_2 == "":
            l1_string["foreground"] = "red"
            return None
        elif ge_2 == "":
            l2_code["foreground"] = 'red'
            return None
        elif b4_mode["text"] == "":
            l4_info["foreground"] = "red"
            l8_mode["foreground"] = 'red'
            return None
        elif b2_start["text"] == "":
            l3_mode["foreground"] = "red"
            l4_info["foreground"] = "red"
            return None
        else:
            out = tk.Tk()
            out.geometry()
            out.title("out result")

        flag = True
        up_1 = tk.Frame(out)
        up_2 = tk.Frame(out)

        error = tk.Tk()
        tk.Label(error, text="The script was certified with an ERROR", foreground="red", font=("Arial", 72)).pack()
        err = "check that the string, key and settings are correct"
        tk.Label(error, text=err, foreground="red", font=("Arial", 20)).pack()
        if name_1 == 1:
            if name_2 == 0:
                text[0] = Processing.txt_bin(text[0])
            string_for_copy = Processing.encoding(text)
            if len(string_for_copy) > 5000:
                l6_string = tk.Label(up_1, text="encoded text: " + "text if bigest for print" + "      ")
            else:
                l6_string = tk.Label(up_1, text="encoded text: " + string_for_copy + "      ")
            l7_code = tk.Label(up_2, text="key code: " + key)
        else:
            string_for_copy = Processing.decoding(text)
            print(string_for_copy)
            if name_2 == 0:
                string_for_copy = Processing.bin_txt(string_for_copy)
            print(string_for_copy)
            if len(string_for_copy) > 5000:
                l6_string = tk.Label(up_1, text="decoded text: " + "text if bigest for print" + "      ")
            else:
                l6_string = tk.Label(up_1, text="decoded text: " + string_for_copy + "      ")
            l7_code = tk.Label(up_2, text="")

        out.geometry(str(len(string_for_copy) + 60) + "x120")

        l5_mode = tk.Label(out, text="mode: " + Bottom.rename_1(1))
        b4_copy = tk.Button(out, text="press for copy", command=Copy.line)
        b5_copy = tk.Button(out, text="press for copy", command=Copy.key)

        l5_mode.pack()
        l6_string.pack(side=tk.LEFT)
        l7_code.pack(side=tk.LEFT)
        up_1.pack()
        b4_copy.pack()
        up_2.pack()
        b5_copy.pack()

        root.destroy()
        error.destroy()

        out.mainloop()

    @staticmethod
    def help_window():
        help_frame = tk.Tk()
        help_frame.geometry()
        help_frame.title("Help")
        tk.Label(help_frame, text="").pack()
        tk.Label(help_frame, text="В поле 'введите ключ' находятся числа и #.     .").pack()
        tk.Label(help_frame, text="").pack()
        tk.Label(help_frame, text="Все числа кроме последнего не должны           .").pack()
        tk.Label(help_frame, text="быть не больше 10, но больше 1,                .").pack()
        tk.Label(help_frame, text="а последнее не больше 36                       .").pack()
        tk.Label(help_frame, text="").pack()
        tk.Label(help_frame, text="").pack()
        tk.Label(help_frame, text="режимы чтения:                                 .").pack()
        tk.Label(help_frame, text="* 'Number' в строке не осмысленый текст         .").pack()
        tk.Label(help_frame, text="* 'Text' в строке числа                         .").pack()
        tk.Label(help_frame, text=" если строка зашифрована спросите у собеседника.").pack()
        tk.Label(help_frame, text="").pack()
        tk.Label(help_frame, text="").pack()
        tk.Label(help_frame, text="режимы обработки:                              .").pack()
        tk.Label(help_frame, text="* 'Encoding' зашифровать введённую строку       .").pack()
        tk.Label(help_frame, text="* 'Decoding' расшифровать введённую строку      .").pack()
        tk.Label(help_frame, text="").pack()
        tk.Label(help_frame, text="").pack()
        help_frame.mainloop()

    @staticmethod
    def rename_1(fi=0) -> str | None:
        global name_1
        l4_info["text"] = " "
        if fi == 0:
            if name_1 == 0:
                b1_mode["text"] = "Encode"
                b2_start["text"] = "start encoding"
                name_1 = 1
            elif name_1 == 1:
                b1_mode["text"] = "decode"
                b2_start["text"] = "start decoding"
                name_1 = 0
            return None
        else:
            if name_1 == 0:
                return "Decode"
            elif name_1 == 1:
                return "Encode"

    @staticmethod
    def rename_2(fi=0) -> str | None:
        global name_2
        l4_info["text"] = " "
        if fi == 0:
            if name_2 == 0:
                b4_mode["text"] = "Number"
                name_2 = 1
            elif name_2 == 1:
                b4_mode["text"] = "String"
                name_2 = 0
            return None
        else:
            if name_2 == 0:
                return "Number"
            elif name_2 == 1:
                return "String"


class Processing(object):

    @staticmethod
    def clean(text: str) -> str:
        if name_2 == 1:
            return re.sub('[\W_]+', '', text)
        else:
            return text

    @staticmethod
    def load(text: str) -> list[int]:
        text = str(text)
        text = list(map(int, text.split('#')))
        print(text)
        return text

    @staticmethod
    def decoding(text: list) -> str:
        text[0] = Processing.clean(text[0])

        mx = text[1].split("#")
        xm = mx[0]
        del mx[0]
        for i in mx:
            xm = (xm[::-1] + "#" + i[::-1])[::-1]
        print(xm)
        text[1] = Processing.load(xm)
        for i in text[1]:
            print(text[0])
            text[0] = str(int(text[0], i))
            print("de")
        return text[0]

    @staticmethod
    def up(text: str | int, system) -> str:
        global alphabet
        system -= 0
        a, b = '', text
        while b > 0:
            x = int(b) % system
            a += alphabet[x]
            b = b // system
        return a[::-1]

    @staticmethod
    def encoding(roster: list[str]):
        roster[0] = Processing.clean(roster[0])
        roster[1] = Processing.load(roster[1])
        for i in roster[1]:
            roster[0] = Processing.up(int(roster[0]), i)
        return roster[0]

    @staticmethod
    def txt_bin(text: str) -> str:
        out = ""
        for i in list(text):
            print(i)
            out += str("0"*(4-len(str(ord(i))))) + str(ord(i))
        print(out)
        return "1" + out

    @staticmethod
    def bin_txt(text: str) -> str:
        out = ""
        for j in re.findall('.' * 4, text[1::]):
            print(j)
            out += str(chr(int(j)))
        return out


string = tk.Frame(root)
code = tk.Frame(root)
mode = tk.Frame(root)
mode_2 = tk.Frame(root)

e1_string = tk.Entry(string, width=l_string)
e2_code = tk.Entry(code)
b1_mode = tk.Button(mode, text=" ", command=Bottom.rename_1, width=8)
b2_start = tk.Button(text="", width=16, command=Bottom.start)
b3_code = tk.Button(root, text="help", command=Bottom.help_window)
b4_mode = tk.Button(mode_2, text=" ", command=Bottom.rename_2, width=8)

l1_string = tk.Label(string, text="    enter string: ")
l2_code = tk.Label(code, text="enter key code: ")
l3_mode = tk.Label(mode, text="choose processing mode: ")
l4_info = tk.Label(text="chose mod to start:", foreground="black")
l8_mode = tk.Label(mode_2, text="choose reading mode: ")

l1_string.pack(side=tk.LEFT)
l2_code.pack(side=tk.LEFT)
l3_mode.pack(side=tk.LEFT)
l8_mode.pack(side=tk.LEFT)

e1_string.pack(side=tk.RIGHT)
e2_code.pack(side=tk.RIGHT)
b1_mode.pack(side=tk.RIGHT)
b4_mode.pack(side=tk.RIGHT)

string.pack(pady=2)
code.pack(pady=2)
b3_code.pack()
mode.pack(pady=2)
mode_2.pack(pady=2)

tk.Label(text=" ").pack()

l4_info.pack()
b2_start.pack()

root.mainloop()
