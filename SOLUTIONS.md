# 📘 Solutions Document
## Python Project: Web Scraping & Stock Data Extraction

---

## 📁 Project Structure

```
python_stock_scraping_project/
├── venv/                          ← Python virtual environment
├── WebScraping_Review_Lab.ipynb   ← Lab 1: BeautifulSoup exercises
├── Final_Assignment Library.ipynb ← Lab 2: yfinance assignment
├── solutions.py                   ← Python script with all solutions
└── SOLUTIONS.md                   ← This document
```

---

## ⚙️ Setup Instructions

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate it (Windows)
venv\Scripts\activate

# 3. Install all dependencies
pip install yfinance beautifulsoup4 requests pandas matplotlib lxml html5lib

# 4. Run the solutions script
python solutions.py
```

---

---

# PART 1 — Web Scraping Lab (BeautifulSoup)

## 🔧 Setup

```python
from bs4 import BeautifulSoup
import requests

html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body>" \
       "<h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p>" \
       "<h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p>" \
       "<h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

soup = BeautifulSoup(html, "html.parser")
```

---

## 🏷️ Tags

```python
tag_object = soup.h3        # → <h3><b id="boldest">Lebron James</b></h3>
tag_child  = tag_object.b   # → <b id="boldest">Lebron James</b>
```

**Output:**
```
soup.title        : <title>Page Title</title>
soup.h3           : <h3><b id="boldest">Lebron James</b></h3>
tag_object.b      : <b id="boldest">Lebron James</b>
```

---

## 🌳 Children, Parents, and Siblings

```python
tag_child.parent        # → <h3><b id="boldest">Lebron James</b></h3>
tag_object.parent.name  # → body

sibling_1 = tag_object.next_sibling   # → <p> Salary: $ 92,000,000 </p>
sibling_2 = sibling_1.next_sibling    # → <h3> Stephen Curry</h3>
```

---

## ✅ Exercise 1 — Find Stephen Curry's Salary

**Task:** Using `sibling_2` and `next_sibling`, find Stephen Curry's salary.

```python
sibling_2.next_sibling
```

**Answer:**
```
<p> Salary: $85,000, 000 </p>
```

---

## 🔑 HTML Attributes

```python
tag_child['id']       # → 'boldest'
tag_child.attrs       # → {'id': 'boldest'}
tag_child.get('id')   # → 'boldest'
```

---

## 📝 NavigableString

```python
tag_string = tag_child.string
# → 'Lebron James'
# type: <class 'bs4.element.NavigableString'>

unicode_string = str(tag_string)
# → 'Lebron James'
```

---

## 🔍 Filter Section — find_all() and find()

### Setup (Rocket Launch Table)

```python
table_html = "<table>..." # rocket launch HTML
table_bs = BeautifulSoup(table_html, "html.parser")
```

### find_all by tag name

```python
table_rows = table_bs.find_all('tr')
# Returns 4 rows: header + 3 data rows
```

**Output:**
```
row 0: <tr><td id="flight">Flight No</td><td>Launch site</td><td>Payload mass</td></tr>
row 1: <tr><td>1</td><td><a href="...Florida">Florida</a></td><td>300 kg</td></tr>
row 2: <tr><td>2</td><td><a href="...Texas">Texas</a></td><td>94 kg</td></tr>
row 3: <tr><td>3</td><td><a href="...Florida">Florida</a></td><td>80 kg</td></tr>
```

### find_all by attribute

```python
table_bs.find_all(id="flight")
# → [<td id="flight">Flight No</td>]

table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
# → [<a href="...">Florida</a>, <a href="...">Florida</a>]

table_bs.find_all(href=True)
# → All 3 anchor tags (Florida, Texas, Florida)

table_bs.find_all(string="Florida")
# → ['Florida', 'Florida']
```

---

## ✅ Exercise 2 — find_all Elements WITHOUT href

**Task:** Find all `<a>` elements without an `href` value.

```python
table_bs.find_all('a', href=False)
```

**Answer:**
```
[]   ← (all <a> tags in this table have href values)
```

---

## ✅ Exercise 3 — Find Element with id="boldest"

**Task:** Using the `soup` object, find the element with `id="boldest"`.

```python
soup.find_all(id="boldest")
```

**Answer:**
```
[<b id="boldest">Lebron James</b>]
```

---

## 🔎 find() — Two Tables Example

```python
two_tables_bs.find("table")
# → Returns the FIRST table (rocket table)

two_tables_bs.find("table", class_='pizza')
# → Returns the pizza table specifically
```

---

---

# PART 2 — Final Assignment: Extracting Stock Data Using yfinance

## 🔧 Setup

```python
import yfinance as yf
import pandas as pd
```

---

## 🍎 Apple (AAPL) — Guided Example

```python
apple = yf.Ticker("AAPL")
apple_info = apple.info
```

### Stock Info
```python
apple_info['country']   # → 'United States'
apple_info['sector']    # → 'Technology'
```

### Historical Share Price
```python
apple_share_price_data = apple.history(period="max")
apple_share_price_data.reset_index(inplace=True)
apple_share_price_data.head()
```

**Output (first 3 rows):**
```
Date                        Open      High       Low     Close      Volume
1980-12-12 00:00:00-05:00   0.0983    0.0987    0.0983    0.0983    469,033,600
1980-12-15 00:00:00-05:00   0.0936    0.0936    0.0932    0.0932    175,884,800
1980-12-16 00:00:00-05:00   0.0868    0.0868    0.0863    0.0863    105,728,000
```

### Dividends
```python
apple.dividends
```

**Output (last 5 dividends):**
```
Date
2025-02-10    0.25
2025-05-12    0.26
2025-08-11    0.26
2025-11-10    0.26
2026-02-09    0.26
Name: Dividends, dtype: float64
```

---

## 🔴 AMD (Advanced Micro Devices) — Assignment Exercise

```python
amd = yf.Ticker("AMD")
amd_info = amd.info
```

---

### ✅ Question 1 — Country

**Task:** Use the key `'country'` to find the country the AMD stock belongs to.

```python
amd_info['country']
```

**✅ Answer: `United States`**

---

### ✅ Question 2 — Sector

**Task:** Use the key `'sector'` to find the sector the AMD stock belongs to.

```python
amd_info['sector']
```

**✅ Answer: `Technology`**

---

### ✅ Question 3 — Volume on First Day

**Task:** Obtain stock data for AMD using `history(period="max")` and find the Volume traded on the first day.

```python
amd_share_price_data = amd.history(period="max")
amd_share_price_data.reset_index(inplace=True)
amd_share_price_data.iloc[0]['Volume']
```

**Output (first 3 rows):**
```
Date                        Open      High       Low     Close    Volume
1980-03-17 00:00:00-05:00   3.1250    3.3021    3.1250    3.1458    219,600
1980-03-18 00:00:00-05:00   3.1250    3.1250    2.9375    3.0313    727,200
1980-03-19 00:00:00-05:00   3.0313    3.0833    3.0208    3.0417    295,200
```

**✅ Answer:**
- **First Day Date:** `1980-03-17`
- **Volume Traded:** `219,600`

---

## 📊 Summary of Assignment Answers

| Question | Answer |
|---|---|
| **Q1** AMD Country | **United States** |
| **Q2** AMD Sector | **Technology** |
| **Q3** AMD First Day Volume | **219,600** (on 1980-03-17) |

---

## 👨‍💻 Authors
- Joseph Santarcangelo (IBM)
- Azim Hirjani
- Ramesh Sannareddy

