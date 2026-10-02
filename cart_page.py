from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page

        self.cart_items = page.locator(".cart_list > .cart_item")
        self.cart_item_names = page.locator(
            ".cart_list > .cart_item .inventory_item_name"
        )
        self.cart_item_prices = page.locator(
            ".cart_list > .cart_item .inventory_item_price"
        )

        self.continue_shopping_button = page.locator(
            "[data-test='continue-shopping']"
        )

        self.checkout_button = page.locator(
            "[data-test='checkout']"
        )

    def wait_for_cart(self):
        self.page.wait_for_url("**/cart.html")
        self.page.locator(".cart_list").wait_for(state="visible")

    def wait_for_cart_items(self):
        self.wait_for_cart()

        if self.cart_items.count() > 0:
            self.cart_items.first.wait_for(state="visible")

    def get_item_count(self):
        self.wait_for_cart()
        return self.cart_items.count()

    def get_item_names(self):
        self.wait_for_cart_items()
        return self.cart_item_names.all_inner_texts()

    def get_item_prices(self):
        self.wait_for_cart_items()
        prices = self.cart_item_prices.all_inner_texts()
        return [float(price.replace("$", "")) for price in prices]

    def remove_product(self, product_name: str):
        self.wait_for_cart_items()
        item = self.cart_items.filter(has_text=product_name)
        item.locator("button").click()

    def continue_shopping(self):
        self.wait_for_cart()
        self.continue_shopping_button.click()

    def proceed_to_checkout(self):
        self.wait_for_cart()
        self.checkout_button.click()