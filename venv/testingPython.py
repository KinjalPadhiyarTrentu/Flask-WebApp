import unittest
from BLApi import app

class MyTest(unittest.TestCase):

    def test_app(self):
        tester = app.test_client()
        response = tester.get("/my",content_type="html/text")
        self.assertEqual(response.status_code,200)
        self.assertIn(b"Error",response.data)

if __name__== "__main__":
    unittest.main()