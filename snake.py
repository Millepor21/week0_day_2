# x=5
# print(min(6,9))
# some_list=[6,7,8,43]
# def func(name):
#     print(name)
# USE CTRL + / TO COMMENT OUT A LINE OR MULTIPLE LINES


this_is_an_int = 5
this_is_a_float = 5.0
print(type(this_is_an_int))
print(type(this_is_a_float))
div= this_is_an_int / 1
print(type(div))

#math operators

# add +
# subtract -
# multiply *
# divide /
# floor divide //
# modulo %
# exponents **

sum1 = 4+5
sub1 = 5-4
prod = 4*5
div1 = 25/5
floor_div = 7//3
rem = 7%3
exp = 5**2
print(sum1, sub1, prod, div1, floor_div, rem, exp)
print(int(div1))
print(int(5.9))

# whatevernum % 2 == 0: is the function for odd or even

# STRINGS
st1 = 'this is a string'
st2 = "so's this" # alternatively we could use an escape character here:
st3 = 'so\'s this'
print(st2, '\n', st3)
# STRINGS ARE IMMUTABLE!!!!
st4 = st1 + ' ' + st2
print(st4)
print('hello there' + " " + 'MATRIX' + '130!')
first_name = 'Lyla'
fname = 'Toby'
print(f"Hello there {fname}!")

#LISTS
a_list = ['abc', 4, True, 987]
print(a_list)
num_list = [23, 456, 56, 78, 1, 18765]
print(sum(num_list))
print(min(num_list))
print(max(num_list))
print('LIST SHENANIGANS:--> \n\n')

print(len(num_list))
print(num_list[len(num_list)-1])
print(num_list[5])
print(num_list[-1])
print(num_list[-2])

# list.append(whatever we're appending) --> generic method format
# .append() --> adds on to the end
# .pop() 
# .remove()
# .insert()
ex_list = [1234, 'abc']

ex_list.append(9876543224121)
print(ex_list)
popped= ex_list.pop()
print(popped, ex_list)
ex_list.append(1234)
print(ex_list)
ex_list.remove(1234)
print(ex_list)
ex_list.insert(0, 1234)
print(ex_list)
ex_list.insert(3, 'ABC')
print(ex_list)

l_list = [ 56, 78, 1, 187, ]
l_st = 'SJFSH'
# LOOPING!
# for - super common use, executes code block at each item in the list
for l in l_st:
    print(l)
# for x in range(len(l_list)):
#     print(x)
# index
for i in range(len(l_st)):
    print(i)
# while
# runs as long as condition is True
print('WHILE LOOP EXAMPLE \n')
l=0
while l < len (l_st):
    if l_st[l] == 'F':
        print ('FOUND IT!')
    elif l_st[l]=='S':
        print('OHHH NO IT\'S HERE')
    else:
        print('Not a S or a F')
    print(l_st[l])
    l = l + 1

# Conditionals / control flow
# if/elif/else

# IN LINE VERSION!

# age = int(input('input your age '))

# if age < 18:
#     print('Minor')
# elif age >= 18 and age <= 65:
#     print('Adult')
# else:
#     print('Senior')
# truth-tree:
# T & T = T
# T & F = F
# with an and BOTH have to be True
# T or T = T
# F or T = T
# with an or EITHER have to be True
# TURN IT INTO A FUNC!
print("FUNCTION TEST: \n")
def age_filter(user_age):
    # user_age = int(input('input your age '))
    if user_age < 18:
        print('Minor')
    elif user_age >= 18 and user_age <= 65:
        print('Adult')
    else:
        return ('Senior')
print(age_filter(15))


def multiply(a, b):
    return a*b
v_prod = multiply(9,9)
print(v_prod)
print(multiply(6,6))