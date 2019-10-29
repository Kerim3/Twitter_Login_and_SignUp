from testall import TestHome
from testall import TestSignIn
from  testall import TestSignUp
import unittest
from multiprocessing import Pool

def run_test(test_to_run):
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_to_run)
tests = [TestHome('test_TC001_sign_up'),
         TestSignUp('test_TC003_SignUp'),
         TestHome('test_TC002_sign_in'),
         TestSignIn('test_TC004_SignIn')]
if __name__ == '__main__':
    with Pool(4) as p:
        p.map(run_test, tests)