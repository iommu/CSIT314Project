# This file takes the generates string/dict from generate.py and runs it
# through api.py to recieve wolframs' output. It then calculates the supposed
# answer to the question (or looks it up in a db is the answer is static) then
#install pip install truth-table-generator
# checks it against the api.py's output
from sympy import symbols, solve
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication,
    convert_xor,
)
import ttg

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
    return solve(expr)  # example [-1/5 - sqrt(46)*I/10, -1/5 + sqrt(46)*I/10]


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
