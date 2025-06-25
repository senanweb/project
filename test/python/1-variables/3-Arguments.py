def test(name, age=0, city="baghdad"): #parameter
    print ("My name is {}, and im {} old, i life in {}".format(name, age, city))
    #print("{} is {} years old, from {}".format(name, age, city))
test (input("your Name. "), int(input("your AGE. ")), input("your City. "))    #Arguments
#=========================================
def test1(name):
    print ("hi {}".format(name))
test1(input("your Name. "))