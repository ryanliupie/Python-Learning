from Cat import Cat # from Cat = 'Cat.py' and we since we need the class, we 'import Cat' IMPORTANT!! WE NEED TO CREATE AN __INIT__.PY file before we can import
# This is because python doesn't know that 'programming_practice' is a package. Therefore, the empty __init__ file says to python "hey this folder 'programming_practice' is a package, so look inside for the modules like Cat..py"

# The assignment said to create 3 different cats so we will do that. These different cats represent objects of the Cat class or instances of that class

koby = Cat(name="koby", tame=False, health=0, alive=False) #object 1
kylo = Cat(name="kylo", tame=True, health=3, fish=2) #object 2
aiko = Cat(name="aiko", tame=True, health=1, fish=2 ) #object 3 

# Fill the rest in