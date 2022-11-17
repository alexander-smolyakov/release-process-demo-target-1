import unittest

from app import printMessage

class SimpleTestCase(unittest.TestCase):
    def test_print_message(self):
        print("test_print_message")
        expectedMessage: str = "This is test"
        result = printMessage(expectedMessage)
        self.assertEqual(result, expectedMessage)

if __name__ == "__main__":
    unittest.main()
