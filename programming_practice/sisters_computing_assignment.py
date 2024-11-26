# 1. Create a class to represent a Cat. This cat can be tame or wild, and it can be alive or dead. The cat also has a name, a certain number of hearts to represent its health, and a certain number of fish in its stomach 
    # Okay, Class = cat ---- Attributes = tame, wild, alive, dead, health, fish 

# 2. You can feed a cat a fish where its health goes up by 1 (maximum 4) and it becomes tame (50%). However, if a cat has more than 3 fish in the stomach, it will become dead and drop health to 0

# 3. You can hit a Cat and make its health go down by 1.5 times (minumum 0). Hitting a Cat, will always make it wild, and sometimes makes it dead when it has 0 hearts 
    # If you hit the cat, the health is going to go down by 1.5 times and every hit makes it wild. And if the cats hearts = 0, then it it'll be dead

# 4. At the end of every night, if a cat is a alive, there will 1 less fish in its stomach. If the number of fish drops to 0, the cat becomes wild. 
 
# 5. Dead cats cannot be fed and don't give gifts 


class Cat:
    def __init__(self, name, tame = False, wild = True, alive = True, dead = False, health= 4, fish = 0): #tame is default because we need to feed, alive is default because if we create a new cat instance, we assume its alive, which results for cat being dead is false. Max health of cat is 4, and no fish in stomach yet = 0)  
        self.name = name 
        self.tame = tame 
        self.wild = wild 
        self.alive = alive 
        self.dead = dead 
        self.health = health 
        self.fish = fish 

    def feed(self): # this says, if the cat is not alive, you wont be able to feed it. we raise an exception so that the program does not fail, rather gives feedback
        if not self.alive:
            raise Exception("Cat is dead, you cannot feed it")
            
    def hit(self):
        self.health -= 1.5 
        self.tame = False
        if self.health <=0:
            self.health = 0 
            self.alive = False

    def night(self):
        if not self.alive:
            return # if the cat is not alive, then do nothing 
        if self.alive:
            self.fish > 0 # if the cat is alive, there must be more an o fishes in stomach 
            self.fish -= 1
        if self.fish <= 0:
            self.tame = False # if the cat has no fish in stomach, it becomes wild so tame = false 

    def gift(self):
        if not self.alive:
            return f"{self.name} is dead and cannot give gifts" 
        if self.tame: 
            return #if cat is tamed do nothing 
        if self.tame and self.fish > 0:
            print(f"{self.name}: Left you a gift!") # If the cat is tamed and has more than 0 fish in stomach it will leave a gift 
    

    def __str__(self):
        if not self.alive:
            status = "DEAD" # if the cat is not alive, it is dead 
        if self.alive and self.tame == False:
            status = "WILD" # if the cat is alive and is not tamed, it is wild 
        if self.alive and not self.tame: # if the cat is alive and tamed, it is tamed 
            status = "TAMED"
        return f" Cat {self.name}: Status={status}, Health={self.health}, fish in stomach={self.fish}" # This returns a string representing the objects state 


#Koby = Cat(name ="Koby", tame= False, wild= True, alive = False, dead = True, health= 3, fish = 2)
#print(Koby.gift())
#print(Koby)

#koby = Cat(name="koby", tame=False, health=0, alive=False)-- object 1
#kylo = Cat(name="kylo", tame=True, health=3, fish=2) ------- object 2
#aiko = Cat(name="aiko", tame=True, health=1, fish=2 ) ------ object 3 