import unittest
import HtmlTestRunner

from live9 import Test
from live101 import Test_Mozila

class TestSuite(unittest.TestCase):
    #aici implementam o suita de teste
    def test_suite(self): #cuvant cheie
        smoketest = unittest.TestSuite()
        #aici adaugam testele noastre in suita
        smoketest.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Test_Mozila)
        ])

        #aici implementam raportul HTML
        runner=HtmlTestRunner.HTMLTestRunner(
            combine_reports = True,
            report_title = "Primul meu raport",
            report_name = "Acesta este un raport de testare automata"
        )



        runner.run(smoketest)
