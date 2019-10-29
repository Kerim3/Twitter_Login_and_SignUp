import unittest
from testall import TestHome
from testall import TestSignIn
from testall import TestSignUp

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestHome('test_TC001_sign_up'))
    suite.addTest(TestSignUp('test_TC003_SignUp'))
    suite.addTest(TestHome('test_TC002_sign_in'))
    suite.addTest(TestSignIn('test_TC004_SignIn'))

    return suite
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    suite = suite()
    runner.run(suite)
