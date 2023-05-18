"""Beginner Python Project"""


from sample_madlibs import madlib_code, madlib_hp, madlib_hugergames, madlib_test, madlib_zombie
import random


if __name__ == "__main__":
    m = random.choice([madlib_code, madlib_hp, madlib_zombie, madlib_hugergames, madlib_test])
    m.madlib()