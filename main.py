
print("Katie")
print(19)

pet_name = "Logan"
pet_age = 11

print(pet_name)
print(pet_age)

total_price = 0

among_us_price = 12
elden_ring_price = 60
project_grove_price = 20

us_tax = 1.14

total_price += (among_us_price + elden_ring_price + project_grove_price)
total_price *= us_tax
print("Your total is: " + str(total_price))

name = "Katie"
age = 19
height = 1.72

print("Your name is %s, your age is %d and you are %.2f cm tall" % (name, age, height))
print("Your name is {}, your age is {} and you are {:.2f} cm tall" .format(name, age, height))

number = int(input("Give me a number: "))

if number < 10:
    print("That is a small number.")

elif number <= 100:
    print("Still too small.")

else:
    print("That is a big number.")

if number % 2 == 0:
    print("Even")

else:
    print("Odd")