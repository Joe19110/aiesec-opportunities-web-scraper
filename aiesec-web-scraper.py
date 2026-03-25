from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime
import re
import time


START_LIMIT = datetime(2026, 7, 1)
END_LIMIT = datetime(2026, 9, 7)

SEARCH_URL = (
"https://aiesec.org/search"
"?home_mcs=1609" # Change this to your country code
"&programmes=7"
"&earliest_start_date=2026-7-01"
)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

wait = WebDriverWait(driver, 20)

driver.get(SEARCH_URL)


# Open output file
file = open(
    "list_opportunities_egypt.txt",
    "w",
    encoding="utf-8"
)


def write_output(text):

    print(text)
    file.write(text + "\n")


# Accept cookies
try:
    cookie_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'Accept')]")
        )
    )
    cookie_button.click()

except:
    pass

time.sleep(5)


# LOAD ALL OPPORTUNITIES
while True:

    try:
        load_more_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(.,'Load more')]")
            )
        )

        driver.execute_script(
            "arguments[0].click();",
            load_more_button
        )

        time.sleep(3)

    except:
        break


# Collect links
links = driver.find_elements(
    By.XPATH,
    "//a[contains(@href,'/opportunity/global-volunteer/')]"
)

opportunity_links = []

for l in links:

    href = l.get_attribute("href")

    if href not in opportunity_links:
        opportunity_links.append(href)


write_output("")
write_output("EGYPT") # Change this to your country name
write_output("")


# Visit each opportunity
for link in opportunity_links:

    driver.get(link)

    time.sleep(5)

    # TITLE
    try:
        title = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h3[contains(@class,'text-3xl')]")
            )
        ).text

    except:
        continue


    # LOCATION
    try:
        location_block = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class,'text-[16px]')]")
            )
        )

        location_lines = location_block.text.split("\n")

        if len(location_lines) >= 2:
            location = location_lines[0] + "·" + location_lines[1]
        else:
            location = location_lines[0]

    except:
        location = "Unknown Location"


    # PRICE
    try:
        price = driver.find_element(
            By.XPATH,
            "//*[contains(text(),'IDR')]"
        ).text

    except:
        price = "Check page"


    # SLOT SOURCE
    slot_source = driver

    try:

        view_all_buttons = driver.find_elements(
            By.XPATH,
            "//*[contains(text(),'View all slots')]"
        )

        if len(view_all_buttons) > 0:

            driver.execute_script(
                "arguments[0].click();",
                view_all_buttons[0]
            )

            slot_source = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@role='dialog']")
                )
            )

            time.sleep(2)

    except:
        slot_source = driver


    # READ SLOT BLOCKS
    slot_blocks = slot_source.find_elements(
        By.XPATH,
        ".//div[contains(., 'Apply')]"
    )

    printed_periods = set()
    printed_header = False

    valid_periods = []

    for block in slot_blocks:

        text = block.text

        date_match = re.search(
            r'(\d{1,2}\s\w{3},\s\d{4})\s-\s(\d{1,2}\s\w{3},\s\d{4})',
            text
        )

        slot_match = re.search(
            r'(\d+)\sopenings',
            text
        )

        if not date_match:
            continue

        start_str, end_str = date_match.groups()

        period_key = start_str + end_str

        if period_key in printed_periods:
            continue

        try:
            start_date = datetime.strptime(
                start_str,
                "%d %b, %Y"
            )

            end_date = datetime.strptime(
                end_str,
                "%d %b, %Y"
            )

        except:
            continue

        if start_date < START_LIMIT:
            continue

        if end_date > END_LIMIT:
            continue

        printed_periods.add(period_key)

        if slot_match:
            openings = slot_match.group(1)
        else:
            openings = "Check page"

        valid_periods.append(
            (
                start_str,
                end_str,
                openings
            )
        )


    if len(valid_periods) > 0:

        write_output("📍" + title)
        write_output("Location 🗺️ : " + location)

        for period in valid_periods:

            write_output(
                "Realization Period 🗓️ : "
                + period[0]
                + " - "
                + period[1]
            )

            write_output(
                "Slot : "
                + period[2]
            )

        write_output("Price : " + price)
        write_output("Link : " + link)
        write_output("")


file.close()

driver.quit()