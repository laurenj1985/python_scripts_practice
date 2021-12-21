#using counter and tuple to number the output of the script

farm_animals= ('goat', 'horse', 'chicken', 'cow', 'dog')

counter = 0

for animal in farm_animals:
    counter = counter + 1
    sentence = str(counter) + " " + animal + " is safe in our farm!"
    print(sentence)
