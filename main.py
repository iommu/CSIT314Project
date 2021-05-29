from wolfTest import generate, test, api
import unittest
from sympy import simplify


class TestWA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api = api.Wolframalpha()

    # python main.py TestWA.test_dob
    def test_dob(self):
        # Generate random values
        name = generate.rand_name()
        # Pass random values to known solution generator
        result_test = test.dob_check(name)
        # Pass random values to random string generator and then to search query and the trim returned JSON into final string
        query = generate.dob_string_gen(name)
        result_wolf = self.api.search(query)
        result_wolf = self.api.get_pod(result_wolf, "Result")[0]["plaintext"]
        # Test both equal
        self.assertEqual(result_test, result_wolf)

    # python main.py TestWA.test_quadratic
    def test_quadratic(self):
        # Generate random values
        a = generate.rand_int_range(0, 100)
        b = generate.rand_int_range(0, 100)
        c = generate.rand_int_range(0, 100)
        # Pass random values to known solution generator
        result_test = test.quadratic_check(a, b, c)
        # Pass random values to random string generator and then to search query and the trim returned JSON into final string
        query = generate.quadratic_gen(a, b, c)
        result_wolf = self.api.search(query)
        result_wolf = self.api.get_pod(result_wolf, "Complex solutions")
        if result_wolf == None:  # sometimes results is not complex
            result_wolf = self.api.get_pod(result_wolf, "Solutions")
        result_wolf = test.quaratic_format(result_wolf)
        # Test both equal
        same = True
        for index in range(2):
            same = simplify(result_test[index] - result_wolf[index]) == 0
            if same == False:
                break
        self.assertTrue(same)
    
    # python main.py TestWA.test_hash
    def test_hash(self):
        query = generate.hash_gen() # should have input for random string
        result_test = test.hash_check(query)
        result_wolf = self.api.search(query)
        result_wolf = self.api.get_pod(result_wolf, "Message digest")[0]['plaintext']
        # example output "integer form | 1095738169\nhexadecimal form | 414f a339"
        # Test both equal
        self.assertEqual(result_test, result_wolf)

    # python main.py TestWA.test_math
    def test_math(self):
        # Generate random values
        a = generate.rand_int_range(0, 100)
        b = generate.rand_int_range(0, 100)
        c = generate.rand_int_range(0, 100)
        d = generate.rand_int_range(0, 100)
        # Pass random values to known solution generator
        result_test = test.math_check(a, b, c, d)
        query = generate.test_gen(a, b, c, d)
        result_wolf = self.api.search(query)

    # python main.py TestWA.test_factor
    def test_factor(self):
        # Generate random values
        a = generate.rand_int_range(0, 20)
        b = generate.rand_int_range(0, 20)
        c = generate.rand_int_range(0, 20)
        d = generate.rand_int_range(0, 20)
        e = generate.rand_int_range(0, 20)
        f = generate.rand_int_range(0, 20)
        # Pass random values to known solution generator
        result_test = test.factor_check(a, b, c, d, e, f)
        query = generate.factor_gen(a, b, c, d, e, f)
        result_wolf = self.api.search(query)

    # python main.py TestWA.test_deg2rad
    def test_deg2rad(self):
        # Generate random values
        deg = generate.rand_float_range(-180, 180)
        result_test = test.deg2rad_check(a)
        query = generate.geometry_gen(a)
        result_wolf = self.api.search(query)

if __name__ == "__main__":
    unittest.main()
