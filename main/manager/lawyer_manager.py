import doctest
from main.classes.lawyer import Lawyer

if __name__ == "__main__":
    lawyer = Lawyer('Sebastian', 18, 100, False, True, False)
    print(lawyer)