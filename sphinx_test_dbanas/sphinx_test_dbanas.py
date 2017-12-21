""" A simple test case, illustrating a Sphinx bug. """

import sys

class SphinxTest(object):
    """ Class docstring. """

    cAtt = int(1)  #: A class attribute.

    def __init__(self):
        """ Instance docstring. """

        self.iAtt = int(2)  #: An instance attribute.

def main():
    """ Main entry point for the script. """

    mySphinxTest = SphinxTest()
    print("cAtt = {}; iAtt = {}".format(mySphinxTest.cAtt, mySphinxTest.iAtt))

if __name__ == '__main__':
    sys.exit(main())

