#
#  GoogleFindMyTools - A set of tools to interact with the Google Find My API
#  Copyright © 2024 Leon Böttger. All rights reserved.
#

from selenium.webdriver.support.ui import WebDriverWait
from chrome_driver import create_driver

def request_oauth_account_token_flow():

    print("""[AuthFlow] This script will now open Google Chrome on your device to login to your Google account.
> Please make sure that Chrome is installed on your system.
> For macOS users only: Make that you allow Python (or PyCharm) to control Chrome if prompted. 
    """)

    # Press enter to continue
    user_input = input("[AuthFlow] Press Enter to continue (or type 'q' to exit)...")
    if user_input.lower() in ['q', 'exit', 'quit']:
        print("[AuthFlow] Exiting...")
        import sys
        sys.exit(0)

    # Automatically install and set up the Chrome driver
    print("[AuthFlow] Installing ChromeDriver...")

    driver = create_driver()

    from selenium.common.exceptions import WebDriverException

    try:
        # Open the browser and navigate to the URL
        driver.get("https://accounts.google.com/EmbeddedSetup")

        # Wait until the "oauth_token" cookie is set
        print("[AuthFlow] Waiting for 'oauth_token' cookie to be set...")
        try:
            WebDriverWait(driver, 300).until(
                lambda d: d.get_cookie("oauth_token") is not None
            )
        except WebDriverException:
            print("[AuthFlow] Browser closed or connection lost. Exiting...")
            import sys
            sys.exit(0)

        # Get the value of the "oauth_token" cookie
        oauth_token_cookie = driver.get_cookie("oauth_token")
        oauth_token_value = oauth_token_cookie['value']

        # Print the value of the "oauth_token" cookie
        print("[AuthFlow] Retrieved Account Token successfully.")

        return oauth_token_value

    except Exception as e:
        print(f"[AuthFlow] An unexpected error occurred: {e}")
        import sys
        sys.exit(1)

    finally:
        # Close the browser
        try:
            driver.quit()
        except:
            pass

if __name__ == '__main__':
    request_oauth_account_token_flow()