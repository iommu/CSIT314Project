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
##################################################################
################## new case ######################################
 # same as what alex did. 
def math_gen():
       return "(a+d-c)/b".format(a,b,c)
    
    # very similar to quadratic
def solve_gen():
    return "{}x^2 + {}x = {} - {}x^3".format(a,b,c,d)
    return" factor {}x^5 - {}x^4 + {}x^4 - {}x^2 + {}x^3 - {}".format(a,b,c,d,e)
#this might be a bit difficult. try it if u can otherwise just leave it. 
def derivative_gen():
    return"d/dx {}x^2+{}y^4, d/dy x^2 y^4".format(a,b)

# this is easy because formula = p and q and p implies q       
def truth_table_gen():
    return"truth table p implies q"
    return"truth table p and q"
    
  #checks for the given digits of pi

def pi_dig_gen(a=100,b=20,c=50):
    return "pi {}digits".format(a,b,c)
            


#works in similar way to rand_name and is easier to validate. can be validated with eith hexadecimal form or ineger. i think the integer is easier but i coud be wrong.
# /
def hash_gen
    return random.choice([
            "SHA1 Hi, i love computer science",
            "MD5 HELLO THERE I AM MD5!"
            "CRC32 The quick brown fox jumps over the lazy dog"
        
        ])

