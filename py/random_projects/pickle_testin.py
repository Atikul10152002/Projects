from PIL import Image, ImageDraw
from random import choice, randint
import pickle

class cool():
    def __init__(self,pizza, meat, sause):
        self.pizza = pizza
        self.meat = meat
        self.sause = sause
    
    def printi(self):
        print("We want",self.pizza,self.meat, "pizza; sause=", self.sause)
    
pizza = cool("cheese","chicken","yes")
with open("cool.pickle","wb") as f:
    pickle.dump(pizza, f)

with open("cool.pickle","rb") as f:
    run = pickle.load(f)
run.printi()