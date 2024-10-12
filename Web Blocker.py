from tkinter import *
import os

def Blocker():
    website_lists = Websites.get(1.0, END)
    Website = list(website_lists.split(","))
    with open(host_path, 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website.strip() in file_content:
                Label(root, text='Already Blocked', font='arial 12 bold').place(x=200, y=200)
            else:
                host_file.write(ip_address + " " + website.strip() + '\n')
                Label(root, text="Blocked", font='arial 12 bold').place(x=230, y=200)

def Unblocker():
    website_lists = Websites.get(1.0, END)
    Website = list(website_lists.split(","))
    with open(host_path, 'r+') as host_file:
        lines = host_file.readlines()
        host_file.seek(0)
        for line in lines:
            if not any(website.strip() in line for website in Website):
                host_file.write(line)
        host_file.truncate()
        Label(root, text="Unblocked", font='arial 12 bold').place(x=230, y=200)

if 'DISPLAY' not in os.environ:
    # Handle non-graphical environment
    pass
else:
    root = Tk()
    root.geometry('500x300')
    root.resizable(0, 0)
    root.title("Website Blocker")

    Label(root, text='WEBSITE BLOCKER', font='arial 20 bold').pack()

    host_path = r'C:\Windows\System32\drivers\etc\hosts'
    ip_address = '127.0.0.1'

    Label(root, text='Enter Website :', font='arial 13 bold').place(x=5, y=60)
    Websites = Text(root, font='arial 10', height='2', width='40', wrap=WORD, padx=5, pady=5)
    Websites.place(x=140, y=60)

    block = Button(root, text='Block', font='arial 12 bold', pady=5, command=Blocker,
                   width=6, bg='royal blue1', activebackground='sky blue')
    block.place(x=230, y=150)

    unblock = Button(root, text='Unblock', font='arial 12 bold', pady=5, command=Unblocker,
                     width=6, bg='red', activebackground='pink')
    unblock.place(x=320, y=150)

    root.mainloop()
