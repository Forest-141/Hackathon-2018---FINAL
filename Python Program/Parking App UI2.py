import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk

def print_availability(output):
    file = open(r'D:\Desktop\Hackathon 2018 - FINAL\VS C Program\Hackathon\hackathon\output.txt', 'r')
    spaces = file.read()
    availability = int(spaces)
    output.delete(0.0, tk.END)
    string = 'There are ' + str(availability) + ' spots available.'
    output.insert(tk.END, string)

ticketurl = 'https://parking.wsu.edu/ticket.php'
dailyurl = 'https://parking.wsu.edu/permit.php?cmd=new'
eventurl = 'https://parking.wsu.edu/permit.php?cmd=new_events'
annualurl = 'https://parking.wsu.edu/permit.php?cmd=new_login'

def open_url(url):
    webbrowser.open(url)

LARGE_FONT= ("Verdana", 12)

class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1, minsize = 300)
        container.grid_columnconfigure(0, weight=1, minsize = 750)
        self.frames = {}

        tk.Tk.wm_title(self, "WSU Parking App")

        self.frames['StartPage'] = StartPage(container, self)
        self.frames['Main_Menu'] = Main_Menu(container, self)
        self.frames['Parking_Map'] = Parking_Map(container, self)
        self.frames['Permit_Options'] = Permit_Options(container, self)
        self.frames['Green1'] = Green1(container, self)
        self.frames['Green4'] = Green4(container, self)
        self.frames['Orange3'] = Orange3(container, self)

        self.show_frame('StartPage', 'Parking_Map')


    def show_frame(self, cont, cont2):
        self.frames[cont].grid(column = 0, row = 0)
        self.frames[cont2].grid_forget()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, bg = 'red3')
        self.grid_rowconfigure(6, weight=1, minsize = 191)
        self.grid_columnconfigure(0, weight=1, minsize = 750)
        label = tk.Label(self, text="Please Log-in using your WSU information", font=LARGE_FONT)
        label.grid(row = 1, pady=10,padx=10)

        photo = tk.PhotoImage(file = r'D:\Desktop\Hackathon 2018 - FINAL\Python Program\cougar.png')
        label2 = tk.Label(self, image = photo)
        label2.photo = photo
        label2.grid(row = 0, padx = 10, pady = 10)

        username = tk.Label(self, text = "Email:")
        username.grid(row = 2, padx = 10, pady = 10)
        textentry = tk.Entry(self, width = 20, bg="white")
        textentry.grid(row = 3, padx = 10, pady=10)

        password = tk.Label(self, text="Password:")
        password.grid(row = 4, padx = 10, pady=10)
        textentry2 = tk.Entry(self, width = 20, bg = "white")
        textentry2.grid(row = 5, padx = 10, pady = 10)

        button = ttk.Button(self, text ="Enter",
                            command = lambda: controller.show_frame('Main_Menu', 'StartPage'))
        button.grid(row = 6, padx = 10, pady = 10)

class Main_Menu(tk.Frame):
    def __init__(self, parent, controller): #initializes class self
        tk.Frame.__init__(self,parent, bg = 'red3', width = 300, height = 300)
        self.grid_rowconfigure(4, weight=1, minsize = 334)
        self.grid_columnconfigure(0, weight=1, minsize = 750)
        label = tk.Label(self, text="Select Option: ", font=LARGE_FONT)
        label.grid(row = 0, padx = 10, pady = 10)

        button = ttk.Button(self, text="See Parking Availability",
                            command=lambda: controller.show_frame('Parking_Map', 'Main_Menu'))
        button.grid(row = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text="Purchase Parking Permit",
                            command=lambda: controller.show_frame('Permit_Options', 'Main_Menu'))
        button2.grid(row = 2, padx = 10, pady = 10)
        
        button3 = ttk.Button(self, text="Pay Parking Ticket",
                            command=lambda: open_url('ticketurl'))
        button3.grid(row = 3, padx = 10, pady = 10)
        

class Parking_Map(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = 'red3')
        self.grid_rowconfigure(6, weight=1, minsize = 222)
        self.grid_columnconfigure(0, weight=1, minsize = 750)
        photo = tk.PhotoImage(file = r'D:\Desktop\Hackathon 2018 - FINAL\Python Program\parkingmap.png')
        label2 = tk.Label(self, image = photo)
        label2.photo = photo
        label2.grid(row = 0, padx = 10, pady = 10)

        label = tk.Label(self, text="Select Parking Lot: ", font=LARGE_FONT)
        label.grid(row = 1, pady=10,padx=10)

        button = ttk.Button(self, text="Green 1",
                            command=lambda: controller.show_frame('Green1', 'Parking_Map'))
        button.grid(row = 2, padx = 10, pady = 10)

        button2 = ttk.Button(self, text="Green 4",
                            command=lambda: controller.show_frame('Green4', 'Parking_Map'))
        button2.grid(row = 3, padx = 10, pady = 10)
        
        button3 = ttk.Button(self, text="Orange 3",
                            command=lambda: controller.show_frame('Orange3', 'Parking_Map'))
        button3.grid(row = 4, padx = 10, pady = 10)
                
        button4 = ttk.Button(self, text="Back to Main Menu",
                            command=lambda: controller.show_frame('Main_Menu', 'Parking_Map'))
        button4.grid(row = 5, padx = 10, pady = 10)

class Permit_Options(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = 'red3')
        self.grid_rowconfigure(5, weight=1, minsize = 267)
        self.grid_columnconfigure(0, weight=1, minsize = 750)
        label = tk.Label(self, text="Select Parking Lot: ", font=LARGE_FONT)
        label.grid(row = 0, pady=10,padx=10)

        button = ttk.Button(self, text="Daily Permit",
                            command=lambda: open_url(dailyurl))
        button.grid(row = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text="Event/RV Permits",
                            command=lambda: open_url(eventurl))
        button2.grid(row = 2, padx = 10, pady = 10)
        
        button3 = ttk.Button(self, text="Annual Permit",
                            command=lambda: open_url(annualurl))
        button3.grid(row = 3, padx = 10, pady = 10)
                
        button4 = ttk.Button(self, text="Back to Main Menu",
                            command=lambda: controller.show_frame('Main_Menu', 'Permit_Options'))
        button4.grid(row = 4, padx = 10, pady = 10)

class Green1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = 'red3')
        self.grid_rowconfigure(4, weight=1, minsize = 334)
        self.grid_columnconfigure(0, weight=1, minsize = 750)
        label = tk.Label(self, text="Availability: ", font=LARGE_FONT)
        label.grid(row = 0, pady=10,padx=10)

        output = tk.Text(self, width = 100, height = 25, wrap = tk.WORD, background = "red3")
        output.grid(row = 1, padx = 10, pady = 10)

        button = ttk.Button(self, text="Show Availability",
                            command=lambda: print_availability(output))
        button.grid(row = 2, padx = 10, pady = 10)

        button = ttk.Button(self, text="Back to Lot Options",
                            command=lambda: controller.show_frame('Parking_Map', 'Green1'))
        button.grid(row = 3, padx = 10, pady = 10)

class Green4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = 'red3')
        self.grid_rowconfigure(4, weight=1, minsize = 334)
        self.grid_columnconfigure(0, weight=1, minsize = 750)
        label = tk.Label(self, text="Availability: ", font=LARGE_FONT)
        label.grid(row = 0, pady=10,padx=10)

        output = tk.Text(self, width = 100, height = 25, wrap = tk.WORD, background = "red3")
        output.grid(row = 1, padx = 10, pady = 10)

        button = ttk.Button(self, text="Show Availability",
                            command=lambda: print_availability(output))
        button.grid(row = 2, padx = 10, pady = 10)

        button = ttk.Button(self, text="Back to Lot Options",
                            command=lambda: controller.show_frame('Parking_Map', 'Green4'))
        button.grid(row = 3, padx = 10, pady = 10)

class Orange3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = 'red3')
        self.grid_rowconfigure(4, weight=1, minsize = 334)
        self.grid_columnconfigure(0, weight=1, minsize = 750)
        label = tk.Label(self, text="Availability: ", font=LARGE_FONT)
        label.grid(row = 0, pady=10,padx=10)

        output = tk.Text(self, width = 100, height = 25, wrap = tk.WORD, background = "red3")
        output.grid(row = 1, padx = 10, pady = 10)

        button = ttk.Button(self, text="Show Availability",
                            command=lambda: print_availability(output))
        button.grid(row = 2, padx = 10, pady = 10)

        button = ttk.Button(self, text="Back to Lot Options",
                            command=lambda: controller.show_frame('Parking_Map', 'Orange3'))
        button.grid(row = 3, padx = 10, pady = 10)


app = SeaofBTCapp()
app.mainloop()
