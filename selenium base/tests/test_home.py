from seleniumbase import BaseCase

class CoffeeCartTest(BaseCase):
    def test_coffee_cart(self):
        self.open("https://seleniumbase.io/coffee/")
        self.click('div[data-sb="Cappuccino"]')
        self.click('div[data-sb="Flat-White"]')
        self.click('div[data-sb="Cafe-Latte"]')
        self.click('a[aria-label="Cart page"]')
        self.assert_exact_text("Total: $53.00", "button.pay")
        self.click("button.pay")
        self.type("input#name", "Selenium Coffee")
        self.type("input#email", "test@test.test")
        self.click("button#submit-payment")
        self.assert_text("Thanks for your purchase.", "#app")


class TestMFALogin(BaseCase):
  def test_mfa_login(self):
    self.open("https://seleniumbase.io/realworld/login")
    self.type("#username", "demo_user")
    self.type("#password", "secret_pass")
    self.enter_mfa_code("#totpcode", "GAXG2MTEOR3DMMDG")  # 6-digit
    self.assert_exact_text("Welcome!", "h1")
    self.assert_element("img#image1")
    self.click('a:contains("This Page")')
    self.save_screenshot_to_logs()
