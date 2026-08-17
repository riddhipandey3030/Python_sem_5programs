# Create a set of fruits consisting of name of 10 fruits.Create another set of summer fruits that 
# consist of data fruits that are available only in the summer season. create another set winter 
# fruits consisting 5 fruits of only winter season. Now perform the following operation on these sets
# 1. Print the name of all fruits in the three sets 
# 2. print the name of those fruits that are present in both summer and winter fruits 
# 3. Print the name of the fruits that are present only in summer fruits but not in fruits.
#--------------------------------------------------------------------------------------------------

fruits = {"Apple", "Mango", "Banana", "kiwi", "Grapes","Guava", "Papaya", "Watermelon", "Pineapple", "dragonfruit"}
summer_fruits = {"Mango", "Watermelon", "Papaya", "Litchi", "Muskmelon"}
winter_fruits = {"Apple", "kiwi", "Guava", "Strawberry", "dragonfruit"}

# 1. Print all fruits in 3 sets
print("Fruits:", fruits)
print("Summer Fruits:", summer_fruits)
print("Winter Fruits:", winter_fruits)

# 2. Print fruits present in both winter fruits and summer_fruits
print("Fruits present in both:")
for fruit in summer_fruits:
    if fruit in winter_fruits:
        print(fruit)

# 3. Print fruits present only in summer_fruits but not in fruits
print("Summer fruits not present in fruits:")
for fruit in summer_fruits:
    if fruit not in fruits:
        print(fruit)
 