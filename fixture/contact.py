from selenium.webdriver.common.by import By
import time

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_form(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_contact_form()
        #fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element(By.NAME, "submit").click()
        self.return_to_home_page()

    def edit_first(self, contact):
        wd = self.app.wd
        # select first contact
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # edit entry
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element(By.NAME, "update").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        #select first contact
        wd.find_element(By.NAME, "selected[]").click()
        #submit deletion contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Delete 1 addresses[\s\S]$")
        wd.switch_to.alert.accept()
        time.sleep(5)  # Сон в 5 секунд

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()
