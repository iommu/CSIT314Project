import random
# This file generates a "random" string to passes it to the assert file

############################# WORKING #############################

# Random generators
def rand_name():
    return random.choice([
            "Harriet Tubman", 
            "Marvin Gaye",
            "Charlemagne",
            "Galileo Galilei",
            "Warren Buffett",
            "Tom Hanks",
            "Ferdinand Magellan",
            "Wiley Post"
        ])

def rand_int_range(start=0, end=200):
    return random.randint(start, end)

# String generators
def dob_string_gen(name):
    return "date of birth of {}".format(name)

def quadratic_gen(a, b, c):
    return "{}x^2 + {}x + {} = 0".format(a, b, c)

############################# IN PROGRESS #############################

 # same as what alex did. 
def math_gen(a, b, c, d):
    return "({}+{}-{})/{}".format(a, b, c, d)
    
    # very similar to quadratic
def solve_gen(a, b, c, d):
    return "{}x^2 + {}x = {} - {}x^3".format(a, b, c, d)
 
def factor_gen(a, b, c, d, e, f):    
    return "factor {}x^5 - {}x^4 + {}x^4 - {}x^2 + {}x^3 - {}".format(a, b, c, d, e, f)

#this might be a bit difficult. try it if u can otherwise just leave it. 
def derivative_gen(a, b, c):
    return"d/dx {}x^4+{}x^3+{}x".format(a, b, c)
    
  #checks for the given digits of pi
def geometry_gen(a=100,b=20,c=50):
    return "pi {} digits".format(a)
    return "convert {} degree to radian".format(a)
            
#works in similar way to the fist one"
# /
def hash_gen():
    return random.choice([
            "SHA1 Hi, i love computer science",
            "MD5 HELLO THERE I AM MD5!",
            "CRC32 The quick brown fox jumps over the lazy dog",
        ])
# Very simple equation 
def sum(a, b):
    return f"{a} + {b} "





