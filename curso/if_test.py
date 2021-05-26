import unittest

x = 2
if x == 2:
    result = 'OK'
elif x == 1:
    result = 'Error: x igual 1'
else:
    result = 'Error: X distinto 2'
print(result)


class TestResult(unittest.TestCase):

    def test_result(self):
        self.assertTrue(result)
