from playwright.sync_api import Page


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

        # Checkout information fields
        self.first_name_input = page.locator(
            "[data-test='firstName']"
        )
        self.last_name_input = page.locator(
            "[data-test='lastName']"
        )
        self.postal_code_input = page.locator(
            "[data-test='postalCode']"
        )

        # Buttons
        self.continue_button = page.locator(
            "[data-test='continue']"
        )
        self.cancel_button = page.locator(
            "[data-test='cancel']"
        )
        self.finish_button = page.locator(
            "[data-test='finish']"
        )

        # Checkout title
        self.checkout_title = page.locator(
            ".title"
        )

        # Overview page
        self.summary_info = page.locator(
            ".summary_info"
        )

        # Completion page
        self.confirmation_message = page.locator(
            ".complete-header"
        )

    def wait_for_information_page(self):

        self.page.wait_for_url(
            "**/checkout-step-one.html",
            timeout=15000
        )

        self.first_name_input.wait_for(
            state="visible",
            timeout=15000
        )

    def enter_customer_details(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ):

        self.wait_for_information_page()

        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_to_overview(self):

        self.continue_button.wait_for(
            state="visible",
            timeout=15000
        )

        self.continue_button.click()

        self.page.wait_for_url(
            "**/checkout-step-two.html",
            timeout=15000
        )

        self.summary_info.wait_for(
            state="visible",
            timeout=15000
        )

    def finish_checkout(self):

        self.finish_button.wait_for(
            state="visible",
            timeout=15000
        )

        self.finish_button.click()

        self.page.wait_for_url(
            "**/checkout-complete.html",
            timeout=15000
        )

        self.confirmation_message.wait_for(
            state="visible",
            timeout=15000
        )

    def get_checkout_title(self):

        self.checkout_title.wait_for(
            state="visible",
            timeout=15000
        )

        return self.checkout_title.inner_text()

    def get_confirmation_message(self):

        self.confirmation_message.wait_for(
            state="visible",
            timeout=15000
        )

        return self.confirmation_message.inner_text()