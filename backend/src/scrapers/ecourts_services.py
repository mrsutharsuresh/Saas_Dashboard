import asyncio
import os
import base64
from playwright.async_api import async_playwright
from src.core.logger import logger
from dotenv import load_dotenv

load_dotenv()

class ECourtsServicesScraper:
    def __init__(self):
        self.base_url = "https://services.ecourts.gov.in/ecourtindia_v6/"
        self.twocaptcha_key = os.getenv("TWOCAPTCHA_API_KEY")

    async def fetch_case_by_cnr(self, cnr_number: str):
        logger.info("Initializing eCourts Services Scraper", cnr=cnr_number)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 NyayaTrack-Bot POC"
            )
            page = await context.new_page()

            try:
                logger.info("Navigating to eCourts home page", url=self.base_url)
                await page.goto(self.base_url, timeout=30000)

                # Wait for the main options to load - in services.ecourts, we usually click on 'Search by CNR'
                cnr_input = page.locator("#cino")
                await cnr_input.wait_for(state="visible", timeout=15000)
                
                logger.info("CNR Input found, entering data", cnr=cnr_number)
                await cnr_input.fill(cnr_number)

                # Find the Captcha image
                captcha_image = page.locator("#captcha_image")
                await captcha_image.wait_for(state="visible")
                captcha_buffer = await captcha_image.screenshot()
                captcha_b64 = base64.b64encode(captcha_buffer).decode("utf-8")
                
                logger.info("Captcha image captured", size=len(captcha_b64))

                # Note: In a real run, we would send `captcha_b64` to 2Captcha here.
                # For this basic POC script, we will just log that we reached the captcha stage.
                # Since we don't have a real 2Captcha key configured yet in the .env, we will pause here.
                
                logger.info("POC Step 1: Successfully loaded page, entered CNR, and grabbed CAPTCHA.")
                
                return {
                    "status": "success",
                    "cnr": cnr_number,
                    "captcha_base64_length": len(captcha_b64),
                    "message": "Ready to send to 2Captcha"
                }

            except Exception as e:
                logger.error("Error during scraping", error=str(e), exc_info=True)
                return {"status": "error", "message": str(e)}
            finally:
                await browser.close()

if __name__ == "__main__":
    scraper = ECourtsServicesScraper()
    # Test with a dummy CNR number
    result = asyncio.run(scraper.fetch_case_by_cnr("RJJP010000012024"))
    print(result)
