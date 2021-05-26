import random
# This file generates a "random" string to passes it to the assert file

# Random generators
def rand_name():
    return random.choice([
            "Harriet Tubman", 
            "Marvin Gaye"
        ])

def rand_int_range(start=0, end=200):
    return random.randint(start, end)

# String generators
def dob_string_gen(name):
    return "date of birth of {}".format(name)

def quadratic_gen(a,b,c):
    return "{}x^2 + {}x + {} = 0".format(a,b,c)
 
def math_gen():
       return "(a+d-c)/b".format(a,b,c)
def solve_gen():
    return "{}x^2 + {}x = {} - {}x^3".format(a,b,c,d)
    return" factor {}x^5 - {}x^4 + {}x^4 - {}x^2 + {}x^3 - {}".format(a,b,c,d,e)

def derivative_gen():
    return"d/dx {}x^2+{}y^4, d/dy x^2 y^4".format(a,b)
            
def truth_table_gen():
    return"truth table p and q xor r and s"
    return"simplify p && (q xor r) && s"
    return"simplify p not r&& (r xor s) xor q"

def logic_gen():
    return"logic circuit (~p or ~q) and (r xor s)"

