#course: Object-oriented programming, year 2, semester 1
#academic year: 2020-21
#author: B. Schoen-Phelan
#date: 02-10-2020
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: "+ message)

        #
        # Enter your own print statements below:
        print("hello world")
        print("this is week 2 of python")

        #

        # print only first and last of the sentence:
        my_string = "Klaud"
        print(my_string[0:6:4])


        # use slice notation:
        my_string2 ="Hello Guys"
        print(my_string2[6:-1])

        # escaping a character:
        print("He said 'That\'s fantasic!'")

# find all a's in the input word and count how many there are:
        print("this is a string".find('a'))

        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():


    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out:
        my_list = [message]
        print(my_list)


        # append a new element to the list and print:
        my_list.append("new")
        print(my_list)

        # remove from the list in 3 ways:
        my_list.remove("new")
        print(my_list)

        # check if the word cake is in your input list:
        if "cake" in my_list:
            print("cake is in your list")
        else:
            print("cake is NOT in your list")


        # reverse the items in the list and print:
        my_list.append("small")
        my_list.reverse()
        print(my_list)

        # reverse the list with the slicing trick:
        print(my_list[::-1])

        # print the list 3 times by using multiplication:
        print(my_list * 3)


tas = Types_and_Strings()
#tas.play_with_strings()
tas.play_with_lists()

