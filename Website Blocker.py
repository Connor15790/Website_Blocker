from tkinter import *

root = Tk()
root.geometry("500x350")
root.title("Website Blocker")

# Path and IP Address
host_path = r'C:\Windows\System32\drivers\etc\hosts'
Ip_address = '127.0.0.1'

# Setting a consistent font style
title_font = ("Times", 24, "bold")
label_font = ("Arial", 14)
button_font = ("Arial", 12, "bold")

# Main Title
main_label = Label(root, text="Website Blocker", font=title_font, fg="navy")
main_label.pack(pady=20)

# Entry Label
entry_label = Label(root, text="Enter Website(s) (comma-separated):", font=label_font)
entry_label.pack(pady=10)

# Entry Field
entry_field = Text(root, font='Arial 12', height=2, width=40, borderwidth=2, relief="groove")
entry_field.pack(pady=10)

# Status Label
status_label = Label(root, text="", font=label_font, fg="green")
status_label.pack(pady=10)

# Block Function
def Block():
    websites_list = entry_field.get(1.0, END).strip()
    Websites = list(websites_list.split(","))
    if not Websites[0]:
        status_label.config(text="Please enter a website.", fg="red")
        return

    with open(host_path, "r+") as host_file:
        file_content = host_file.read()
        blocked_sites = []
        for website in Websites:
            if Ip_address + " " + website in file_content:
                blocked_sites.append(website)
            else:
                host_file.write(Ip_address + " " + website + "\n")
        
        if blocked_sites:
            status_label.config(text=f"Already Blocked: {', '.join(blocked_sites)}", fg="orange")
        else:
            status_label.config(text="Website(s) blocked successfully!", fg="green")

# Unblock Function
def Unblock():
    websites_list = entry_field.get(1.0, END).strip()
    Websites = list(websites_list.split(","))
    if not Websites[0]:
        status_label.config(text="Please enter a website.", fg="red")
        return

    with open(host_path, "r+") as host_file:
        file_content = host_file.readlines()
        host_file.seek(0)
        unblocked_sites = []
        for line in file_content:
            if not any(website in line for website in Websites):
                host_file.write(line)
            else:
                unblocked_sites.append(line.strip().split()[1])
        host_file.truncate()

        if unblocked_sites:
            status_label.config(text=f"Website(s) unblocked: {', '.join(unblocked_sites)}", fg="green")
        else:
            status_label.config(text="No matching websites found.", fg="orange")

# Buttons Frame
buttons_frame = Frame(root)
buttons_frame.pack(pady=20)

# Block Button
block_btn = Button(buttons_frame, text="Block", command=Block, bg="red", fg="white", font=button_font, width=15, height=2)
block_btn.grid(row=0, column=0, padx=20)

# Unblock Button
unblock_btn = Button(buttons_frame, text="Unblock", command=Unblock, bg="green", fg="white", font=button_font, width=15, height=2)
unblock_btn.grid(row=0, column=1, padx=20)

# Footer
footer_label = Label(root, text="Manage your blocked websites easily.", font=("Arial", 10), fg="gray")
footer_label.pack(side=BOTTOM, pady=10)

mainloop()
