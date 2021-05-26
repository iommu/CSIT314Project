# This file takes the generates string/dict from generate.py and runs it
# through api.py to recieve wolframs' output. It then calculates the supposed
# answer to the question (or looks it up in a db is the answer is static) then
# checks it against the api.py's output

from sympy import symbols, solve
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
    expr = a * x ** 2 + b * x + c
    return solve(expr)  # example [-1 - sqrt(2)*I, -1 + sqrt()*I], a = 2, b = 4, c = 6

def math_check(a,b,c,d):
    expr = (a + d - c) / b
    return expr         #example 1.0, a = 2, b = 4, c = 6, d = 8


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
