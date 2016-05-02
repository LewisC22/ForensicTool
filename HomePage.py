# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, 'G:/1516PythonProject2.0/GUI/ChromeCode')
sys.path.insert(0, 'G:/1516PythonProject2.0/GUI/WebCrawler')
sys.path.insert(0, 'G:/1516PythonProject2.0/GUI/PasswordGenerator')
sys.path.insert(0, 'G:/1516PythonProject2.0/GUI/TrueCryptCrack')

from Tkinter import *
import tkMessageBox

from ChromeCode.ChromeHistory import *
from ChromeCode.ChromeDecryption import *
from WebCrawler.main import MainSpider
from WebCrawler.Spider import Spider
#from PasswordGenerator.PassGen import PasssGen
#from TrueCryptCrack.Dictionary_Attack import *

Histclass = HP()
LoginDataclass = LDP()
WebCrawlerclass = MainSpider()
WebSpiderclass = Spider
#PassGenclass = PasssGen()
#DictAttackclass = DictAttack()


OPTIONS = [
    "Homepage",
    "Instructions",
    "Contact Page"
]


root = Tk()
root.title("Tittle")
root.geometry('700x300')

var = StringVar(root)
var.set("Menu")
#var.set(OPTIONS[0])

menu = apply(OptionMenu, (root, var) + tuple(OPTIONS))
menu.pack(side=TOP, anchor=W)

#Set the separator between the menu and the buttons
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=1, pady=20)

top = Frame(root)
center = Frame(root)
bottom = Frame(root)
top.pack(side=TOP)
center.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

#Method to change the GUI when an option from the Menu is selected
def change_age(*args):
    if var.get()=="Homepage":
        b1.pack(in_=center, side=LEFT)
        b2.pack(in_=center, side=LEFT)
        b3.pack(in_=center, side=LEFT)
        b4.pack(in_=center, side=LEFT)
        b5.pack_forget()
        b6.pack_forget()
        b7.pack_forget()
        b8.pack_forget()
        b9.pack_forget()
        b10.pack_forget()
        b11.pack_forget()
        L1.pack_forget()
        L2.pack_forget()
    if var.get()=="Instructions":
        b1.pack_forget()
        b2.pack_forget()
        b3.pack_forget()
        b4.pack_forget()
        b5.pack_forget()
        b6.pack_forget()
        b7.pack_forget()
        b8.pack_forget()
        b9.pack_forget()
        b10.pack_forget()
        b11.pack_forget()
        L1.pack(in_=center, side=LEFT)
        L2.pack_forget()
    if var.get()=="Contact Page":
        b1.pack_forget()
        b2.pack_forget()
        b3.pack_forget()
        b4.pack_forget()
        b5.pack_forget()
        b6.pack_forget()
        b7.pack_forget()
        b8.pack_forget()
        b9.pack_forget()
        b10.pack_forget()
        b11.pack_forget()
        L1.pack_forget()
        L2.pack(in_=center, side=LEFT)

#Method to change the GUI when the button Database Parser is pressed
def database():
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    b4.pack_forget()
    b5.pack(in_=center, side=LEFT)
    b6.pack(in_=center, side=LEFT)

#Method to change the GUI when the button Web Crawler is pressed
def crawler():
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    b4.pack_forget()
    b7.pack(in_=center, side=LEFT)

#Method to change the GUI when the button Password Generator is pressed
def password():
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    b4.pack_forget()
    b8.pack(in_=center, side=LEFT)
    b9.pack(in_=center, side=LEFT)
    b10.pack(in_=center, side=LEFT)

#Method to change the GUI when the button Dictionary Attack is pressed
def dictionary():
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    b4.pack_forget()
    b11.pack(in_=center, side=LEFT)

def HistoryParser():
    tkMessageBox.showinfo("", "History Parser")
    Histclass.HistParser()
def LoginDataParser():
    tkMessageBox.showinfo("", "Database has now been Parsed, Proceed to Web Crawler")
    LoginDataclass.LDParser()

def RunWebCrawler():
    tkMessageBox.showinfo("", "Web Crawling successful to Stage 3 if necessary")
    WebCrawlerclass.CopyFile()
    WebSpiderclass.boot()
    WebCrawlerclass.create_workers()
    WebCrawlerclass.get_keywords()
    WebCrawlerclass.crawl()
    WebCrawlerclass.create_jobs()

def PasswordNumGen():
    tkMessageBox.showinfo("", "Your Password List has been produced, proceed to Dictionary Attack")
    PasssGen.PWNumCombo()
def PasswordSpecGen():
    tkMessageBox.showinfo("", "Your Password List has been produced, proceed to Dictionary Attack")
    PasssGen.PWSpecCombo()
def PasswordNumSpecGen():
    tkMessageBox.showinfo("", "Your Password List has been produced, proceed to Dictionary Attack")
    PasssGen.PWSMultiCombo()
def DictionaryAttack():
    tkMessageBox.showinfo("", "Your attack has been launched, Please wait for results")
    DictAttackclass.__init__()
    DictAttackclass.load_passwords()
    DictAttackclass.dict_attack()
    DictAttackclass.cmd()

var.trace('w', change_age)

# create the widgets for the top part of the GUI
b1 = Button(root, text="Database Parser", height=5, command=database)
b1.place(x=170, y=500)
b2 = Button(root, text="Web Crawler", height=5, command=crawler)
b3 = Button(root, text="Password Generator", height=5, command=password)
b4 = Button(root, text="Dictionary Attack", height=5, command=dictionary)

#Database Parser
b5 = Button(root, text="History Parser", height=5, command=HistoryParser)
b6 = Button(root, text="Login Data Parser", height=5, command=LoginDataParser)

#Web Crawler
b7 = Button(root, text="Run Web Crawler", height=5, command=RunWebCrawler)

#Password Generator
b8 = Button(root, text="Password -\nAlphanumerical Combination", height=5, command=PasswordNumGen)
b9 = Button(root, text="Password - Words &\nSpecial Characters", height=5, command=PasswordSpecGen)
b10 = Button(root, text="Password - Alphanumerical\nwith Special Characters", height=5, command=PasswordNumSpecGen)

#Dictionary Attack
b11 = Button(root, text="Launch Dictionary Attack", height=5, command=DictionaryAttack)

#Instructions labels
L1 = Label(root, text="Instructions:\n To edit instructions")
L2 = Label(root, text="Contact Page:\n To add contact information")


b1.pack(in_=center, side=LEFT)
b2.pack(in_=center, side=LEFT)
b3.pack(in_=center, side=LEFT)
b4.pack(in_=center, side=LEFT)

# create the widgets for the bottom part of the GUI,
# and lay them out

#text = Text(root, width=35, height=15)
#scrollbar = Scrollbar(root)
#scrollbar.config(command=text.yview)
#text.config(yscrollcommand=scrollbar.set)
#scrollbar.pack(in_=bottom, side=RIGHT, fill=Y)
#text.pack(in_=bottom, side=LEFT, fill=BOTH, expand=True)

root.mainloop()
