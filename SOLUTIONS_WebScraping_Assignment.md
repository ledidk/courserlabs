# 📘 Solutions: Final Assignment — Extracting Stock Data Using Web Scraping

---

## 🎯 Objective
Extract Amazon historical stock data from a web page using **BeautifulSoup** and **pandas**, then answer quiz questions based on the extracted data.

---

## ⚙️ Setup

```python
import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import StringIO
import warnings
warnings.filterwarnings("ignore")
```

---

## 📥 Step 1 — Download the Web Page

```python
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"

html_data = requests.get(url).text
```

---

## 🔍 Step 2 — Parse HTML with BeautifulSoup

```python
soup = BeautifulSoup(html_data, 'html.parser')
```

---

## ✅ Question 1 — What is the content of the title tag?

```python
soup.title.string
```

**✅ Answer:**
```
Amazon.com, Inc. (AMZN) Stock Historical Prices & Data - Yahoo Finance
```

---

## 📊 Step 3 — Extract Table into DataFrame

```python
amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date      = col[0].text
    Open      = col[1].text
    high      = col[2].text
    low       = col[3].text
    close     = col[4].text
    adj_close = col[5].text
    volume    = col[6].text

    amazon_data = pd.concat([
        amazon_data,
        pd.DataFrame({
            "Date":      [date],
            "Open":      [Open],
            "High":      [high],
            "Low":       [low],
            "Close":     [close],
            "Adj Close": [adj_close],
            "Volume":    [volume]
        })
    ], ignore_index=True)
```

---

## ✅ Question 2 — What are the names of the columns in the DataFrame?

```python
list(amazon_data.columns)
```

**✅ Answer:**
```
['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
```

---

## 📋 First 5 Rows of amazon_data

```python
amazon_data.head()
```

| # | Date | Open | High | Low | Close | Volume | Adj Close |
|---|---|---|---|---|---|---|---|
| 0 | Jan 01, 2021 | 3,270.00 | 3,363.89 | 3,086.00 | 3,206.20 | 71,528,900 | 3,206.20 |
| 1 | Dec 01, 2020 | 3,188.50 | 3,350.65 | 3,072.82 | 3,256.93 | 77,556,200 | 3,256.93 |
| 2 | Nov 01, 2020 | 3,061.74 | 3,366.80 | 2,950.12 | 3,168.04 | 90,810,500 | 3,168.04 |
| 3 | Oct 01, 2020 | 3,208.00 | 3,496.24 | 3,019.00 | 3,036.15 | 116,226,100 | 3,036.15 |
| 4 | Sep 01, 2020 | 3,489.58 | 3,552.25 | 2,871.00 | 3,148.73 | 115,899,300 | 3,148.73 |

---

## ✅ Question 3 — What is the `Open` of the last row of amazon_data?

```python
amazon_data.iloc[-1]['Open']
```

**Last row (row 60):**

| Date | Open | High | Low | Close | Volume | Adj Close |
|---|---|---|---|---|---|---|
| Jan 01, 2016 | **656.29** | 657.72 | 547.18 | 587.00 | 130,200,900 | 587.00 |

**✅ Answer: `656.29`**

---

## 📌 Summary of All Answers

| Question | Answer |
|---|---|
| **Q1** Title tag content | `Amazon.com, Inc. (AMZN) Stock Historical Prices & Data - Yahoo Finance` |
| **Q2** Column names | `Date, Open, High, Low, Close, Volume, Adj Close` |
| **Q3** Open of last row | **`656.29`** (Date: Jan 01, 2016) |

---

## 🔄 Alternative Method — Using pandas read_html

```python
from io import StringIO

# Method 1: directly from URL
read_html_pandas_data = pd.read_html(url)

# Method 2: from BeautifulSoup object
read_html_pandas_data = pd.read_html(StringIO(str(soup)))

# Get the first (only) table
amazon_dataframe = read_html_pandas_data[0]
amazon_dataframe.head()
```

---

## 👨‍💻 Authors
- Joseph Santarcangelo (IBM)
- Azim Hirjani
- Akansha Yadav

© IBM Corporation 2020. Released under MIT License.
