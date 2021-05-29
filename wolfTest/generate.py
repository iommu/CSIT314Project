import random
import boolean
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

# generate random float number for the geometry_gen
def rand_float_range(start=-360, end=360):
    return round(random.uniform(start, end), 1)

def rand_logic(letters_int):
    letters = ['q', 'r', 's', 't', 'u', 'v'] # std array of logic letters
    logic = ['and', 'or', 'xor']
    if letters_int > len(letters):
        raise RuntimeError('Too many letters, max {}'.format(len(letters)))
    output = ""
    for letter in letters[:letters_int-1]:
        not_rand = random.choices(["not ",""], weights=[1,5], k=1)[0] # 1 in 5 chance for not
        output += f"{not_rand}{letter} {random.choice(logic)} ("
    output += letters[letters_int-1]
    output += ")"*(letters_int-1)
    return output

# String generators
def dob_string_gen(name):
    return "date of birth of {}".format(name)

def quadratic_gen(a, b, c):
    return "{}x^2 + {}x + {} = 0".format(a, b, c)

def truth_table_gen(logic):
    return "truth table {}".format(logic)

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
def pie_gen(a):
    return "pi {} digits".format(a)

    #checkes for the conversion of degree to radian
def deg2rad_gen(a):
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

# String letter generation
def get_random_string(length):
    # With combination of upper case letter
    result_str = ''.join(random.choice(string.ascii_uppercase) for i in range(length))
    # print random string
    print(result_str)

# string of length 5
get_random_string(5)
get_random_string(5)

# Random string of length 7
result_str = ''.join((random.choice('abcdxyzpqr') for i in range(7)))
print(result_str)

