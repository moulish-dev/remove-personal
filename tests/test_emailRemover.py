import unittest
from email_remover.removeEmail import removeEmailsText

class TestEmailRemover(unittest.TestCase):
    
    def test_remove_emails(self):
        data = "Contact me at example@example.com for more info."
        result = removeEmailsText(data)
        self.assertEqual(result, "Contact me at  for more info.")
        
    def test_no_emails(self):
        data = "No emails here."
        result = removeEmailsText(data)
        self.assertEqual(result, "No emails here.")
        
    def test_multiple_emails(self):
        data = "My emails are first@example.com and second@example.org."
        result = removeEmailsText(data)
        self.assertEqual(result, "My emails are  and .")

if __name__ == "__main__":
    unittest.main()
