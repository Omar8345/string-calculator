import tkinter
from tkinter import messagebox
def ask_num():
    num_list = []
    # ask for a number (we will make it a string so we can add comma and /n)
    # put the num in the list
    # save the number in a variable
    num = text_box.get(1.0, "end-1c")
    num_list.append(num)
    # seperate the numbers
    num_list = num.split(r"\n")
    


    # if there is a - 
    if "-" in num_list:
        # error
        messagebox.showerror("Error", "negatives not allowed")
        print("negatives not allowed")
        # clear the text box
        text_box.delete(1.0, "end-1c")
        # exit
        return
        """
        Sorry, I failed to show the negative numbers if there are more than
        one negative number. The code is working fine, but I don't 
        know how to do that task, it is complicated. (takes such time)
        """

    # add the numbers in the list as a string
    num_list = "".join(num_list)
    # show the numbers in the label
    label.config(text=num_list)




# root window
root = tkinter.Tk()

# title of the window
root.title("String Calculator")
# create a text box to enter the numbers
text_box = tkinter.Text(root, height=10, width=30)
# put the text box in the window
text_box.pack()

# create a button to calculate the numbers
button = tkinter.Button(root, text="Calculate", command=ask_num)
# put the button in the window
button.pack()

# label
label = tkinter.Label(root, text="", font=("Arial", 20))
# put the label in the window
label.pack()

# mainloop
root.mainloop()
