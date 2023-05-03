import unittest
from helm_values_generator.generate_values import generate_values

class TestMain1(unittest.TestCase):
    def test_main1(self):
        vals = generate_values("./tests/testdata")

        expected = """cronJob:
  container:
    image: <value>
  schedule: <value>
database:
  tables: <value>
jobName: <value>
secretName: <value>"""
        self.assertEqual(vals, expected)


if __name__ == "__main__":
    unittest.main()