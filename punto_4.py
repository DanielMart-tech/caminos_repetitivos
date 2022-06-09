# variable to store the generation
generation = int(input("Please, indicate a generation: "))

# While loop to print the number of people in each generation
while generation >= 0:
    print(f"Total number of people up to {str(generation)} generation: {2**generation}")
    generation -= 1