import tkinter as tk
import tkinter.font as font
import random, pyperclip


the_window = tk.Tk()
the_window.title("Password Generator")
class app(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.font = font.Font(family="Consolas")
        self.letter_option = tk.IntVar()
        self.number_option = tk.IntVar()
        self.symbol_option = tk.IntVar()
        self.create_widgets()
    def create_widgets(self):
        #The label containing the password
        self.the_label = tk.Label(self, text="Hello World", width=50)
        self.the_label["font"] = self.font
        self.the_label.grid(row=0, column=0)
        self.strength_label = tk.Label(self, text="Password Strength: ", width=25)
        self.strength_label["font"] = self.font
        self.strength_label.grid(row=0, column=2)
        #The slider to determine the length of the password
        self.length_slider = tk.Scale(self, from_=5, to=50, orient="horizontal", command=self.generate_password, length=450)
        self.length_slider.grid(row=1, column=0)
        self.length_slider["font"] = self.font
        self.length_slider["label"] = "Length"
        #Initialize the Checkboxes to let the user customize their password
        self.letter_check = tk.Checkbutton(self, text="Letters", var=self.letter_option)
        self.letter_check.select()
        self.letter_check["font"] = self.font
        self.letter_check.grid(row=2, column=0)
        self.number_check = tk.Checkbutton(self, text="Numbers", var=self.number_option)
        self.number_check["font"] = self.font
        self.number_check.grid(row=2, column=1)
        self.number_check.select()
        self.symbol_check = tk.Checkbutton(self, text="Symbols", var=self.symbol_option)
        self.symbol_check["font"] = self.font
        self.symbol_check.grid(row=2, column=2)
        self.symbol_check.select()
        #Refresh button simply changes the Password
        self.refresh_button = tk.Button(self, text="Refresh", command=self.generate_password)
        self.refresh_button["font"] = self.font
        self.refresh_button.grid(row=0, column=1)
        #The copy button copies the value of the_label to your clipboard
        self.copy_button = tk.Button(self, text="Copy", command=self.copy)
        self.copy_button["font"] = self.font
        self.copy_button.grid(row=3, column=0)
        #The quit button simply terminates the program
        self.quit_button = tk.Button(self, text="Quit", command=self.master.destroy)
        self.quit_button["font"] = self.font
        self.quit_button.grid(row=3, column=1)

    def copy(self):
        #This copies the password to your clipboard
        pyperclip.copy(self.the_label.cget("text"))
        print("Text copied to the clipboard")
    def generate_password(self, value=None):
        if value == None:
            value = self.length_slider.get()

        password = ""
        #The options will be set in a tuple with each checkbox having a 1 for on and 0 for off
        options = (self.letter_option.get(), self.number_option.get(), self.symbol_option.get())
        #This dictionary determines which characters can be included
        options_dict = {
        (0,0,0):[], #No options selected
        (1,0,0):[{"lower":65, "upper":90},{"lower":97, "upper":122}], #Letters only
        (0,1,0):[{"lower":48, "upper":57}], #Numbers only
        (0,0,1):[{"lower":33, "upper":47}, {"lower":58, "upper":64}, {"lower":91, "upper":96}, {"lower":123, "upper":126}], #Symbols only
        (1,1,0):[{"lower":48, "upper":57},{"lower":65, "upper":90},{"lower":97, "upper":122}], #Letters and Numbers
        (1,0,1):[{"lower":65, "upper":90},{"lower":97, "upper":122},{"lower":33, "upper":47},{"lower":58, "upper":64}, {"lower":91, "upper":96}, {"lower":123, "upper":126}], #Letters and Symbols
        (0,1,1):[{"lower":33, "upper":64}, {"lower":91, "upper":96}, {"lower":123, "upper":126}], #Numbers and Symbols only
        (1,1,1):[{"lower":33, "upper":126}] #All character types
        }
        value = int(value)
        char_list = options_dict[options]
        if len(char_list) == 0:
            #Change the label to tell the user to select an option
            self.length_slider["label"] = "Please select one of the options"
        else:
            #Change the label to Length
            self.length_slider["label"] = "Length"
            for i in range(value):
                #Make the password
                index_select = random.randint(0, len(char_list)-1)
                the_letter = chr(random.randint(char_list[index_select]["lower"], char_list[index_select]["upper"]))
                password = password + the_letter
            self.the_label.config(text=password)
            #Change the strength label to show the user the rough strength of their password
            if value <= 10:
                self.strength_label.config(text="Password Strength: Weak", bg="red", fg="white")
            elif (value > 10 and value < 20) or options == (0,1,0) or options == (1,0,0):
                self.strength_label.config(text="Password Strength: Medium", bg="yellow", fg="black")
            else:
                self.strength_label.config(text="Password Strength: Strong", bg="green", fg="white")


the_app = app(master=the_window)
the_window.mainloop()
