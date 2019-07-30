import unittest
from unittest.mock import patch
from emp import Employee


class TestEmp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # useful to do once set up task only once
        print("setUpClass")
        print("I run ONCE at the START of this test suite")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        print("I run ONCE at the END of this test suite")

    def setUp(self):
        # instance attributes
        # runs for every test
        print("setUp")
        self.emp1 = Employee("Roger", "Ramjet", 100)
        self.emp2 = Employee("Daisy", "Flower", 200)

    def tearDown(self):
        # removes for each test
        # tear down databases etc here
        print("tearDown")

    def test_full_name(self):
        self.assertEqual(self.emp1.fullname, "Roger Ramjet")
        self.assertEqual(self.emp2.fullname, "Daisy Flower")
        self.assertNotEqual(self.emp1.fullname, "Daisy Flower")

    def test_email(self):
        self.assertEqual(self.emp1.email, "Roger.Ramjet@email.com")
        self.assertEqual(self.emp2.email, "Daisy.Flower@email.com")

    def test_apply_raise(self):
        # apply the raise and check it
        self.emp1.apply_raise()

        self.assertNotEqual(self.emp1.pay, 100)
        self.assertEqual(self.emp1.pay, 105)
        self.assertEqual(self.emp2.pay, 200)
        self.assertNotEqual(self.emp2.pay, 210)

    def test_monthly_sched(self):
        # mock out calls to things which are out of our control,
        # or resource intensive. We are testing our code not the endpoint etc.
        with patch("emp.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            sched = self.emp1.get_schedule("May")
            mocked_get.assert_called_with("https://website.com/Ramjet/May")
            self.assertEqual(sched, "Success")

            mocked_get.return_value.ok = False
            mocked_get.return_value.text = "Bad response!"

            sched = self.emp2.get_schedule("October")
            mocked_get.assert_called_with("https://website.com/Flower/October")
            self.assertEqual(sched, "Bad response!")


if __name__ == "__main__":
    unittest.main()
