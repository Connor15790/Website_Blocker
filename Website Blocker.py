from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("Website Blocker")
host_path = 'C:\Windows\System32\drivers\etc\hosts'
Ip_address = '127.0.0.1'

main_label = Label(root, text="Website Blocker", font="Times 20 bold").place(x=155, y=0)

# Creating the entry field and label
entry_label = Label(root, text="Enter Website: ", font="Arial 14").grid(row=1, column=0, padx=10, pady=(80, 10))
entry_field = Text(root, font = 'arial', height='1', width = '25')
entry_field.place(x= 190,y = 80)

# Creating the block function
def Block():
    websites_list = entry_field.get(1.0, END)
    Websites = list(websites_list.split(","))
    with open(host_path, "r+") as host_file:
        file_content = host_file.read()
        for i in Websites:
            if i in file_content:
                Label(root, text="Already Blocked", font="Arial 14").grid(row=3, column=0)
                pass
            else:
                host_file.write(Ip_address + " " + i + "\n")
                Label(root, text="Website has been blocked").grid(row=3, column=0)
# Create Block Button
block_btn = Button(root, text="Block", command=Block, bg="red").grid(row=2, column=1, padx=(0, 45), pady=20, ipadx=80, ipady=5)

mainloop()