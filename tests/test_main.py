# pylint: disable=C0114
import unittest
from helm_values_generator.generate_values import generate_values


class TestMain1(unittest.TestCase):  # pylint: disable=C0115
    def test_main1(self):  # pylint: disable=C0116
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
