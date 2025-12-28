"""
Authors: Alexander Bousman and Javan Hirwa
poker_gui.py
Project 11

This program makes the graphical user interface for the
implementation of a poker game, with the poker hand
calculations handled by the poker_calc.py file
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox, PhotoImage

from cards import Card, Deck
import poker_calc
import random
import os

class PokerGui(Tk):
    BET = 10
    JACKS = "JACKS"
    DEUCES = "DEUCES"
    def __init__(self):
        super().__init__()
        self.geometry("1200x450")
        #Default fonts for buttons and labels
        b_font = ("courier", 20)
        l_font = ("courier new", 20)

        #Dictionary for the stats displayed by the Stats button
        self.stats = {"Total Earnings": 0, "Total Hands": 0, "Max Cash": 0, "Total Games": 0}
        self.cash = 0
        self.ruleset = PokerGui.JACKS
        self.inverted = [False, False, False, False, False]

        #Code to set up the menubar at the top
        menu_bar = Menu(self, tearoff=False)
        gamemenu = Menu(menu_bar, tearoff=False)
        gamemenu.add_command(label = "New Game", command = self.new_game)
        gamemenu.add_command(label = "Exit", command = self.destroy)        #Destroy myself
        infomenu = Menu(menu_bar, tearoff=False)
        infomenu.add_command(label = "Statistics", command = self.stats_menu)
        infomenu.add_command(label = "Payout Table", command = self.payouts)
        menu_bar.add_cascade(menu=gamemenu, label = "Game")
        menu_bar.add_cascade(menu=infomenu, label = "Info")
        self.configure(menu=menu_bar)
        
        self.cashLabel = Label(self, text = "Cash: $" + str(self.cash), font = b_font)
        self.cashLabel.grid(row = 0, column = 0)

        self.rulesLabel = Label(self, text = "Ruleset: Jacks or Better", font = b_font)
        self.rulesLabel.grid(row = 0, column = 2, columnspan=2)

        #Example of an image label with a command bound to it
        self.label1 = Label(self, text = "")
        self.label1.grid(row = 1, column = 0)
        self.image1 = PhotoImage(file = "./card_images/blue_back.png")
        self.label1.configure(image = self.image1)
        self.label1.bind("<Button-1>", self.card1_click)

        self.label2 = Label(self, text = "")
        self.label2.grid(row = 1, column = 1)
        self.image2 = PhotoImage(file = "./card_images/blue_back.png")
        self.label2.configure(image = self.image1)
        self.label2.bind("<Button-1>", self.card2_click)

        self.label3 = Label(self, text = "")
        self.label3.grid(row = 1, column = 2)
        self.image3 = PhotoImage(file = "./card_images/blue_back.png")
        self.label3.configure(image = self.image1)
        self.label3.bind("<Button-1>", self.card3_click)

        self.label4 = Label(self, text = "")
        self.label4.grid(row = 1, column = 3)
        self.image4 = PhotoImage(file = "./card_images/blue_back.png")
        self.label4.configure(image = self.image1)
        self.label4.bind("<Button-1>", self.card4_click)

        self.label5 = Label(self, text = "")
        self.label5.grid(row = 1, column = 4)
        self.image5 = PhotoImage(file = "./card_images/blue_back.png")
        self.label5.configure(image = self.image1)
        self.label5.bind("<Button-1>", self.card5_click)

        self.button1 = Button(self, text = "New Game", font = l_font, command=self.new_game)
        self.button1.grid(row = 2, column = 0)
        self.button1.configure(height = 1, width = 10)

        self.button2 = Button(self, text = "New Hand", font = l_font, command=self.new_hand)
        self.button2.grid(row = 2, column = 1)
        self.button2.configure(height = 1, width = 10)
        self.button2.configure(state = "disabled")

        self.button3 = Button(self, text = "Draw!", font = l_font, command=self.draw)
        self.button3.grid(row = 2, column = 2)
        self.button3.configure(height = 1, width = 6)
        self.button3.configure(state = "disabled")
        
        self.button4 = Button(self, text = "Change Rules", font = l_font, command=self.changeRules)
        self.button4.grid(row = 2, column = 3)
        self.button4.configure(height = 1, width = 12)

        self.button5 = Button(self, text = "Cash Out", font = l_font, command=self.cashOut)
        self.button5.grid(row = 2, column = 4)
        self.button5.configure(height = 1, width = 10)
        self.button5.configure(state = "disabled")

    def card1_click(self, event):
        if self.inverted[0]:
            self.image1 = PhotoImage(file = "./card_images/" + self.hand[0].get_file_name())
            self.label1.configure(image = self.image1)
            self.inverted[0] = False
        else:
            self.image1 = PhotoImage(file = "./inverted_images/inverted_" + self.hand[0].get_file_name())
            self.label1.configure(image = self.image1)
            self.inverted[0] = True

    def card2_click(self, event):
        if self.inverted[1]:
            self.image2 = PhotoImage(file = "./card_images/" + self.hand[1].get_file_name())
            self.label2.configure(image = self.image2)
            self.inverted[1] = False
        else:
            self.image2 = PhotoImage(file = "./inverted_images/inverted_" + self.hand[1].get_file_name())
            self.label2.configure(image = self.image2)
            self.inverted[1] = True

    def card3_click(self, event):
        if self.inverted[2]:
            self.image3 = PhotoImage(file = "./card_images/" + self.hand[2].get_file_name())
            self.label3.configure(image = self.image3)
            self.inverted[2] = False
        else:
            self.image3 = PhotoImage(file = "./inverted_images/inverted_" + self.hand[2].get_file_name())
            self.label3.configure(image = self.image3)
            self.inverted[2] = True

    def card4_click(self, event):
        if self.inverted[3]:
            self.image4 = PhotoImage(file = "./card_images/" + self.hand[3].get_file_name())
            self.label4.configure(image = self.image4)
            self.inverted[3] = False
        else:
            self.image4 = PhotoImage(file = "./inverted_images/inverted_" + self.hand[3].get_file_name())
            self.label4.configure(image = self.image4)
            self.inverted[3] = True
    
    def card5_click(self, event):
        if self.inverted[4]:
            self.image5 = PhotoImage(file = "./card_images/" + self.hand[4].get_file_name())
            self.label5.configure(image = self.image5)
            self.inverted[4] = False
        else:
            self.image5 = PhotoImage(file = "./inverted_images/inverted_" + self.hand[4].get_file_name())
            self.label5.configure(image = self.image5)
            self.inverted[4] = True

    def new_game(self):
        print("We should start a new game!")
        self.cash = 100
        self.cashLabel.configure(text="Cash: $" + str(self.cash))
        self.deck = Deck()
        self.deck.shuffle()

        self.image1 = PhotoImage(file = "./card_images/blue_back.png")
        self.label1.configure(image = self.image1)
        self.image2 = PhotoImage(file = "./card_images/blue_back.png")
        self.label2.configure(image = self.image2)
        self.image3 = PhotoImage(file = "./card_images/blue_back.png")
        self.label3.configure(image = self.image3)
        self.image4 = PhotoImage(file = "./card_images/blue_back.png")
        self.label4.configure(image = self.image4)
        self.image5 = PhotoImage(file = "./card_images/blue_back.png")
        self.label5.configure(image = self.image5)
        self.button2.configure(state = "active")
        self.button3.configure(state = "active")
        self.button5.configure(state = "active")
        self.stats["Total Games"] += 1
        self.hand = []
    
    def new_hand(self):
        if self.cash == 0:
            messagebox.showerror(title = "NO CASH", message = "To keep playing, pay more cash")
            self.button2.configure(state = "disabled")
            self.button3.configure(state = "disabled")
        else:
            self.cash -= 10
            self.cashLabel.configure(text="Cash: $" + str(self.cash))
            self.hand = [self.deck.deal() for i in range(5)]

            self.image1 = PhotoImage(file = "./card_images/" + self.hand[0].get_file_name())
            self.label1.configure(image = self.image1)
            self.image2 = PhotoImage(file = "./card_images/" + self.hand[1].get_file_name())
            self.label2.configure(image = self.image2)
            self.image3 = PhotoImage(file = "./card_images/" + self.hand[2].get_file_name())
            self.label3.configure(image = self.image3)
            self.image4 = PhotoImage(file = "./card_images/" + self.hand[3].get_file_name())
            self.label4.configure(image = self.image4)
            self.image5 = PhotoImage(file = "./card_images/" + self.hand[4].get_file_name())
            self.label5.configure(image = self.image5)
            self.stats["Total Hands"] += 1
            self.button3.configure(state = "active")
    
    def draw(self):
        for i in range(len(self.hand)):
            if self.inverted[i] == True:
                self.hand[i] = self.deck.deal()
                self.inverted[i] = False
                if i == 0:
                    self.image1 = PhotoImage(file = "./card_images/" + self.hand[i].get_file_name())
                    self.label1.configure(image = self.image1)
                elif i == 1:
                    self.image2 = PhotoImage(file = "./card_images/" + self.hand[i].get_file_name())
                    self.label2.configure(image = self.image2)
                elif i == 2:
                    self.image3 = PhotoImage(file = "./card_images/" + self.hand[i].get_file_name())
                    self.label3.configure(image = self.image3)
                elif i == 3:
                    self.image4 = PhotoImage(file = "./card_images/" + self.hand[i].get_file_name())
                    self.label4.configure(image = self.image4)
                else:
                    self.image5 = PhotoImage(file = "./card_images/" + self.hand[i].get_file_name())
                    self.label5.configure(image = self.image5)
        
        self.earnings = poker_calc.calc_hand(self.hand, self.ruleset)
        if self.earnings[0] > 0:
            messagebox.showinfo(title = "Earned!", message = "You earned $" + str(10*self.earnings[0]) + " on this hand with a " + self.earnings[1] + "!")
            self.cash += 10*self.earnings[0]
            self.cashLabel.configure(text = "Cash: $" + str(self.cash))
        else:
            messagebox.showinfo(title = "Poor...", message = "You didn't earn any money on this hand...")
        
        self.button3.configure(state = "disabled")
        self.stats["Total Earnings"] += 10*self.earnings[0] - 10
    
    def changeRules(self):
        if self.ruleset == "JACKS":
            changeRules = messagebox.askquestion(title = "Change Rules?", message = "Currently the game is " + self.ruleset + " Do you want to change the rules to Deuces Wild? [This will end the game and start a new game.]")
            if changeRules == "yes":
                self.ruleset = "DEUCES"
                self.rulesLabel.configure(text = "Ruleset: Deuces Wild")
                self.new_game()
        elif self.ruleset == "DEUCES":
            changeRules = messagebox.askquestion(title = "Change Rules?", message = "Currently the game is " + self.ruleset + " Do you want to change the rules to Jacks or Better? [This will end the game and start a new game.]")
            if changeRules == "yes":
                self.ruleset = "JACKS"
                self.rulesLabel.configure(text = "Ruleset: Jacks or Better")
                self.new_game()
    
    def cashOut(self):
        if self.cash > self.stats["Max Cash"]:
            self.stats["Max Cash"] = self.cash
        self.cash = 0 
        self.cashLabel.configure(text = "Cash: $" + str(self.cash))
        self.button2.configure(state = "disabled")
        self.button3.configure(state = "disabled")
        self.button5.configure(state = "disabled")

    def payouts(self):
        payout = HowGui(self)
        payout.mainloop()
    
    def stats_menu(self):
        stats = StatsGui(self)
        stats.mainloop()

class HowGui(Toplevel):
    HAND_VALUES_JACKS = [("Four of a Kind", 25), ("Full House", 10), ("Flush", 7), ("Straight", 5), ("Three of a Kind", 3), ("Two Pairs", 2), ("One Pair\n(Jacks or Better)", 1)]
    HAND_VALUES_DEUCES = [("Four Deuces", 4000), ("Five of a Kind", 18), ("Straight Flush", 10), ("Four of a Kind", 6), ("Full House", 4), ("Flush", 2), ("Straight", 2), ("Three of a Kind", 1)]
    BG = 'gray'

    def __init__(self, base):
        super().__init__(base)      #The base window is the one below this window
        self.geometry("500x380")
        self.title("Hands")
        self.resizable(False, False)
        self.configure(bg=HowGui.BG)
        
        self.hands_row = 0
        self.rules = "Jacks"
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.table_frame = Frame(self, bg=HowGui.BG)
        tf = self.table_frame
        self.display_rules(tf)
        tf.grid(row = 0, column = 0)

        Button(self, text = "Other Rules", command=self.change_rules).place(relx=0.4, rely=0.9, relwidth=0.2, relheight=0.1)

        self.grab_set()
        base.wait_window(self)      #the base window can't do anything until we get rid of this How window

    def display_rules(self, tf):
        hands_row = self.hands_row
        curr_row = hands_row
        header_font = ('courier', 24)
        label_font = ("courier new", 20)

        Label(tf, text = "Hand", font = header_font, bg=HowGui.BG).grid(row = curr_row, column = 0)
        Label(tf, text = "Payout", font = header_font, bg=HowGui.BG).grid(row = curr_row, column = 1)
        curr_row+=1

        sep = ttk.Separator(tf)
        sep.grid(row = curr_row, column=0, columnspan=3, sticky='ew', ipadx=250)
        curr_row+=1

        if self.rules=="Jacks":
            hands = HowGui.HAND_VALUES_JACKS
        elif self.rules=="Deuce":
            hands = HowGui.HAND_VALUES_DEUCES

        for row, (name, mult) in enumerate(hands):
            tf.rowconfigure(curr_row+row, weight=1)
            Label(tf, text= f"{name:^20}", font = label_font, bg=HowGui.BG).grid(row = curr_row + row, column = 0)
            Label(tf, text= f"{mult:^6}", font = label_font, bg=HowGui.BG).grid(row = curr_row + row, column = 1)
        curr_row += row
    
    def change_rules(self):
        self.table_frame.destroy()
        self.table_frame = Frame(self, bg=HowGui.BG)
        self.table_frame.grid(row=0, column=0)
        if self.rules=="Jacks":
            self.rules="Deuce"
            self.display_rules(self.table_frame)
        else:
            self.rules="Jacks"
            self.display_rules(self.table_frame)

class StatsGui(Toplevel):
    def __init__(self, poker_gui):
        super().__init__(poker_gui)      #The poker_gui window is the one below this window
        self.geometry("400x350")
        self.title("Stats")
        self.resizable(False, False)

        header_font = ('courier', 24)
        label_font = ("courier new", 20)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        curr_row = 0
        Label(self, text = "Statistics", font = header_font).grid(row = curr_row, column = 0, columnspan=2)
        curr_row+=1

        sep = ttk.Separator(self)
        sep.grid(row = curr_row, column=0, columnspan=2, sticky='ew', ipadx=200)
        curr_row+=1

        for stat, val in poker_gui.stats.items():
            self.rowconfigure(curr_row, weight=1)
            Label(self, text= f"{stat}", font = label_font).grid(row = curr_row, column = 0)
            if int(val)<0:
                Label(self, text= f"{val}", font = label_font, fg = 'red').grid(row = curr_row, column = 1)
            else:
                Label(self, text= f"{val}", font = label_font, fg = 'green').grid(row = curr_row, column = 1)
            curr_row += 1

        self.grab_set()
        poker_gui.wait_window(self)      #the base window can't do anything until we get rid of this How window

if __name__ == "__main__":
    main_gui = PokerGui()
    main_gui.mainloop()
