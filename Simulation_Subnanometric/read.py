import os
import numpy as np
from ase.io import read
from ase.io import write

class fileCheck:
    def __init__(self,file):
        if file[-3:] != 'xyz':
            temp = read(file,index=':')
            write("temp.xyz",temp)
            file = "temp.xyz"

        g = open(file,"r")
        self.content = g.readlines()
        self.numberofatoms = int(int(self.content[0].split()[0]))
        self.numberofrows = int(len(self.content)/(self.numberofatoms+2))

        print("Atoms per frame: %d" %self.numberofatoms)
        print("Frames in file: %d" %self.numberofrows)

        if file=="temp.xyz":
            os.remove(file)

class openStruct:
    def __init__(self,file,start=None,last=None):
        if file[-3:] != 'xyz':
            temp = read(file,index=':')
            write("temp.xyz",temp)
            file = "temp.xyz"

        g = open(file,"r")
        self.content = g.readlines()
        self.numberofatoms = int(int(self.content[0].split()[0]))
        self.numberofrows = int(len(self.content)/(self.numberofatoms+2))
        allcoordinates = []
        if start==None:
            start = 0
        if last==None:
            last = self.numberofrows
        for i in range(start,last):
            coordinates = []
            for j in range(i*(self.numberofatoms+2)+2,i*(self.numberofatoms+2)+self.numberofatoms+2):
                coordinates.append([self.content[j].split()[0],float(self.content[j].split()[1]),float(self.content[j].split()[2]),float(self.content[j].split()[3])])
            allcoordinates.append(coordinates)
        self.coordinates = allcoordinates

        if file=="temp.xyz":
            os.remove(file)