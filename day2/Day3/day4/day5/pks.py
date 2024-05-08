# print("hello world")
# print("this is another line")
# print("testing")

# vara = 10
# print(vara)

# a = 10
# print(type(a))

# b = 10.5
# print(type(b))

# c = True
# print(type(c))

# d = "hello world"
# print(type(d))

# e = None
# print(type(e))

# a = 10
# b = 30
# c = a+b
# print(c)

# a = 40
# b= 30
# c = a-b
# print(c)

# a = 12
# b = 7
# c = a*b
# print(c)

# a = 30
# b= 5
# print(a/b)

# a = 30 
# b = 5
# print(a//b)

# a = 30
# print("hello world", a )

# a = 30
# b = 4
# print(a>b)

# print(a<b)

# print(a==b)

# a = 34
# b= 45
# if a>b:
#     print("a is greater")
# else:
#     print("b is greater")
    
# age = 10
# if age>18:
#     print("you are an adult")
# else:
#     print("you are a minor")

# age = 60
# if age>=18 and age<=40:
#     print("you are an  adult")
# elif age>40:
#     print("you are a senior")
# else:
#     print("you are a minor")

# degree ="BSC"
# if degree == "ba" and degree == "bca":
#     print("you are eligible")
# else:
#     print("you are not eligible")

# list1 = []
# print(type(list1))

# tup1 = ()
# print(type(tup1))

list1 = [2, 33, 4, 5, 6, 7, 33, 33, ['pradeep', 'ankit', 'anuj'], 34]
# print(list1)

# tuple1 = (2, 3, 4, 5, 6, 7, 33, 33, ['pradeep', 'ankit', 'anuj'], 34)
# print(tuple1)

# list1.append(45)
# print(list1)

# list1.remove(5)
# print(list1)

# list1.insert(4, "hello world")
# print(list1)

# list1.reverse()
# print(list1)

# list1[1]
# print(list1)

# def func1(func):
#     def inner_function():
#         print("i am decorated")
#         func()
        
#     inner_function()
    
#     return inner_function

# @ func1
# def func2():
#     print("i am not decorated")
    
# def add(x, y):
#     return x + y

# def calculate(func, x, y):
#     return func(x, y)

# result = calculate(add, 4, 6)
# print(result)  # prints 10
# func 2

def printBoard(xstate, zstate):
    print(f"0 | 1 | 2 ")
    print(f"--|---|---")
    print(f"3 | 4 | 5 ")
    print(f"--|---|---")
    print(f"6 | 7 | 8 ")
    pass
    
if __name__ == "__main__":
    xstate = [0, 0, 0, 0, 0, 0, 0, 0]
    zstate = [0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # for x and 0 for 0
    print("Wwlcome to Tic Tac Toe")
    while(True):
        printBoard(xstate, zstate)
        if (turn == 1):
           print("X's chance")
           value = int(input("plese enter a value"))
           xstate[value] = 1
        else:
            print("X's chance")
            value = int(input("plese enter a value"))
            zstate[value] = 1
        
        break
    