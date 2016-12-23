from pyCalc.main import calculator
from pyCalc.interpreter import exceptions
from math import *
import unittest

class TestPyCalc(unittest.TestCase):
    COMP_TESTS = [('10*e^0*log10(.4* -5/-0.1-10) - -fabs(-53//10) + -5',
              '10*e**0*log10(.4* -5/-0.1-10) - - fabs(-53//10) + -5'),
             ('1*4+3.3/(3 + .3)*3(sqrt(4))/(sin(0) + 1)',
              '1*4+3.3/(3 + .3)*3*(sqrt(4))/(sin(0) + 1)'),
             ('(1+4)(5^0*5)*log(-5*-.5, 2)(-5)',
              '(1+4)*(5**0*5)*log(-5*-.5, 2)*(-5)'),
             ('5+(5+(5+(5+(5+(5+5(5+(5+(5-3))))))))-100',
              '5+(5+(5+(5+(5+(5+5*(5+(5+(5-3))))))))-100'),
             ('+ + + - - - 5// + - 5* - - - - - - - 1',
              '+ + + - - - 5// + - 5* - - - - - - - 1')]
    EXC_TESTS = ['5+3)', '((5+3)', '5*log(e, 54, 54)', 'log*5', 'fun(45)*46 - 3',
                 'log(-5, 3)', '5**3*3', '5/0', '']

    def test_computations(self):
        for calcTest, evalTest in self.COMP_TESTS:
            with self.subTest(test=calcTest):
                self.assertEqual(round(calculator.compute(calcTest), 10),
                                 round(eval(evalTest), 10)) 
    def test_exceptions(self):
        for test in self.EXC_TESTS:
            with self.subTest(test=test):
                self.assertRaises(exceptions.CalcError, calculator.compute, test)

if __name__ == '__main__':
    unittest.main()
