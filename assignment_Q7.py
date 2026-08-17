# Text="Python Programming". Consider the given string and perform the following operations on the string
#1. Display Python
#2. Display Programming 
#3. Find whether Java is present in the string or not,if not then include Java in between Python and Programming
#4. find the length of the new string
#5. Count the number of words in the string
#6. Capitalize each word in the string 
#7. Remove all the spaces and print the string
#8. Print the frequency of 'A','P','R','M'.
#---------------------------------------------------------------------------------------------

text = "Python Programming"
# a) Display Python
print("First word:", text.split()[0])
# b) Display Programming
print("Second word:", text.split()[1])
# c) Check whether Java is present
if "Java" in text:
    print("Java is present")
else:
    print("Java is not present")

    # Include Java between Python and Programming
    text = text.replace("Programming", "Java Programming")

print("New string:", text)
# d) Find the length of the new string
print("Length of new string:", len(text))
# e) Count the number of vowels
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)


# f) Capitalize each word
print("Each word capitalized:", text.title())


# g) Remove all spaces
no_space = text.replace(" ", "")

print("String without spaces:", no_space)


# h) Find frequency of A, P, R and M in capital letters
print("Frequency of A:", text.upper().count("A"))
print("Frequency of P:", text.upper().count("P"))
print("Frequency of R:", text.upper().count("R"))
print("Frequency of M:", text.upper().count("M")) 