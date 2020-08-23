from selenium import webdriver
import unittest
import time
import re as regex

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_read_cv(self):
        # User navigates to the webpage
        self.browser.get('http://127.0.0.1:8000')

        # User reaches home page and notices it's a personal website with a name in the title
        self.assertIn('Likkan Chung', self.browser.title)

        # User looks for a 'CV' page and finds it in the nav bar
        try:
            cv_button = self.browser.find_element_by_link_text('CV')
        except (NoSuchElementException):
            self.fail()

        # User clicks on 'CV button in the nav bar'
        cv_button.click()
        time.sleep(1)

        # User reaches the 'CV' page and notices 'CV' in the title bar
        self.assertIn('CV', self.browser.title)

        # User looks for basic contact details, including a phone number, email, and address
        # phone pattern matches any UK mobile number starting +447 or 07 - with arbitrary ry whitespaeces
        #phone_pattern = regex.compile(r"(\+(\s)?4(\s)?4(\s)?7(\s)?[0-9](\s)?[0-9](\s)?[0-9](\s)?[0-9](\s)?[0-9](\s)?[0-9](\s)?[0-9](\s)?[0-9](\s)?[0-9])|(0(\s)?7(\s)?[0-9](\s)?[0-9](\s)?[0-9](\s)?[0-9](\s)?[0-9](\s)?[0-9](\s)?[0-9](\s)?[0-9](\s)?[0-9])")
        phone_pattern = regex.compile(r"\+44700 000 0000")
        phone_match = False
        # email pattern matches email addresses anon@anon.com(.com)*
        email_pattern = regex.compile(r"[a-zA-Z]+\@[a-zA-Z]+\.[a-zA-Z]+(\.[a-zA-Z]+)*")
        email_match = False
        # address pattern matches a UK post code as listed on https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom - ignoring special cases
        address_pattern = regex.compile(r"[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}")
        address_match = False
        elements = self.browser.find_elements_by_tag_name('div')
        self.assertIsNot(len(elements), 0)
        for element in elements:
            match = phone_pattern.search(element.text)
            if match:
                phone_match = True
            match = email_pattern.search(element.text)
            if match:
                email_match = True
            match = address_pattern.search(element.text)
            if match:
                address_match = True
        self.assertTrue(phone_match)
        self.assertTrue(email_match)
        self.assertTrue(address_match)

        # User wants to know if the person has been to University so looks for 'Education'
        education_pattern = regex.compile("education")
        education_match = False
        for element in elements:
            match = education_pattern.search(element.text.lower())
            if match:
                education_match = True
        self.assertTrue(education_match)

        # User wants to know what jobs they have done so looks for 'Experience'
        experience_pattern = regex.compile("experience")
        experience_match = False
        for element in elements:
            match = experience_pattern.search(element.text.lower())
            if match:
                experience_match = True
        self.assertTrue(experience_match)

        # User thinks that volunteering is also a good sign so looks for 'Volunteering'
        volunteering_pattern = regex.compile("volunteering")
        volunteering_match = False
        for element in elements:
            match = volunteering_pattern.search(element.text.lower())
            if match:
                volunteering_match = True
        self.assertTrue(volunteering_match)

        # Satisfied with the content the user closes the webpage

if __name__ == '__main__':
    unittest.main(warnings='ignore')
