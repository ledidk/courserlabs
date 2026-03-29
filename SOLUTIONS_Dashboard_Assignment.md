# 📘 Solutions: Extracting and Visualizing Stock Data (Revenue & Dashboard)

---

## 🎯 Objective
Extract stock price data using **yfinance** and revenue data using **BeautifulSoup** web scraping for **Tesla (TSLA)** and **GameStop (GME)**, then visualize them using the `make_graph` function.

---

## ⚙️ Setup

```python
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
```

---

## 📊 Graph Function (Pre-defined)

```python
import matplotlib.pyplot as plt

def make_graph(stock_data, revenue_data, stock):
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']

    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    axes[0].plot(pd.to_datetime(stock_data_specific.Date), stock_data_specific.Close.astype("float"), label="Share Price", color="blue")
    axes[0].set_ylabel("Price ($US)")
    axes[0].set_title(f"{stock} - Historical Share Price")

    axes[1].plot(pd.to_datetime(revenue_data_specific.Date), revenue_data_specific.Revenue.astype("float"), label="Revenue", color="green")
    axes[1].set_ylabel("Revenue ($US Millions)")
    axes[1].set_xlabel("Date")
    axes[1].set_title(f"{stock} - Historical Revenue")

    plt.tight_layout()
    plt.show()
```

---

---

## ✅ Question 1 — Use yfinance to Extract Tesla Stock Data

```python
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
tesla_data.head()
```

**Output (First 5 rows):**

| # | Date | Open | High | Low | Close | Volume |
|---|---|---|---|---|---|---|
| 0 | 2010-06-29 | 1.2667 | 1.6667 | 1.1693 | 1.5927 | 281,494,500 |
| 1 | 2010-06-30 | 1.7193 | 2.0280 | 1.5533 | 1.5887 | 257,806,500 |
| 2 | 2010-07-01 | 1.6667 | 1.7280 | 1.3513 | 1.4640 | 123,282,000 |
| 3 | 2010-07-02 | 1.5333 | 1.5400 | 1.2473 | 1.2800 | 77,097,000 |
| 4 | 2010-07-06 | 1.3333 | 1.3333 | 1.0553 | 1.0740 | 103,003,500 |

> Tesla IPO date: **June 29, 2010** | Starting price: ~$1.59

---

## ✅ Question 2 — Use Web Scraping to Extract Tesla Revenue Data

```python
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html.parser')

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for row in soup.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    if len(col) >= 2:
        date    = col[0].text.strip()
        revenue = col[1].text.strip()
        tesla_revenue = pd.concat([
            tesla_revenue,
            pd.DataFrame({"Date": [date], "Revenue": [revenue]})
        ], ignore_index=True)

# Clean the Revenue column
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(',|\$', '', regex=True)
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue["Revenue"] != ""]

tesla_revenue.tail()
```

**Output (Last 5 rows of tesla_revenue):**

| # | Date | Revenue |
|---|---|---|
| 48 | 2010-09-30 | 31 |
| 49 | 2010-06-30 | 28 |
| 50 | 2010-03-31 | 21 |
| 52 | 2009-09-30 | 46 |
| 53 | 2009-06-30 | 27 |

> Revenue values are in **$US Millions**. Earliest data goes back to **Q2 2009**.

---

## ✅ Question 3 — Use yfinance to Extract GameStop Stock Data

```python
gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)
gme_data.head()
```

**Output (First 5 rows):**

| # | Date | Open | High | Low | Close | Volume |
|---|---|---|---|---|---|---|
| 0 | 2002-02-13 | 1.6201 | 1.6934 | 1.6033 | 1.6917 | 76,216,000 |
| 1 | 2002-02-14 | 1.7127 | 1.7161 | 1.6706 | 1.6833 | 11,021,600 |
| 2 | 2002-02-15 | 1.6833 | 1.6875 | 1.6580 | 1.6748 | 8,389,600 |
| 3 | 2002-02-19 | 1.6664 | 1.6664 | 1.5780 | 1.6075 | 7,410,400 |
| 4 | 2002-02-20 | 1.6159 | 1.6622 | 1.6033 | 1.6622 | 6,892,800 |

> GameStop first listed: **February 13, 2002**

---

## ✅ Question 4 — Use Web Scraping to Extract GameStop Revenue Data

```python
url_gme = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data_2 = requests.get(url_gme).text
soup2 = BeautifulSoup(html_data_2, 'html.parser')

gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for row in soup2.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    if len(col) >= 2:
        date    = col[0].text.strip()
        revenue = col[1].text.strip()
        gme_revenue = pd.concat([
            gme_revenue,
            pd.DataFrame({"Date": [date], "Revenue": [revenue]})
        ], ignore_index=True)

# Clean the Revenue column
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(',|\$', '', regex=True)
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue["Revenue"] != ""]

gme_revenue.tail()
```

**Output (Last 5 rows of gme_revenue):**

| # | Date | Revenue |
|---|---|---|
| 57 | 2006-01-31 | 1667 |
| 58 | 2005-10-31 | 534 |
| 59 | 2005-07-31 | 416 |
| 60 | 2005-04-30 | 475 |
| 61 | 2005-01-31 | 709 |

> Revenue values are in **$US Millions**. Earliest data goes back to **Q1 2005**.

---

## ✅ Question 5 — Plot Tesla Stock Graph

```python
make_graph(tesla_data, tesla_revenue, 'Tesla')
```

**What the graph shows:**
- **Top panel:** Tesla share price (Close) from IPO (2010) up to June 2021 — shows massive growth from ~$1.59 to ~$600+
- **Bottom panel:** Tesla quarterly revenue from 2009 to April 2021 — shows steady revenue growth from $27M to over $10,000M

---

## ✅ Question 6 — Plot GameStop Stock Graph

```python
make_graph(gme_data, gme_revenue, 'GameStop')
```

**What the graph shows:**
- **Top panel:** GameStop share price from 2002 up to June 2021 — shows the famous **short squeeze spike** in early 2021 where price surged from ~$20 to ~$400+
- **Bottom panel:** GameStop quarterly revenue from 2005 to April 2021 — shows declining revenue trend as physical game retail declined

---

## 📌 Summary Table

| Question | Task | Key Result |
|---|---|---|
| **Q1** | Tesla stock via yfinance | First date: 2010-06-29, Open: $1.27 |
| **Q2** | Tesla revenue via scraping | Earliest: Q2 2009 ($27M), cleaned & formatted |
| **Q3** | GameStop stock via yfinance | First date: 2002-02-13, Open: $1.62 |
| **Q4** | GameStop revenue via scraping | Earliest: Q1 2005 ($709M), cleaned & formatted |
| **Q5** | Tesla graph | `make_graph(tesla_data, tesla_revenue, 'Tesla')` |
| **Q6** | GameStop graph | `make_graph(gme_data, gme_revenue, 'GameStop')` |

---

## 🔑 Key Concepts Used

| Concept | Usage |
|---|---|
| `yf.Ticker("TSLA")` | Create ticker object for Tesla |
| `.history(period="max")` | Get all historical stock data |
| `reset_index(inplace=True)` | Move Date from index to column |
| `requests.get(url).text` | Download HTML page |
| `BeautifulSoup(html, 'html.parser')` | Parse HTML |
| `soup.find_all("tbody")[1]` | Get second table body (revenue table) |
| `.str.replace(',|\$','',regex=True)` | Clean currency formatting |
| `make_graph(stock, revenue, name)` | Plot dual-panel dashboard |

---

## 👨‍💻 Authors
- Joseph Santarcangelo (IBM)
- Azim Hirjani

© IBM Corporation 2020. All rights reserved.
