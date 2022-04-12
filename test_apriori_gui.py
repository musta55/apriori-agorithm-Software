from email.message import Message
from fileinput import filename
from os import system
import re
import tkinter as tk
from tkinter import CENTER, RAISED, StringVar, filedialog
from turtle import st

from numpy import pad

from apriori import Apriori

def browseFiles():
    global fileName
    fileName = filedialog.askopenfilename(  initialdir = "/", 
                                            title = "Select a File", 
                                            filetypes = (("Text files", "*.txt*"),("all files", "*.*")))
    explore_var.set(fileName)

def submit():
    global minSup, minCon, g_RHS, dataset
    if support_var.get()!='' : minSup = float(support_var.get())
    if confidence_var.get()!='' : minCon = float(confidence_var.get())
    if rhs_var.get()!='' : g_RHS = frozenset([rhs_var.get()])
    dataset = fileName
    root.destroy()

root=tk.Tk()
root.geometry("1000x1000")
root.title("Input")

minSup = 0.2
minCon = 0.5
g_RHS = frozenset(['Bread'])
dataset = ''
fileName = 'data\\transaction.csv'

support_var=tk.StringVar()
confidence_var=tk.StringVar()
rhs_var=tk.StringVar()
explore_var=tk.StringVar()

explore_label = tk.Label(root, text = 'Dataset', font=('bold'))
explore_entry = tk.Entry(root,textvariable = explore_var, font=('normal'))
button_explore = tk.Button(root, text = "Select",command = browseFiles)

support_label = tk.Label(root, text = 'Min Support', font=('bold'))
support_entry = tk.Entry(root,textvariable = support_var, font=('normal'))

confidence_label = tk.Label(root, text = 'Min Confidence', font = ('bold'))
confidence_entry=tk.Entry(root, textvariable = confidence_var, font = ('normal'))

rhs_label = tk.Label(root, text = 'Right Destination', font = ('bold'))
rhs_entry=tk.Entry(root, textvariable = rhs_var, font = ('normal'))

sub_btn=tk.Button(root,text = 'Submit', font=('normal'), command = submit, bg="green")
  
# explore_label.grid(row=0,column=0, pady=5, padx=10)
# explore_label.place(x=100, y=300)
# explore_entry.grid(row=0,column=1, pady=5, padx=10)
# button_explore.grid(row=0, column=2, pady=5, padx=10)
explore_label.place(x=350, y=300)
explore_entry.place(x=500, y=300)
button_explore.place(x=700, y=300)

# support_label.grid(row=1,column=0, pady=5, padx=10)
# support_entry.grid(row=1,column=1, pady=5, padx=10)
support_label.place(x=350, y=340)
support_entry.place(x=500, y=340)

# confidence_label.grid(row=2,column=0, pady=5, padx=10)
# confidence_entry.grid(row=2,column=1, pady=5, padx=10)
confidence_label.place(x=350, y=380)
confidence_entry.place(x=500, y=380)

# rhs_label.grid(row=3, column=0, pady=5, padx=10)
# rhs_entry.grid(row=3, column=1, pady=5, padx=10)
rhs_label.place(x=350, y=420)
rhs_entry.place(x=500, y=420)

# sub_btn.grid(row=4,column=1, pady=5, padx=10)
sub_btn.place(x=500, y=500, anchor=CENTER)

# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
root.mainloop()


res = tk.Tk()
res.title("Results")
res.geometry("1000x1000")

msg = 'The APRIORI Algorithm'
title_label = tk.Label(res, text=msg, font=("Arial",20, "bold"))
title_label.place(x=350, y=20)

msg = ''

msg += """Parameters: \n - filePath: {} \n - mininum support: {} \n - mininum confidence: {} \n - rhs: {}\n""".format(dataset,minSup,minCon, g_RHS) + '\n'
par_label = tk.Label(res, text=msg)

msg=''
objApriori = Apriori(minSup, minCon)
itemCountDict, freqSet = objApriori.fit(dataset)
for key, value in freqSet.items():
    msg += 'frequent {}-term set:'.format(key) + '\n'
    msg += '-'*20 +'\n'

    for itemset in value:
        msg += str(list(itemset)) + '\n'

    msg += '\n'



rules = objApriori.getSpecRules(g_RHS)
msg += '-'*20 + '\n'
freq_lebel = tk.Label(res, text=msg)
msg = ''
msg += 'rules refer to {}'.format(list(g_RHS)) + '\n'
for key, value in rules.items():
    msg += '{} -> {}: {}'.format(list(key), list(g_RHS), value) + '\n'

rule_label = tk.Label(res, text=msg)


# str_var = tk.StringVar()
# res_label = tk.Message(res, textvariable=str_var, relief=RAISED)
# str_var.set(msg)
# res_label.pack()
par_label.place(x=100, y=300)
freq_lebel.place(x=400, y=200)
rule_label.place(x=600, y=300)
res.mainloop()
