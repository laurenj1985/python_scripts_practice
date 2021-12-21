#get the remainder of the number that is divided in the solution and state what the remainder is in a sentence

def remainder (random_number = 0):
    return "The remainder is " + str(random_number % 3) + "!"


solution = remainder(29)

print(solution)
