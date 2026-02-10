from playwright.sync_api import sync_playwright, Page, BrowserContext
import time
from .utils import get_random_user_agent, random_sleep

class BaseScraper:
    def __init__(self, headless=False):
        self.headless = headless
        self.browser = None
        self.context = None
        self.page = None
        self.playwright = None

    def start(self):
        """Initializes the browser with stealth settings."""
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            headless=self.headless,
            args=["--disable-blink-features=AutomationControlled"] # Hide webdriver propery
        )
        
        # Create a context with a random user agent and viewport
        self.context = self.browser.new_context(
            user_agent=get_random_user_agent(),
            viewport={"width": 1280, "height": 720},
            locale="en-IN",
            timezone_id="Asia/Kolkata"
        )
        
        # Add init script to further hide automation
        self.context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """)
        
        self.page = self.context.new_page()
        print("Browser started in Stealth Mode.")

    def stop(self):
        """Closes the browser resources."""
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
        print("Browser stopped.")

    def solve_captcha(self, image_selector: str):
        """
        Placeholder for 2Captcha / CapSolver integration.
        For now, it pauses for manual solving if not headless.
        """
        print(f"Captcha detected at {image_selector}. Waiting for solution...")
        if not self.headless:
            print("Please solve the captcha manually in the browser window.")
            # In production, this would make an API call to 2Captcha
            # result = two_captcha_client.solve(image)
            # return result
            time.sleep(15) # Wait for human to solve
        else:
            print("Headless mode: Cannot solve captcha manually. Integration required.")
            raise Exception("Captcha detected in headless mode.")

    def navigate(self, url):
        """Safe navigation with retries."""
        print(f"Navigating to {url}...")
        try:
            self.page.goto(url, timeout=60000, wait_until="networkidle")
            random_sleep(2, 4)
        except Exception as e:
            print(f"Navigation failed: {e}")
            # Logic to retry or refresh could go here
            raise e

    def save_screenshot(self, filename="screenshot.png"):
        self.page.screenshot(path=filename)
        print(f"Screenshot saved to {filename}")
