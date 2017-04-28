"""This is the entry point of the program."""


def highest_number_cubed(limit):
    count = 0
    cubed_number = 0
    while cubed_number <= limit:
        cubed_number = count**3
        if cubed_number >  limit:
            return count - 1
        else:
            count = count + 1
        
