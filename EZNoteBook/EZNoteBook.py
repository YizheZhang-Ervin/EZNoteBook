# coding=utf-8

from builtins import str, len, range
from tkinter.filedialog import *
from tkinter.messagebox import *

filename = ""
bgcText = 'black'


def author():
    showinfo(title="Author", message="          ------Ervin.Zhang (AKA.哲戨)------          ")


def power():
    showinfo(title="CopyRight",
             message="    'This Notebook Belongs to Everyone'    \n    --[EZNoteBook Version 1.0.2]--  ")


def newFile():
    global root, filename, textPad
    root.title("Unnamed File")
    filename = None
    textPad.delete(1.0, END)


def openFile():
    global filename
    filename = askopenfilename(defaultextension=".txt")
    if filename == "":
        filename = None
    else:
        root.title("EZNoteBook" + os.path.basename(filename))
        textPad.delete(1.0, END)  # 1.0 =start of text
        f = open(filename, 'r')
        textPad.insert(1.0, f.read())
        f.close()


def saveFile():
    global filename
    try:
        f = open(filename, 'w')
        msg = textPad.get(1.0, END)
        f.write(msg)
        f.close()
    except:
        saveasFile()


def saveasFile():
    global filename
    f = asksaveasfilename(initialfile="unnamed.txt", defaultextension=".txt")
    filename = f
    fh = open(f, 'w')
    msg = textPad.get(1.0, END)
    fh.write(msg)
    fh.close()
    root.title("EZNoteBook" + os.path.basename(f))


def cut():
    global textPad
    textPad.event_generate("<<Cut>>")


def copy():
    global textPad
    textPad.event_generate("<<Copy>>")


def paste():
    global textPad
    textPad.event_generate("<<Paste>>")


def undo():
    global textPad
    textPad.event_generate("<<Undo>>")


def redo():
    global textPad
    textPad.event_generate("<<Redo>>")


def select_all():
    global textPad
    # textPad.event_generate("<<Cut>>")
    textPad.tag_add("sel", "1.0", "end")


def find():
    t = Toplevel(root)
    t.title("Search")
    t.geometry("350x60+200+250")
    t.transient(root)
    Label(t, text="Search：").grid(row=0, column=0, sticky="e")
    v = StringVar()
    e = Entry(t, width=20, textvariable=v)
    e.grid(row=0, column=1, padx=2, pady=2, sticky="we")
    e.focus_set()
    c = IntVar()
    Checkbutton(t, text="Ignore UpperCase & LowerCase", variable=c).grid(row=1, column=1, sticky='e')
    Button(t, text="Search All", command=lambda: search(v.get(), c.get(), textPad, t, e)).grid(row=0, column=2,
                                                                                               sticky="e" + "w", padx=2,
                                                                                               pady=2)

    def close_search():
        textPad.tag_remove("match", "1.0", END)
        t.destroy()

    t.protocol("WM_DELETE_WINDOW", close_search)


def rightClick(event):
    # global editmenu
    editmenu.tk_popup(event.x_root, event.y_root)


def search(needle, cssnstv, textPad, t, e):
    textPad.tag_remove("match", "1.0", END)
    count = 0
    if needle:
        pos = "1.0"
        while True:
            pos = textPad.search(needle, pos, nocase=cssnstv, stopindex=END)
            if not pos: break
            lastpos = pos + str(len(needle))
            textPad.tag_add("match", pos, lastpos)
            count += 1
            pos = lastpos
        textPad.tag_config('match', foreground="yellow", background="green")
        e.focus_set()
        t.title(str(count) + "were matched")


def changetheme():
    global bgcText
    if bgcText == 'black':
        textPad.config(bg='#FFFFCC', fg='black')
        toolbutton0.config(text='Black Theme')
        bgcText = 'white'
    else:
        textPad.config(bg='black', fg='#FF6600')
        toolbutton0.config(text='Eye-Protect Theme')
        bgcText = 'black'


def newInterface():
    toplevel=Toplevel(bg='black')
    toplevel.title('Have A Rest')
    toplevel.geometry("350x620+0+50")
    toplevel.config(cursor='spider')


# tkinter start
root = Tk()
root.title("  EZNoteBook  ")
root.geometry("1000x600+355+50")
root.resizable(width=TRUE, height=FALSE)

mainmenu = Menu(root, font=('time', 10))
root.config(menu=mainmenu)  # root['menu'] = mainmenu

# file menu
filemenu = Menu(mainmenu)
filemenu.add_command(label="New", accelerator="Ctrl+N", command=newFile)
filemenu.add_command(label="Open", accelerator="Ctrl+O", command=openFile)
filemenu.add_command(label="Save", accelerator="Ctrl+S", command=saveFile)
filemenu.add_command(label="Save As", accelerator="Ctrl+shift+s", command=saveasFile)
filemenu.config(font=('time', 10))
mainmenu.add_cascade(label="File", menu=filemenu)

# edit menu
editmenu = Menu(mainmenu)
editmenu.config(font=('time', 10))
editmenu.add_command(label="Undo", accelerator="Ctrl+Z", command=undo)
editmenu.add_command(label="Redo", accelerator="Ctrl+Y", command=redo)
editmenu.add_separator()
editmenu.add_command(label="Cut", accelerator="Ctrl+X", command=cut)
editmenu.add_command(label="Copy", accelerator="Ctrl+C", command=copy)
editmenu.add_command(label="Paste", accelerator="Ctrl+V", command=paste)
editmenu.add_separator()
editmenu.add_command(label="Search", accelerator="Ctrl+F", command=find)
editmenu.add_command(label="Select All", accelerator="Ctrl+A", command=select_all)
mainmenu.add_cascade(label="Edit", menu=editmenu)

# about menu
aboutmenu = Menu(mainmenu)
aboutmenu.config(font=('time', 10))
aboutmenu.add_command(label="Author", command=author)
aboutmenu.add_command(label="CopyRight", command=power)
mainmenu.add_cascade(label="About", menu=aboutmenu)

# entertainment menu
playmenu= Menu(mainmenu)
playmenu.config(font=('time', 10))
playmenu.add_command(label="Take A Rest", command=newInterface)
mainmenu.add_cascade(label="Play", menu=playmenu)


# status
status = Label(root, text='Line:xx', bd=1, relief=SUNKEN, anchor=E, bg='light gray')
status.pack(side=BOTTOM,fill=X)


ToolBar = Frame(root, height=25, bg='light gray')
toolbutton0 = Button(ToolBar, text="Eye-Protect Theme", command=changetheme, font=('time', 9), fg='white', bg='#333333')
toolbutton0.pack(side=LEFT, padx=5, pady=5)
toolbutton1 = Button(ToolBar, text="Open", command=openFile, font=('time', 9), fg='white', bg='#333333')
toolbutton1.pack(side=LEFT, padx=5, pady=5)
toolbutton2 = Button(ToolBar, text="Save", command=saveFile, font=('time', 9), fg='white', bg='#333333')
toolbutton2.pack(side=LEFT, padx=5, pady=5)
toolbutton3 = Button(ToolBar, text="Undo", command=undo, font=('time', 9), fg='white', bg='#333333')
toolbutton3.pack(side=LEFT, padx=5, pady=5)
toolbutton4 = Button(ToolBar, text="Redo", command=redo, font=('time', 9), fg='white', bg='#333333')
toolbutton4.pack(side=LEFT, padx=5, pady=5)
toolbutton5 = Button(ToolBar, text="Cut", command=cut, font=('time', 9), fg='white', bg='#333333')
toolbutton5.pack(side=LEFT, padx=5, pady=5)
toolbutton6 = Button(ToolBar, text="Copy", command=copy, font=('time', 9), fg='white', bg='#333333')
toolbutton6.pack(side=LEFT, padx=5, pady=5)
toolbutton7 = Button(ToolBar, text="Paste", command=paste, font=('time', 9), fg='white', bg='#333333')
toolbutton7.pack(side=LEFT, padx=5, pady=5)
ToolBar.pack(expand=NO, fill=X)

count = ''
for a in range(0, 35):
    count = str(count) + '\n' + str(a)
NumLabel = Label(root, width=2, fg='white', bg='#333333', bd=2, text=count, font=('time', 10))
NumLabel.pack(side=LEFT, anchor='nw', fill=Y)

textPad = Text(root, undo=True)
textPad.pack(expand=YES, fill=BOTH)
scroll = Scrollbar(textPad)
textPad.config(bg='black', fg='#FF6600', font=('time', 11))
textPad.config(yscrollcommand=scroll.set, cursor='spider')
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)

# key binding
textPad.bind("<Control-N>", newFile)
textPad.bind("<Control-n>", newFile)
textPad.bind("<Control-O>", openFile)
textPad.bind("<Control-o>", openFile)
textPad.bind("<Control-S>", saveFile)
textPad.bind("<Control-s>", saveFile)
textPad.bind("<Control-A>", select_all)
textPad.bind("<Control-a>", select_all)
textPad.bind("<Control-F>", find)
textPad.bind("<Control-f>", find)

textPad.bind("<Button-3>", rightClick)
root.mainloop()
