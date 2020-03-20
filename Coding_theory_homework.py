import numpy as np

n = int(input("Ënter the value of n: "))
k = int(input("Enter the value of k: "))
p = input('Enter the polynomial p (ex: "1+X+X^3") : ')

degree = n-k

list = []
list_codes = []
count = -1
P = []

#this function returns a string of the form 1, X or X^p
#the input of this funtion is a int number that represents the rank of the value
def form_element(rank):
    if rank == 0:
        element = "1"
    elif rank == 1:
        element = "X"
    else:
        element = "X^" + str(rank)

    return element

def get_difference(mx, p):
    difference = get_rank(get_last_value(mx)) - get_rank(get_last_value(p))

    return difference

#one of the mos used functions in the program
#the input is a string like : X^4
#and it returns the rank of that value as an int value that we can work with : if input =X^4 , output is 4
def get_rank(value):

    if value == "1":
        return 0
    elif value == "X":
        return 1
    else :
        val = value.split('^')
        new_value = int(val[1])
        return new_value

def get_last_value(string):
    if "+" in string:
        sub_s = string.split("+")
        value = sub_s[-1]
    else:
        return string

    return value

# in order for us to divide 2 values. m*x^(n-k) to get r ,we'll add them up , convert them into their ranks 
# and eliminate the doubles, so it is just like subtracting in a basic division 
def add_and_eliminate(mx, aux):
    new_sum = ""
    summ = []
    string = mx + "+" + aux
    elements = string.split("+")
    for i in elements:
        summ.append(get_rank(i))

    summ.sort()
    summ_2 = []
    for i in range(len(summ)-1):
        if summ[i] != summ[i+1] and summ[i] != summ[i-1]:
            summ_2.append(summ[i])

    for i in summ_2:
         new_sum = new_sum + form_element(i) + "+"

    new_sum = new_sum[:-1]

    return new_sum

#this function decrements the value of an element of the form X or X^p by one at a time
def subtract_value(number):

    if number == "X":
        number = "1"
    elif number == "X^2":
        number = "X"
    else :
        num = number.split("^")
        numb = int(num[1])
        numb -= 1
        number = "X^" + str(numb)

    return number

#this function increment the value of an element of the form 1,X or X^p by one at a time
def add_value(number):
    if number == 0:
        return number
    elif number == "1":
        number = "X"
    elif number == "X":
        number = "X^2"
    else:
        num = number.split("^")
        numb = int(num[1])
        numb += 1
        number = "X^" + str(numb)

    return number

def gen_and_check(v, degree):
    rank = 0
    list_n = []
    number = ""
    elements = v.split("+")
    for i in elements:
        list_n.append(get_rank(i))

    for i in range(0, degree):
        if rank in list_n:
            number = number + "1"
        else :
            number = number + "0"

        rank += 1

    return number

def add_to_string(e, string):
    if "+" in string:
        sub_s = string.split("+")
        string = []
        for number in sub_s:
            if e == 0:
                string.append(number)
            for i in range(e):
                number = add_value(number)
                string.append(number)

        stri = ""
        for i in string :
            stri = stri + i + "+"
        stri = stri[:-1]
        string = stri
    else:
        for i in range(e):
            string = add_value(string)
            
    return string

def divide(mx, p):
    while get_rank(get_last_value(mx)) >= get_rank(get_last_value(p)):
        e = get_difference(mx, p)
        aux = add_to_string(e, p)
        mx = add_and_eliminate(mx, aux)
    return mx

def generate_message(e):
    number = ""
    for i in e:
        number = number + str(i)

    return number


def generate_xnk(degree):
    if degree == "1":
        xnk = "X"
    else: xnk = "X^" + str(degree)

    return xnk

def generate_m(code):
    position = -1

    for i in range(len(code)):
        if code[i] == 1:
            position = i
            break

    if position == 0:
        m = "1"
    elif position == 1:
        m = "X"
    else :
        m = "X^" + str(position)

    return m

def print_G(list_codes, k, n):
    Matrix = [[0 for x in range(k)] for y in range(n)]
    for i in range(k):
        for j in range(n):
            Matrix[j][i] = (list_codes[i])[j]
    print("G = ")
    for i in Matrix:
        print(i)

def print_H(P, k, n):
    Matrix = [[0 for x in range(n)] for y in range(n-k)]

    for i in range(n-k):
        Matrix[i][i] = 1
    x = -1
    for j in range(n-k, n):
        y = -1
        x += 1
        for i in range(n-k):
            y += 1
            Matrix[i][j] = (P[x])[y]

    print("H = ")
    for i in Matrix:
        print(i)

#this function generates the codes and stores tem into the list_codes list
#and stores the first part of the codes in the P list so we can use the when building the matrix G and H
def get_code_word(list):

    for e in list:
        m = generate_m(e)
        xnk = generate_xnk(degree)
        mx = xnk
        for i in range(get_rank(m)):
            mx = add_value(mx)
        r = divide(mx, p)
        v = r + "+" + mx
        code = gen_and_check(v, degree)
        x = generate_message(e)
        P.append(code)
        code_word = str(code) + str(x)
        list_codes.append(code_word)

def generate_start(count):
    for i in range(k):
        sub_list = []
        count += 1
        for j in range(k):
            if j == count:
                sub_list.append(1)
            else:
                sub_list.append(0)

        list.append(sub_list)

    return list

def main():
    get_code_word(generate_start(count))
    print_G(list_codes,k,n)
    print()
    print_H(P,k,n)

main()



