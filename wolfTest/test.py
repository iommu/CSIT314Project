# This file takes the generates string/dict from generate.py and runs it
# through api.py to recieve wolframs' output. It then calculates the supposed
# answer to the question (or looks it up in a db is the answer is static) then
# checks it against the api.py's output

import math, hashlib, zlib
from sympy import symbols, solve, factor
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication,
    convert_xor,
)

# Solution generators


def dob_check(name):
    # Dict can be indexes by a string, i.e. the name in this case
    dob_dict = {
        "Harriet Tubman": "March 1822",
        "Marvin Gaye": "Sunday, April 2, 1939",
    }
    return dob_dict[name]


def quadratic_check(a, b, c):
    x = symbols("x")
    expr = a * x**2 + b * x + c
    return solve(expr)  # example [-1 - sqrt(2)*I, -1 + sqrt()*I], a = 2, b = 4, c = 6

def math_check(a, b, c, d):
    expr = (a + b - c) / d
    return expr         #example 1.0, a = 2, b = 8, c = 6, d = 4

def factor_check(a, b, c, d, e, f):
    x = symbols("x")
    expr = a * x**5 - b * x**4 + c * x**4 - d * x**2 + e * x**3 - f
    return factor(expr)

def hash_check(s):
    # encode string with 3 different has methods. Will return encoded string in hexadecimal form
    s = s.split(' ', 1)
    if s[0] == "SHA1":
        return hashlib.sha1(s[1].encode()).hexdigest()
    elif s[0] == "MD5":
        return hashlib.md5(s[1].encode()).hexdigest()
    elif s[0] == "CRC32":
        return hex(zlib.crc32(str.encode(s[1])))
    else:
        print("Hash method undefined")
        return 0
    
def geometry_check(s):
    s = s.split()
    if s[0] == "pi":
        #print out pi to x digits
        x = int(s[1])
        return round(2*acos(0.0),x)
    #check if converting to radians
    elif s[0] == "convert" and s[4] == "radians":
        x = float(s[1])
        return x * math.pi/180
    #check if converting to degrees
    elif s[0] == "convert" and s[4] == "degrees":
        x = float(s[1])
        return x * 180 / math.pi
    return 0

def truth_table_check(expr, inputs=2):
    #assuming 2 variables p and q always (can change later)
    expr = expr.lower()
    expr = expr.replace("and","&")
    expr = expr.replace("or","|")
    expr = expr.replace("xor","^")
    expr = expr.replace("not","~")
    # create table string for comparison 
    table = expr[0]+" | "+expr[-1]+" | "+expr
    for p in range(0,inputs):
        for q in range (0,inputs):
            x = eval(expr)
            # add results to table string, only add first character of result to match wolf
            table+= "\n" +str(bool(p))[0] +" | "+str(bool(q))[0]+" | "+str(bool(x))[0]
    return table

# Formatters


def quaratic_format(unformatted):
    # unformatted =
    # [
    #     {
    #         "plaintext": "x = 1/45 (-23 - 7 i sqrt(14))",
    #         "title": ""
    #     },
    #     {
    #         "plaintext": "x = 1/45 (-23 + 7 i sqrt(14))",
    #         "title": ""
    #     }
    # ]
    formatted = [
        unformatted[0]["plaintext"][4:],
        unformatted[1]["plaintext"][4:],
    ]  # strip into array removing first 4 characters "x = "
    # formatted = ['1/45 (-23 - 7 i sqrt(14))', '1/45 (-23 + 7 i sqrt(14))']
    formatted = [
        formatted[0].replace("i", "I"),
        formatted[1].replace("i", "I"),
    ]  # replace i with I because that's how sympy does irrational
    # formatted = ['1/45 (-23 - 7 i sqrt(14))', '1/45 (-23 + 7 i sqrt(14))'] # doesn't matter for this eqn obviously
    transformations = standard_transformations + (
        implicit_multiplication,
        convert_xor,
    )  # setup variables for symbpy transformations
    return [
        parse_expr(formatted[0], transformations=transformations),
        parse_expr(formatted[1], transformations=transformations),
    ]  # run parser
