# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 21:41:33 2022

@author: Raghav
"""

#Question 1

from tkinter import *
def findGst() :
    org_cost= int(org_priceField.get())
    N_price = int(net_priceField.get())
    gst_rate = ((N_price - org_cost) * 100) / org_cost;
    gst_rateField.insert(10, str(gst_rate) + " % ")
def clearAll():
    org_priceField.delete(0, END)
    net_priceField.delete(0, END)
    gst_rateField.delete(0, END)
if _name_ == "_main_" :
    gui = Tk()
    gui.configure(background = "yellow")
    gui.title("GST Rate Finder")
    gui.geometry("300x300")
    org_price = Label(gui, text = "Original Price",
                    bg = "light blue")
    net_price = Label(gui, text = "Net Price",
                    bg = "light blue")
    find = Button(gui, text = "Find", fg = "Black",
                bg = "light pink",
                command = findGst)
    gst_rate = Label(gui, text = "Gst Rate", bg = "light green")
    clear = Button(gui, text = "Clear", fg = "Black",
                bg = "light pink",
                command = clearAll)
    org_price.grid(row = 1, column = 1,padx = 10,pady = 10)
    net_price.grid(row = 2, column = 1, padx = 10, pady = 10)
    find.grid(row = 3, column = 2,padx = 10,pady = 10) 
    gst_rate.grid(row = 4, column = 1,padx = 10, pady = 10)
    clear.grid(row = 5, column = 2, padx = 10, pady = 10)
    org_priceField = Entry(gui)
    net_priceField = Entry(gui)
    gst_rateField = Entry(gui)
    org_priceField.grid(row = 1, column = 2 ,padx = 10,pady = 10)
    net_priceField.grid(row = 2, column = 2, padx = 10,pady = 10)
    gst_rateField.grid(row = 4, column = 2, padx = 10,pady = 10)
    gui.mainloop()
    
    
    
#Question 2

from tkinter import *
import calendar
def showCal() :
    new_gui = Tk()
    new_gui.config(background = "light green")
    new_gui.title("CALENDAR")
    new_gui.geometry("450x500")
    fetch_year = int(year_field.get())
    cal_content = calendar.calendar(fetch_year)
    cal_year = Label(new_gui, text = cal_content, font = "Consolas 10 bold")
    cal_year.grid(row = 5, column = 1, padx = 20)
    new_gui.mainloop()
if _name_ == "_main_" :
    gui = Tk()
    gui.config(background = "orange")
    gui.title("CALENDAR")
    gui.geometry("250x140")
    cal = Label(gui, text = "CALENDAR", bg = "green",
                            font = ("times", 28, 'bold'))
    year = Label(gui, text = "Enter Year", bg = "light pink")
    year_field = Entry(gui)
    Show = Button(gui, text = "Show Calendar", fg = "black",
                            bg = "yellow", command = showCal)
    Exit = Button(gui, text = "Exit", fg = "black", bg = "light blue", command = exit)
    cal.grid(row = 1, column = 1)
    year.grid(row = 2, column = 1)
    year_field.grid(row = 3, column = 1)
    Show.grid(row = 4, column = 1)
    Exit.grid(row = 6, column = 1)
    gui.mainloop()



#Question 3

from tkinter import *
expression = ""
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")
if _name_ == "_main_":
    gui = Tk()
    gui.configure(background="light yellow")
    gui.title("Simple Calculator")
    gui.geometry("270x150")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)
    button1 = Button(gui, text=' 1 ', fg='black', bg='light blue',
                    command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)
    button2 = Button(gui, text=' 2 ', fg='black', bg='light blue',
                    command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)
    button3 = Button(gui, text=' 3 ', fg='black', bg='light blue',
                    command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)
    button4 = Button(gui, text=' 4 ', fg='black', bg='light blue',
                    command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)
    button5 = Button(gui, text=' 5 ', fg='black', bg='light blue',
                    command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)
    button6 = Button(gui, text=' 6 ', fg='black', bg='light blue',
                    command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)
    button7 = Button(gui, text=' 7 ', fg='black', bg='light blue',
                    command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)
    button8 = Button(gui, text=' 8 ', fg='black', bg='light blue',
                    command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)
    button9 = Button(gui, text=' 9 ', fg='black', bg='light blue',
                    command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)
    button0 = Button(gui, text=' 0 ', fg='black', bg='light blue',
                    command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)
    plus = Button(gui, text=' + ', fg='black', bg='light green',
                command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='light green',
                command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='light green',
                    command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='light green',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)
    equal = Button(gui, text=' = ', fg='black', bg='orange',
                command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)
    clear = Button(gui, text='Clear', fg='white', bg='red',
                command=clear, height=1, width=7)
    clear.grid(row=5, column='1')
    Decimal= Button(gui, text='.', fg='black', bg='white',
                    command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    gui.mainloop()



#Question 4

def partition(l, r, nums):
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr
def quicksort(l, r, nums):
    if len(nums) == 1: # Terminating Condition for recursion. VERY IMPORTANT!
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums) # Recursively sorting the left values
        quicksort(pi+1, r, nums) # Recursively sorting the right values
    return nums
example = [4, 5, 1, 2, 3]
result = [1, 2, 3, 4, 5]
print(quicksort(0, len(example)-1, example))
example = [2, 5, 6, 1, 4, 6, 2, 4, 7, 8]
result = [1, 2, 2, 4, 4, 5, 6, 6, 7, 8]
print(quicksort(0, len(example)-1, example))



#Question 5

def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print (Repeat(list1))
print(quicksort(0, len(list1)-1, list1))

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return -1
arr = list1
x = int(input("Enter Element : "))
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")



#Question 6

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))


































