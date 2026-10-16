import unittest

from MyProgram import get_message


class TestMyProgram(unittest.TestCase):
    def test_get_message(self):
        self.assertEqual(get_message(), "Hello from GitHub Actions!")


if __name__ == "__main__":
    unittest.main()
