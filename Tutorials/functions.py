# Functions: input, parameter
def make_shirt():
    user_input = input("Enter the size and text on the shirt: ")
    print("The size of the shirt and the text written on it is " + user_input)


make_shirt()


# parameter
def make_shirt(size, colour):
    print("The size of the shirt is size " + size + "," + "and the colour is " + colour)


make_shirt('30', 'red')




