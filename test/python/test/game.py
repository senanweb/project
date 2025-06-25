class game:
    def __init__(self, name,health,status):
        self.name = name
        self.health = health
        self.status = status
    
    # know the status
    def status_change(self):
        self.health = (self.health - 25)
        if self.health == 100:
            print("{} is fully healthy!".format(self.name))
        elif self.health == 85:
            print("{} feels tired.".format(self.name))
        elif self.health == 75:
            print("{} feels unwell.".format(self.name))
        elif self.health <= 50:
            print("{} goes to the doctor.".format(self.name))
        else:
            print("{} is Good.".format(self.name))
    
    # Here to Know health
    def introduce(self):
        print("Hi, I'm {} My Healthy is {}.".format(self.name, self.health)) 

# input
Nadom = game ("Nadom",95, status = True)
Sinan = game ("Sinan",85, status = False)
Omar = game ("Omar",75, status = True)

print("{} is my friend? {}".format(Nadom.name, Nadom.status))
print("{} is my friend? {}".format(Sinan.name, Sinan.status))
print("{} is my friend? {}".format(Omar.name, Omar.status))

# Here to knew healthy and status
Nadom.introduce()
Nadom.status_change()

#inheritance example
class Enemy(game):
    def __init__(self, weapon, name,health,status):
        super().__init__(name,health,status)
        self.weapon = weapon
    #=====================================
    # Here to Know health
    def introduce(self):
        print("You are my mortal enemy!!!")
    
    # weapon
    def hurt(self, other):
        if self.weapon == 'rod':
            other.health -= 30
        elif self.weapon == 'colt':
            other.health -= 40
        elif self.weapon == 'shootgun':
            other.health -= 50
        print(other.health)
    #===============================================
    # insult
    def insult(self, other):
        if other.health <= 20:
            print("{}, you are tired and weak".format(other.name))

    # steal
    def steal(self, other):
        print("ha ha ha, {}, I have your stuff!".format(other.name))
        if other.status == True:
            other.status = False

    

Alex = Enemy(input("your Weapon. "),"Alex",20,status=False)
Alex.hurt(Nadom)
Alex.insult(Sinan)
Alex.insult(Omar)
Alex.steal(Sinan)