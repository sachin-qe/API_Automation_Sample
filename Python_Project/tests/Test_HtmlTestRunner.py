import unittest
import StringIO
import HtmlTestRunner

from test_login import *
from test_member import *
# from test_membertheme import *

class Test_HTMLTestRunner(unittest.TestCase):
    """ Example test for HtmlRunner. """
    # def test0(self):
        # self.suite = unittest.TestSuite()
        # buf = StringIO.StringIO()
        # runner = HTMLTestRunner.HTMLTestRunner(buf)
        # runner.run(self.suite)
        # # didn't blow up? ok.
        # self.assert_('</html>' in buf.getvalue())
    
    def test_main(self):        
        # suite of TestCases
        self.suite = unittest.TestSuite()
        buf = StringIO.StringIO()
        runner = HtmlTestRunner.HTMLTestRunner(buf)
        runner.run(self.suite)
        
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(login_testcase),
            unittest.defaultTestLoader.loadTestsFromTestCase(member_testcase)
            # unittest.defaultTestLoader.loadTestsFromTestCase(membertheme_testcase)
            ])


        # Invoke TestRunner
        # buf = StringIO.StringIO()
        # #runner = unittest.TextTestRunner(buf)       #DEBUG: this is the unittest baseline
        # runner = HTMLTestRunner.HTMLTestRunner(
        #             stream=buf,
        #             title='<Demo Test>',
        #             description='This demonstrates the report output by HTMLTestRunner.'
        #             )
        # runner.run(self.suite)        

if __name__ == '__main__':
    # HTMLTestRunner.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/media/ecolibrium/55BCC67E74BEA2F8/Python_Project/reports/API_Test/'"")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/media/ecolibrium/55BCC67E74BEA2F8/Python_Project/reports/API_Test/'))