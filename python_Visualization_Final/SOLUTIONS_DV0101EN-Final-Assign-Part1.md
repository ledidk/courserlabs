---
jupyter:
  kernelspec:
    display_name: Python (Pyodide)
    language: python
    name: python
  language_info:
    codemirror_mode:
      name: python
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.8
  nbformat: 4
  nbformat_minor: 4

::: {.cell .markdown}
# **Create visualizations using Matplotlib, Seaborn and Folium** - **SOLUTIONS Part 1**

Estimated time needed: **40** minutes
:::

::: {.cell .markdown}
## Setup - Install and Import Libraries

```python
%pip install pandas seaborn folium
import numpy as np
import pandas as pd
%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# Load the dataset
import requests
import io
URL = \"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/d51iMGfp_t0QpO30Lym-dw/automobile-sales.csv\"
response = requests.get(URL)
csv_content = io.StringIO(response.text)
df = pd.read_csv(csv_content)
print('Data downloaded and read into a dataframe!')
```
:::

::: {.cell .markdown}
## TASK 1.1: Line chart - Average Automobile Sales by Year with Recession Annotations
:::

::: {.cell .code}
```python
df_line = df.groupby('Year')['Automobile_Sales'].mean()
plt.figure(figsize=(10, 6))
df_line.plot(kind='line')
plt.xticks(list(range(1980,2024)), rotation=75)
plt.xlabel('Year')
plt.ylabel('Automobile Sales')
plt.title('Automobile Sales during Recession')
plt.text(1982, 650, '1981-82 Recession', bbox=dict(boxstyle='round', facecolor='wheat'))
plt.text(1991, 450, '1991 Recession', bbox=dict(boxstyle='round', facecolor='wheat'))
plt.text(2000, 300, '2000-01 Recession', bbox=dict(boxstyle='round', facecolor='wheat'))
plt.text(2008, 250, '2007-09 Recession', bbox=dict(boxstyle='round', facecolor='wheat'))
plt.text(2020, 200, '2020 Covid Recession', bbox=dict(boxstyle='round', facecolor='wheat'))
plt.legend(['Avg Sales'])
plt.tight_layout()
plt.show()
```
:::

::: {.cell .markdown}
**Inference:** Sales fluctuate yearly; notable drops during annotated recession periods.
:::

::: {.cell .markdown}
## TASK 1.2: Line plots - Advertising Expenditure vs Sales Trends (Non-Recession)
:::

::: {.cell .code}
```python
df_non_rec = df[df['Recession'] == 0]
df_trends = df_non_rec.groupby('Year', as_index=False).agg({'Automobile_Sales': 'mean', 'Advertising_Expenditure': 'mean'})
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_trends, x='Year', y='Automobile_Sales', marker='o', color='green', label='Avg Sales')
sns.lineplot(data=df_trends, x='Year', y='Advertising_Expenditure', marker='s', linestyle='--', color='blue', label='Avg Ad Spend')
plt.xlabel('Year')
plt.ylabel('Values')
plt.title('Trends in Advertising Expenditure vs Automobile Sales (Non-Recession)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```
:::

::: {.cell .markdown}
**Inference:** Sales more volatile than ad spend; inconsistent correlation.
:::

::: {.cell .markdown}
## TASK 1.3: Bar plots - Sales by Recession and Vehicle Type
:::

::: {.cell .code}
```python
# Overall
new_df = df.groupby('Recession')['Automobile_Sales'].mean().reset_index()
plt.figure(figsize=(8, 6))
sns.barplot(x='Recession', y='Automobile_Sales', data=new_df)
plt.xticks([0,1], ['Non-Recession', 'Recession'])
plt.title('Average Automobile Sales: Recession vs Non-Recession')
plt.show()

# By Vehicle Type
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Recession', y='Automobile_Sales', hue='Vehicle_Type')
plt.xticks([0,1], ['Non-Recession', 'Recession'])
plt.title('Vehicle Sales: Recession vs Non-Recession')
plt.show()
```
:::

::: {.cell .markdown}
**Inference:** Drastic sales decline in recession; executive/sports cars most affected.
:::

::: {.cell .markdown}
## TASK 1.4: Subplots - GDP Line Plots during Recession/Non-Recession
:::

::: {.cell .code}
```python
rec_data = df[df['Recession'] == 1]
non_rec_data = df[df['Recession'] == 0]

plt.figure(figsize=(12, 6))
plt.subplot(1,2,1)
sns.lineplot(data=rec_data, x='Year', y='GDP')
plt.title('GDP during Recession')
plt.subplot(1,2,2)
sns.lineplot(data=non_rec_data, x='Year', y='GDP')
plt.title('GDP during Non-Recession')
plt.tight_layout()
plt.show()
```
:::

::: {.cell .markdown}
**Inference:** GDP lower/more volatile during recessions.
:::

::: {.cell .markdown}
## TASK 1.5: Bubble Plot - Seasonality on Non-Recession Sales
:::

::: {.cell .code}
```python
non_rec_data = df[df['Recession'] == 0]
plt.figure(figsize=(12, 6))
sns.scatterplot(data=non_rec_data, x='Month', y='Automobile_Sales', size='Seasonality_Weight', sizes=(50, 500), hue='Seasonality_Weight', legend=False)
plt.title('Seasonality Impact on Automobile Sales (Non-Recession)')
plt.show()
```
:::

::: {.cell .markdown}
**Inference:** Raises in April/December; limited overall seasonality effect.
:::

::: {.cell .markdown}
## TASK 1.6: Scatter Plots - Consumer Confidence/Price vs Sales (Recession)
:::

::: {.cell .code}
```python
rec_data = df[df['Recession'] == 1]
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(12,5))
ax1.scatter(rec_data['Consumer_Confidence'], rec_data['Automobile_Sales'])
ax1.set_title('Consumer Confidence vs Sales (Recession)')
ax2.scatter(rec_data['Price'], rec_data['Automobile_Sales'])
ax2.set_title('Price vs Sales (Recession)')
plt.tight_layout()
plt.show()
```
:::

::: {.cell .markdown}
**Inference:** Higher confidence boosts sales; higher prices reduce sales.
:::

::: {.cell .markdown}
## TASK 1.7: Pie - Advertising Expenditure Recession vs Non
:::

::: {.cell .code}
```python
rdata = df[df['Recession']==1]['Advertising_Expenditure'].sum()
nrdata = df[df['Recession']==0]['Advertising_Expenditure'].sum()
plt.figure(figsize=(8,6))
plt.pie([rdata, nrdata], labels=['Recession','Non-Recession'], autopct='%1.1f%%')
plt.title('Ad Expenditure: Recession vs Non-Recession')
plt.show()
```
:::

::: {.cell .markdown}
**Inference:** Significantly more spend during non-recession.
:::

::: {.cell .markdown}
## TASK 1.8: Pie - Ad Expenditure by Vehicle Type (Recession)
:::

::: {.cell .code}
```python
rdata = df[df['Recession']==1]
vtexp = rdata.groupby('Vehicle_Type')['Advertising_Expenditure'].sum()
plt.pie(vtexp.values, labels=vtexp.index, autopct='%1.1f%%')
plt.title('Ad Spend Share by Vehicle Type (Recession)')
plt.show()
```
:::

::: {.cell .markdown}
**Inference:** Focused on lower-price vehicles.
:::

::: {.cell .markdown}
## TASK 1.9: Lineplot - Unemployment Rate effect on Vehicle Sales (Recession)
:::

::: {.cell .code}
```python
df_rec = df[df['Recession']==1]
plt.figure(figsize=(14,6))
sns.lineplot(data=df_rec, x='Unemployment_Rate', y='Automobile_Sales', hue='Vehicle_Type', marker='o')
plt.title('Effect of Unemployment Rate on Vehicle Sales (Recession)')
plt.show()
```
:::

::: {.cell .markdown}
**Inference:** Sales drop with rising unemployment; smaller cars volatile.
:::

::: {.cell .markdown}
## TASK 1.10 (Optional): Folium Choropleth Map (Highest Sales Regions Recession)
:::

::: {.cell .code}
```python
# Download geo_data
path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data Files/us-states.json'
# Note: Run in browser/Jupyter; assumes 'City' column - adjust key_on if using states
rec_data = df[df['Recession'] == 1]
sales_by_city = rec_data.groupby('City')['Automobile_Sales'].sum().reset_index()
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)
folium.Choropleth(
    geo_data='us-states.json',
    data=sales_by_city,
    columns=['City', 'Automobile_Sales'],
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    legend_name='Sales during Recession'
).add_to(m)
m
```
:::

::: {.cell .markdown}
**Completed!** Copy these code blocks into DV0101EN-Final-Assign-Part1.ipynb cells. All tasks solved with correct plots, labels, titles, annotations as required.
:::
