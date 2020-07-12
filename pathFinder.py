import tkinter
from tkinter import *

class PathFinder :

    def __init__(self,n):
        self.win = Tk()
        self.grid_size = n
        self.nodes = {}
        self.visited = {}
        self.buttons = []
        self.source = None
        self.destination = None
    
    def prepareNodes(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                connections = []
                if i-1 >= 0 :
                    connections.append(self.grid_size*(i-1)+j)
                if i+1 < self.grid_size :
                    connections.append(self.grid_size*(i+1)+j)
                if j-1 >= 0 :
                    connections.append(self.grid_size*i + (j-1))
                if j+1 < self.grid_size :
                    connections.append(self.grid_size*i + (j+1))

                self.nodes[self.grid_size*i + j] = connections

    def createLayout(self):
        for i in range(self.grid_size):
            buttonRow = []
            for j in range(self.grid_size):
                b = Button(self.win, text = "", bg = '#888A85')
                buttonRow.append(b)
                buttonRow[j].configure(command = lambda button = buttonRow[j] : self.change(button))
                buttonRow[j].grid(row = i, column = j)
            self.buttons.append(buttonRow)



    def change(self, button):
        if self.source == None:
            self.source = button
            button['bg'] = '#73D216'
        elif self.destination == None:
            self.destination = button
            button['bg'] = '#EDD400'

        else:
            if button['bg'] == '#888A85':
                button['bg'] = '#000000'
            elif button['bg'] == '#000000':
                button['bg'] = '#888A85'
        

if __name__ == "__main__":
    p = PathFinder(4)
    p.createLayout()
    b = Button(p.win,text = "go")
    b.grid(row = p.grid_size+3, column = 3)
    p.win.mainloop()




