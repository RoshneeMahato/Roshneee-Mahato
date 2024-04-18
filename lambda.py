def make_group(person1, person2):
    group = [person1, person2]
    return group

make_group = lambda person1, person2: [person1, person2]

#create object
person1 = "Ravia"
person2 = "Roshnee"

#calling the function
print(f"Group 1: {make_group(person1, person2)}")
group2 = make_group("somebody, anotherbody")
print(f"Group 2: {group2}")
group3 = make_group("Ravia, Roshnee")
print(f"group 3: group")

shopping_cart = ["pineapple", "watermelon"]
shopping_cart.appened("chatmasala")
print("shopping_cart")
