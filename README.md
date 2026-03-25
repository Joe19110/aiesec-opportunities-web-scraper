# AIESEC Opportunity Scraper

This script collects Global Volunteer opportunities from the AIESEC website  
and saves them into a text file named:

list_opportunities.txt


## Requirements

Install Python  
Download from:

https://www.python.org/downloads/

During installation:

Enable **Add Python to PATH**


Install required packages:

```
pip install selenium webdriver-manager
```


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

This number is the country code. (Check your aiesec.org url after filtering for your specific country)

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
(LEAVE THE SCRIPT RUNNING, DO NOT RESIZE THE WINDOW THAT POPS UP)

estimated waiting time around 1 min / 5 opps

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
