# AIESEC Opportunity Scraper

This script collects Global Volunteer opportunities from the AIESEC website  
and saves them into a text file named:

list_opportunities.txt


## Requirements

### 1. Install Python (Skip if already installed)

Download Python from:

https://www.python.org/downloads/

During installation:

Enable **Add Python to PATH**

To check if Python is already installed, open Command Prompt and run:

```
python --version
```

If a version number appears, Python is already installed and you can skip installation.


### 2. Install Required Dependencies

Open Command Prompt and run:

```
pip install selenium webdriver-manager
```

This installs:

- selenium (controls the browser)  
- webdriver-manager (automatically installs Chrome driver)


### 3. Use Google Chrome

This script uses **Google Chrome** as the browser.

Make sure Chrome is installed:

https://www.google.com/chrome/


## Files Needed

Place these in the same folder:

```
aiesec-web-scraper.py
README.md
```


## Change Country

Open:

```
aiesec-web-scraper.py
```

Find this section near the top:

```
SEARCH_URL = (
"https://aiesec.org/search"
"?home_mcs=1609"
"&programmes=7"
"&earliest_start_date=2026-7-01"
)
```

Change the number after:

```
home_mcs=
```

This number is the country code.

To get the correct number:

1. Go to aiesec.org  
2. Filter by your country  
3. Look at the URL  
4. Copy the number after:

```
home_mcs=
```

Example:

```
home_mcs=102
```

After changing the number:

Save the file.



## Run the Script

Open Command Prompt.

Go to your script folder:

```
cd C:\Users\YourName\FolderName
```

Example:

```
cd C:\Users\joell
```

Run:

```
python aiesec-web-scraper.py
```

Leave the browser window open.  
Do not resize or close it while the script is running.

Estimated waiting time:

Around **1 minute per 5 opportunities**.



## What the Script Does

The script will:

- Open the AIESEC search page  
- Click **Load more** until all opportunities appear  
- Open each opportunity  
- Collect realization periods  
- Save results into:

```
list_opportunities.txt
```


## Output File

After completion, check:

```
list_opportunities.txt
```

The file appears in the same folder as the script.



## Notes

Each run overwrites:

```
list_opportunities.txt
```

Rename the file before running again if you want to keep older results.
