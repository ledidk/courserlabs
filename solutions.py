"""
=============================================================
  SOLUTIONS SCRIPT
  Covers:
    1. WebScraping_Review_Lab  - BeautifulSoup exercises
    2. Final_Assignment Library - yfinance stock data exercises
=============================================================
"""

import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────────────────────
# PART 1 — WEB SCRAPING LAB (BeautifulSoup)
# ─────────────────────────────────────────────────────────────

print("=" * 60)
print("PART 1: WEB SCRAPING LAB — BeautifulSoup")
print("=" * 60)

from bs4 import BeautifulSoup
import requests

# ── HTML used in the lab ──────────────────────────────────────
html = (
    "<!DOCTYPE html><html><head><title>Page Title</title></head>"
    "<body>"
    "<h3><b id='boldest'>Lebron James</b></h3>"
    "<p> Salary: $ 92,000,000 </p>"
    "<h3> Stephen Curry</h3>"
    "<p> Salary: $85,000, 000 </p>"
    "<h3> Kevin Durant </h3>"
    "<p> Salary: $73,200, 000</p>"
    "</body></html>"
)

soup = BeautifulSoup(html, "html.parser")

# ── Tags ──────────────────────────────────────────────────────
tag_object = soup.h3          # first <h3> → Lebron James
tag_child  = tag_object.b     # <b> inside <h3>

print("\n[Tags]")
print("  soup.title        :", soup.title)
print("  soup.h3 (tag_obj) :", tag_object)
print("  tag_object.b      :", tag_child)

# ── Children / Parents / Siblings ────────────────────────────
print("\n[Children / Parents / Siblings]")
print("  tag_child.parent  :", tag_child.parent)
print("  tag_object.parent :", tag_object.parent.name)   # body

sibling_1 = tag_object.next_sibling   # <p> Salary: $ 92,000,000
sibling_2 = sibling_1.next_sibling    # <h3> Stephen Curry

print("  sibling_1 (next)  :", sibling_1)
print("  sibling_2 (next)  :", sibling_2)

# ── EXERCISE 1: Find Stephen Curry's salary ──────────────────
print("\n[Exercise 1] Stephen Curry's salary:")
stephen_curry_salary = sibling_2.next_sibling
print(" ", stephen_curry_salary)

# ── HTML Attributes ───────────────────────────────────────────
print("\n[HTML Attributes]")
print("  tag_child['id']   :", tag_child['id'])
print("  tag_child.attrs   :", tag_child.attrs)
print("  tag_child.get('id'):", tag_child.get('id'))

# ── NavigableString ───────────────────────────────────────────
print("\n[NavigableString]")
tag_string = tag_child.string
print("  tag_child.string  :", tag_string)
print("  type              :", type(tag_string))
print("  as str            :", str(tag_string))

# ─────────────────────────────────────────────────────────────
# FILTER SECTION — Rocket launch table
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("FILTER SECTION — find_all / find")
print("=" * 60)

table_html = (
    "<table>"
    "<tr><td id='flight'>Flight No</td><td>Launch site</td><td>Payload mass</td></tr>"
    "<tr><td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td><td>300 kg</td></tr>"
    "<tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr>"
    "<tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td><td>80 kg</td></tr>"
    "</table>"
)

table_bs = BeautifulSoup(table_html, "html.parser")

print("\n[find_all('tr')]")
table_rows = table_bs.find_all('tr')
for i, row in enumerate(table_rows):
    print(f"  row {i}: {row}")

print("\n[find_all by id='flight']")
print(" ", table_bs.find_all(id="flight"))

print("\n[find_all href=Florida Wikipedia]")
print(" ", table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida"))

print("\n[find_all href=True (all links)]")
print(" ", table_bs.find_all(href=True))

print("\n[find_all string='Florida']")
print(" ", table_bs.find_all(string="Florida"))

# ── EXERCISE 2: find_all elements WITHOUT href ────────────────
print("\n[Exercise 2] Elements without href:")
print(" ", table_bs.find_all('a', href=False))

# ── EXERCISE 3: find element with id='boldest' ────────────────
print("\n[Exercise 3] Element with id='boldest':")
print(" ", soup.find_all(id="boldest"))

# ── Two-table find() demo ─────────────────────────────────────
two_tables_html = (
    "<h3>Rocket Launch</h3>"
    "<p><table class='rocket'>"
    "<tr><td>Flight No</td><td>Launch site</td><td>Payload mass</td></tr>"
    "<tr><td>1</td><td>Florida</td><td>300 kg</td></tr>"
    "</table></p>"
    "<p><h3>Pizza Party</h3>"
    "<table class='pizza'>"
    "<tr><td>Pizza Place</td><td>Orders</td><td>Slices</td></tr>"
    "<tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr>"
    "</table></p>"
)
two_tables_bs = BeautifulSoup(two_tables_html, "html.parser")

print("\n[find() — first table]")
print(" ", two_tables_bs.find("table"))

print("\n[find() — pizza table by class]")
print(" ", two_tables_bs.find("table", class_='pizza'))


# ─────────────────────────────────────────────────────────────
# PART 2 — FINAL ASSIGNMENT: yfinance Stock Data
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("PART 2: FINAL ASSIGNMENT — yfinance Stock Data")
print("=" * 60)

try:
    import yfinance as yf
    import pandas as pd
    import json

    # ── Apple (AAPL) — Guided Example ────────────────────────
    print("\n--- Apple (AAPL) ---")
    apple = yf.Ticker("AAPL")

    # Stock Info
    apple_info = apple.info
    print("  Country :", apple_info.get('country', 'N/A'))
    print("  Sector  :", apple_info.get('sector', 'N/A'))

    # Historical Share Price
    apple_share_price_data = apple.history(period="max")
    apple_share_price_data.reset_index(inplace=True)
    print("\n  Apple Share Price (first 3 rows):")
    print(apple_share_price_data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']].head(3).to_string(index=False))

    # Dividends
    print("\n  Apple Dividends (last 5):")
    print(apple.dividends.tail(5))

    # ── AMD — Assignment Exercise ─────────────────────────────
    print("\n--- AMD (Advanced Micro Devices) ---")
    amd = yf.Ticker("AMD")

    amd_info = amd.info

    # QUESTION 1: Country
    amd_country = amd_info.get('country', 'N/A')
    print(f"\n  [Q1] Country the AMD stock belongs to: {amd_country}")

    # QUESTION 2: Sector
    amd_sector = amd_info.get('sector', 'N/A')
    print(f"  [Q2] Sector the AMD stock belongs to  : {amd_sector}")

    # QUESTION 3: Volume on first day
    amd_share_price_data = amd.history(period="max")
    amd_share_price_data.reset_index(inplace=True)
    first_day_volume = amd_share_price_data.iloc[0]['Volume']
    first_day_date   = amd_share_price_data.iloc[0]['Date']
    print(f"  [Q3] Volume traded on first day ({first_day_date.date()}): {int(first_day_volume):,}")

    print("\n  AMD Share Price (first 3 rows):")
    print(amd_share_price_data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']].head(3).to_string(index=False))

    print("\n  AMD Dividends (last 5):")
    print(amd.dividends.tail(5))

except ImportError:
    print("\n  [!] yfinance not yet installed. Run:")
    print("      venv/Scripts/pip install yfinance")
except Exception as e:
    print(f"\n  [!] Error fetching stock data: {e}")


print("\n" + "=" * 60)
print("ALL SOLUTIONS COMPLETE")
print("=" * 60)
