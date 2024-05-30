"""
This script is to use the logic library to help prove 
answers to the quiz.
https://cs50.harvard.edu/ai/2024/quizzes/1/
"""
from src.logic import *


def one():
    """
    'Hermione is in the library'
    'Harry is not in the library or Hermione is in the library'
    -------------------------
    (A) |=  (!(B) v (A))
    """
    herminone_library = Symbol("HermioneLibrary")
    harry_library = Symbol("HarryLibrary")
    third = model_check(herminone_library, Or(Not(harry_library), herminone_library))

    return f"Hermione is in the library entails Harry is not in the library or Hermione is in the library: {third}"


def two():
    return "(A v B) ^ !(A ^ B)"


def three():
    """
    R = It is raining.
    C = It is cloudy.
    S = It is sunny.

    If it is raining, then it is cloudy and not sunny.
    -------------------
    R -> (C ^ !(S))
    """
    return "R -> (C ^ !(S))"


def four():
    """
    Student(x) = x is a student.
    Course(x) = x is a course.
    Enrolled(x, y) = x is enrolled in y.
    """
    return "∃x. Course(x) ∧ Enrolled(Harry, x) ∧ Enrolled(Hermione, x)"


if __name__ == "__main__":
    print("----------")
    print(f"The answer Q1 is '{one()}'")
    print("----------")
    print(f"The answer Q2 is '{two()}'")
    print("----------")
    print(f"The answer Q3 is '{three()}'")
    print("----------")
    print(f"The answer Q4 is '{four()}'")
