import random
import boolean
from random_word import RandomWords
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

def rand_word_sentence(length=10):
    r = RandomWords()
    words = r.get_random_words(limit=10)
    sentence = ""
    for word in words:
        sentence += f" {word}"
    return sentence

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
    return "solve {}x^2 + {}x = {} - {}x^3".format(a, b, c, d)
 
def factor_gen(a, b, c, d, e, f):    
    return "factor {}x^5 - {}x^4 + {}x^4 - {}x^2 + {}x^3 - {}".format(a, b, c, d, e, f)

#this might be a bit difficult. try it if u can otherwise just leave it. 
def derivative_gen(a, b, c):
    return"d/dx {}x^4+{}x^3+{}x".format(a, b, c)
    
#checks for the given digits of pi
def pi_gen(length):
    return "pi {} digits".format(length)

    #checkes for the conversion of degree to radian
def deg2rad_gen(a):
    return "convert {} degree to radian".format(a)
            
#works in similar way to the fist one"
def hash_gen(sentence):
    hash_type = random.choice(["SHA1", "MD5", "CRC32"])
    return f"{hash_type}{sentence}"

# Very simple equation 
def sum_gen(a, b):
    return f"sum of {a} + {b} "

def dod_string_gen(name):
    return "date of death of {}".format(name)

def random_float_list(length=10, start=50.50, end=500.50):
    # any random float between 50.50 to 500.50
    return [random.uniform(start, end) for index in range(length)]

def simple_gen_function(str_in, sep=""):
    if sep == "":
        yield str_in[0]
        for c in str_in[1:]:
            yield c
    else:
        return str_in

def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False
    
def double(L):
    return [x*2 for x in L]

