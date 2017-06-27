import HtmlTestRunner
import unittest
import StringIO

from test_login import *
from test_member import *
from test_membertheme import *

class TestAPIMethods(unittest.TestCase):
    # """ Example test for HtmlRunner. """

    def test_main(self):
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(login_testcase),
            unittest.defaultTestLoader.loadTestsFromTestCase(member_testcase)
            # unittest.defaultTestLoader.loadTestsFromTestCase(membertheme_testcase)
            ])

        # Invoke TestRunner
        # buf = StringIO.StringIO()
        #runner = unittest.TextTestRunner(buf)       #DEBUG: this is the unittest baseline
        # runner = HTMLTestRunner.HTMLTestRunner(
                    # stream=buf,
                    # title='<Demo Test>',
                    # description='This demonstrates the report output by HTMLTestRunner.'
                    # )
        # runner.run(self.suite)  

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/media/ecolibrium/55BCC67E74BEA2F8/Python_Project/reports/API_Test/'))