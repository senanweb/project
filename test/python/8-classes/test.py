class phone:
    def __init__(self, name, model, price,status):
        self.name = name
        self.model = model
        self.price = price
        self.status = status
    #To access all for this we use introduce
    def introduce (self):
        print("Hi, I'm {} {}.".format(self.name, self.model))
    
    def model (self):
        model = random.randrange(1,3)
        if model == 1:
            print ("{} yes its good ".format(self.name))
        elif model == 2:
             print ("{} no its not good ".format(self.name))
samsung = phone ("samsung",  "g200", "200",status = True)
iphone = phone ("iphone", "ipad200", "400", status = False)


print("{} is my friend? {}".format(samsung.name, samsung.status))
print("{} is my friend? {}".format(iphone.name, iphone.status))
