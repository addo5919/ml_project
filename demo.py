# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:41:53 2021

@author: Addo
"""

from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd

df=pd.read_csv("spam.csv",encoding='ISO-8859-1')
data = df.to_numpy()
print(data)
X = data[:, 1]
y = data[:, 0]
print(X.shape)
print(y.shape)



def myClick():
    message=myTextBox.get(1.0,END)
    messagebox.showinfo("Result","")
    myTextBox.delete(1.0,END)
 
        
root=Tk()
root.title("Spam message checker")
myLabel=Label(root,text="Enter the message:")
myTextBox=Text(root,width=60,height=20)
myButton=Button(root,text="Check",command=myClick)
myLabel.grid(row=0,column=0)
myTextBox.grid(row=1,column=0)
myButton.grid(row=2,column=0)
root.mainloop()

