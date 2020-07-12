import time
import tkinter
from tkinter import *

n = 10

class PathFinder :

    def __init__(self,n):
        self.clear(n)

    def clear(self, n):
        self.win = Tk()
        self.grid_Layout = Frame(self.win, padx = 20, pady = 20)
        self.operations_layout = Frame(self.win, padx = 20, pady = 20)
        self.grid_size = n
        self.nodes = dict()
        self.visited = dict()
        self.buttons = []
        self.source = None
        self.destination = None
        self.launch = None
        self.path = []
        self.prepareNodes()
    
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
                self.visited[self.grid_size*i + j] = False
                

    def createLayout(self):
        for i in range(self.grid_size):
            buttonRow = []
            for j in range(self.grid_size):
                b = Button(self.grid_Layout, text = "", bg = '#888A85')
                buttonRow.append(b)
                buttonRow[j].configure(command = lambda r = i, c = j : self.change(r, c))
                buttonRow[j].grid(row = i, column = j)
            self.buttons.append(buttonRow)
        self.grid_Layout.grid(row = 0, column = 0)
        self.setOperations()
    
    def setOperations(self):
        self.launch = Button(self.operations_layout, text = "Go", command= lambda : [self.find(self.source),self.show()])
        self.launch.grid(row = 0, column = 0)
        self.operations_layout.grid(row = 1, column = 0)

    def change(self, i, j):
        if self.source == None:
            self.source = self.grid_size*i + j
            self.buttons[i][j]['bg'] = '#73D216'
        elif self.destination == None:
            self.destination = self.grid_size*i + j
            self.buttons[i][j]['bg'] = '#EDD400'

        else:
            if self.buttons[i][j]['bg'] == '#888A85':
                self.buttons[i][j]['bg'] = '#000000'
            elif self.buttons[i][j]['bg'] == '#000000':
                self.buttons[i][j]['bg'] = '#888A85'

    def find(self,curr):
        self.visited[curr] = True
        for node in self.nodes[curr]:
            if not self.visited[node] :
                self.visited[node] = True
                if node == self.destination :
                    return True
                if self.find(node):
                    self.path.append(node)
                    return True
        return False

    def show(self):
        l = self.path[::-1]
        for index in l:
            i = index//self.grid_size
            j = index % self.grid_size
            self.buttons[i][j].configure(bg = 'white')
            time.sleep(0.3)
            self.win.update()
        

def toGrid(n):
    n = int(n)
    pf = PathFinder(n)
    pf.createLayout()
    pf.win.mainloop()
    print(pf.path)

if __name__ == "__main__":
    popup = Tk()
    Label(popup,text = "Enter grid size", padx = 10, pady = 10 ).pack()
    e = Entry(popup)
    e.pack()
    b = Button(popup, text='create', command= lambda e=e ,popup = popup:[popup.quit(),toGrid(e.get())])
    b.pack()
    popup.mainloop()






