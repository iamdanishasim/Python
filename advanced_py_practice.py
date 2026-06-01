#Practice
# Practicing Args and Kwargs 
def Decorate(func):
    def wrapper(num):
        print("Welcome Stranger")
        func(num)
        print("Thanks for Using our Services")
    return wrapper  

@Decorate
def evenOrNot(a):
    if a % 2 == 0:
        print("The Number is Even")
    else:
        print("The Number is Odd")

evenOrNot(2)


# Practicing List comprehension 
list1 = [i for i in range(21) if i % 2 == 0 ]
print(list1)


#Lambda 
answer = lambda num : "Even" if num % 2 == 0 else "pdd"
num_input = int(input("Please Enter a Number ")) 
print(answer(num_input))

#map & Filter 
list2 = [1,2,3,4,5]

result = map(lambda x : x**2 ,list2)
print(list(result))

secondResult = filter(lambda x : True if x%2 == 0 else False, list2)

print(list(secondResult))
