from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import re

#____________________________________________________________________ Functions ____________________________________________________________________

def search():    
    st2.delete('1.0', END)
    my_search = re.findall(e1.get(), st1.get("1.0",'end-1c'))
    for item in my_search:
        st2.insert(INSERT, item+"\n")

def clear():
    e1.delete('0', END)  
    st1.delete('1.0', END)  
    st2.delete('1.0', END)

def example():
    e1.insert(INSERT, "[A-z0-9\.]+@[A-z0-9]+\.[A-z]+")  
    for i in range(4):
        st1.insert(INSERT, f"{i}) my email => Test.{i}@mail.ma my name => test{i}\n")

#------------------------
window = Tk()
window.title("RegEx App")
window.minsize(1100, 1000)
window.maxsize(1100, 1000)
#------------------------
#____________________________________________________________________ Tabs ____________________________________________________________________
s = ttk.Style()
s.configure('TNotebook.Tab', font=('Arial','15'))
s.configure('TNotebook', tabposition='n')
tabs = ttk.Notebook(window)
tab1 = Frame(tabs)
tab2 = Frame(tabs)
tabs.add(tab1, text="Search")
tabs.add(tab2, text="Rules")

tabs.pack(side=TOP)

#____________________________________________________________________ Tab 1 ____________________________________________________________________
m_f = Frame(tab1)
f1 = Frame(m_f)
f2 = Frame(m_f) #for buttons

Label(f1, text="Regular Expression : ", font=("Arial", 13)).grid(row=0, column=0, sticky="W")
e1 = Entry(f1, width=50, font=("Arial", 13))
Label(f1, text="Test string : ", font=("Arial", 13)).grid(row=2, column=0, sticky="W")
st1 = ScrolledText(f1, width=50,height=4, font=("Arial", 13))
Label(f1, text="Match information : ", font=("Arial", 13)).grid(row=4, column=0, sticky="W")
st2 = ScrolledText(f1, width=50,height=4, font=("Arial", 13))

b1 = Button(f2, text="Search", font=("Arial", 13), command=search)
b2 = Button(f2, text="Clear text", font=("Arial", 13), command=clear)
b3 = Button(f2, text="Example Email Search", font=("Arial", 13), command=example)

#------------------------------- Display ----------------------------
e1.grid(row=1, column=0, sticky="W", padx=10, pady=10)
st1.grid(row=3, column=0, sticky="W", padx=10, pady=10)
st2.grid(row=6, column=0, sticky="W", padx=10, pady=10)

b1.grid(row=1, column=1, sticky="E", padx=10, pady=10)
b2.grid(row=1, column=2, sticky="E", padx=10, pady=10)
b3.grid(row=1, column=3, sticky="E", padx=10, pady=10)

f1.pack()
f2.pack()

m_f.place(relx=0.5, rely=0.5, anchor=CENTER)

#____________________________________________________________________ Tab 2 ____________________________________________________________________

#-------------------------------- g1 --------------------------------
g1 = ttk.Labelframe(tab2, text="Regular Expression Basics")
g1_l = [".\tAny character except newline", "a\tThe character a", "ab\tThe string ab", "a|b\ta or b", "a*\t0 or more a's","\\\tEscapes a special character"]
for i in range(len(g1_l)):
    Label(g1, text=g1_l[i], font=('Arial', 13)).grid(row=i, column=0, sticky="W")

#-------------------------------- g2 --------------------------------
g2 = ttk.Labelframe(tab2, text="Regular Expression Quanitfiers")
g2_l = ["*\t0 or more", "+\t1 or more", "?\t0 or 1", "{2}\tExactly 2", "{2, 5}\tBetween 2 and 5", "{2,}\t2 or more", "{,5}\tUp to 5"]
for i in range(len(g2_l)):
    Label(g2, text=g2_l[i], font=('Arial', 13)).grid(row=i, column=0, sticky="W")

#-------------------------------- g3 --------------------------------
g3 = ttk.Labelframe(tab2, text="Regular Expression Groups")
g3_l = ["(...)\tCapturing group", "(?P<Y>...)\tCapturing group named Y", "(?:...)\tNon-capturing group", "\\Y\tMatch the Y'th captured group", "(?P=Y)\tMatch the named group Y", "(?#...)\tComment"]
for i in range(len(g3_l)):
    Label(g3, text=g3_l[i], font=('Arial', 13)).grid(row=i, column=0, sticky="W")

#-------------------------------- g4 --------------------------------
g4 = ttk.Labelframe(tab2, text="Regular Expression Character Classes")
g4_l = ["[ab-d]\tOne character of: a, b, c, d", "[^ab-d]\tOne character except: a, b, c, d", "[\\b]\tBackspace character", "\d\tOne digit", "\D\tOne non-digit", "\s\tOne whitespace", "\S\tOne non-whitespace", "\w\tOne word character", "\W\tOne non-word character"]
for i in range(len(g4_l)):
    Label(g4, text=g4_l[i], font=('Arial', 13)).grid(row=i, column=0, sticky="W")

#-------------------------------- g5 --------------------------------
g5 = ttk.Labelframe(tab2, text="Regular Expression Assertions")
g5_l = ["^\tStart of string", "\A\tStart of string, ignores m flag", "$\tEnd of string", "\Z\tEnd of string, ignores m flag", "\\b\tWord boundary", "\B\tNon-word boundary", "(?=...)\tPositive lookahead", "(?!...)\tNegative lookahead", "(?<=...)\tPositive lookbehind", "(?<!...)\tNegative lookbehind", "(?()|)\tConditional"]
for i in range(len(g5_l)):
    Label(g5, text=g5_l[i], font=('Arial', 13)).grid(row=i, column=0, sticky="W")

#-------------------------------- g6 --------------------------------
g6 = ttk.Labelframe(tab2, text="Regular Expression Flags")
g6_l = ["i\tIgnore case", "m\t^ and $ match start and end of line", "s\t. matches newline as well", "x\tAllow spaces and comments", "L\tLocale character classes", "u\tUnicode character classes", "(?iLmsux)\tSet flags within regex"]
for i in range(len(g6_l)):
    Label(g6, text=g6_l[i], font=('Arial', 13)).grid(row=i, column=0, sticky="W")

#-------------------------------- g7 --------------------------------
g7 = ttk.Labelframe(tab2, text="Regular Expression Special Characters")
g7_l = ["\\n\tNewline", "\\r\tCarriage return", "\\t\tTab", "\\YYY\tOctal character YYY", "\\xYY\tHexadecimal character YY"]
for i in range(len(g7_l)):
    Label(g7, text=g7_l[i], font=('Arial', 13)).grid(row=i, column=0, sticky="W")

#-------------------------------- g8 --------------------------------
g8 = ttk.Labelframe(tab2, text="Regular Expression Replacement")
g8_l = ["\g<0>\tInsert entire match", "\g<Y>\tInsert match Y (name or number)", "\Y\tInsert group numbered Y"]
for i in range(len(g8_l)):
    Label(g8, text=g8_l[i], font=('Arial', 13)).grid(row=i, column=0, sticky="W")

#------------------------------ Display groups ------------------------------ 
groups1 = [g1, g2, g3]
for i in range(len(groups1)):
    groups1[i].grid(row=i, column=0, padx=10, pady=10)

groups2 = [g4, g5]
for i in range(len(groups2)):
    groups2[i].grid(row=i, column=1, padx=10, pady=10)

groups3 = [g6, g7, g8]
for i in range(len(groups2)):
    groups3[i].grid(row=i, column=2, padx=10, pady=10)

window.mainloop()

























































































































































"""made with love by Med Reda © 2022"""