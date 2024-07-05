"""
if __name__ == "__main__"

y tho?
1. Module can be run as a stand alone program 
2. Module can be imported and used by other programs


python interpreter sets "special variable", one of them is __name__
then python will execute code found in __main__

"""


def main():
    print("We are in the main function")


if __name__ == "shit":
    main()


print(__name__)
