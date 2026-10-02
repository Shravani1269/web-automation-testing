from playwright.sync_api import Page


class ProductPage:
    def __init__(self, page: Page):
        self.page = page

        self.product_items = page.locator(".inventory_item")
        self.product_names = page.locator(".inventory_item_name")
        self.product_prices = page.locator(".inventory_item_price")
        self.sort_dropdown = page.locator(".product_sort_container")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def wait_for_products(self):
        self.page.locator(".inventory_item").first.wait_for(
            state="visible"
        )

    def get_product_count(self):
        self.wait_for_products()
        return self.product_items.count()

    def get_product_names(self):
        self.wait_for_products()
        return self.product_names.all_inner_texts()

    def get_product_prices(self):
        self.wait_for_products()
        prices = self.product_prices.all_inner_texts()
        return [float(price.replace("$", "")) for price in prices]

    def sort_products(self, option: str):
        self.wait_for_products()
        self.sort_dropdown.select_option(option)

    def add_product_to_cart(self, product_name: str):
        self.wait_for_products()

        product = self.product_items.filter(
            has_text=product_name
        )

        product.locator("button").click()

    def get_cart_count(self):
        if self.cart_badge.count() == 0:
            return 0

        return int(self.cart_badge.inner_text())

    def open_cart(self):
        self.cart_link.click()
        self.page.wait_for_url("**/cart.html")