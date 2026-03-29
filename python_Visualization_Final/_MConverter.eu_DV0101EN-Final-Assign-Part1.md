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
  prev_pub_hash: eb7179ca7ced0d6c0a9cd4ef230fad9d1a254c5c4dc39bc1082807b95ea9d6fb
---

::: {.cell .markdown}
<p style="text-align:center">
    <a href="https://skills.network" target="_blank">
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo">
    </a>
</p>
:::

::: {.cell .markdown}
# **Create visualizations using Matplotib, Seaborn and Folium**

Estimated time needed: **40** minutes

In this assignment, you will have the opportunity to demonstrate the skills you have acquired in creating visualizations using *Matplotlib, Seaborn, Folium*.
`<br>`{=html}
`<br>`{=html}
:::

::: {.cell .markdown}
# **Table of Contents**

<ol>
    <li><a href="#Objectives">Objectives</a></li>
    <li>
        <a href="#Setup">Setup</a>
        <ol>
            <li><a href="#Installing-Required-Libraries">Installing Required Libraries</a></li>
            <li><a href="#Importing-Required-Libraries">Importing Required Libraries</a></li>
            </ol>
    </li>
    <li>
        <a href="#Scenario">Scenario</a>
        <ol>
            <li><a href="#Data Description">Data Description</a></li>
        </ol>
    </li>
    <li><a href="#Importing Data">Importing data</a></li>
    <li><a href="#Creating Visualizations for Data Analysis">Creating Visualizations for Data Analysis</a></li>
</ol>
:::

::: {.cell .markdown}
# Objectives

After completing this lab you will be able to:

- Create informative and visually appealing plots with Matplotlib and Seaborn.
- Apply visualization to communicate insights from the data.
- Analyze data through using visualizations.
- Customize visualizations
:::

::: {.cell .markdown}
# Setup
:::

::: {.cell .markdown}
For this lab, we will be using the following libraries:

- [`pandas`](https://pandas.pydata.org/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMML0187ENSkillsNetwork31430127-2021-01-01) for managing the data.
- [`numpy`](https://numpy.org/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMML0187ENSkillsNetwork31430127-2021-01-01) for mathematical operations.
- [`matplotlib`](https://matplotlib.org/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMML0187ENSkillsNetwork31430127-2021-01-01) for plotting.
- [`seaborn`](https://seaborn.pydata.org/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMML0187ENSkillsNetwork31430127-2021-01-01) for plotting.
- [`Folium`](https://python-visualization.github.io/folium/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMML0187ENSkillsNetwork31430127-2021-01-01) for plotting.
:::

::: {.cell .markdown}
### Installing Required Libraries
:::

::: {.cell .code}
``` python
%pip install pandas
%pip install numpy
%pip install seaborn
%pip install folium
```
:::

::: {.cell .markdown}
### Importing Required Libraries

*We recommend you import all required libraries in one place (here):*
:::

::: {.cell .code}
``` python
import numpy as np
import pandas as pd
%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import folium
```
:::

::: {.cell .markdown}
<details><summary>Click here for a hint</summary>
&#10;<p>
You will require:-
<br>Numpy for many scientific computing in Python
<br>Pandas for creating and working on dataframe, also for plotting directly on dataframe/series
<br>The inline backend to generate the plots within the browser [%matplotlib inline]
<br>Matplotlib and its pyplot pacakge for plotting
<br>Seaborn for plotting
</details>
:::

::: {.cell .markdown}
<details><summary>Click here for python solution</summary>
&#10;```python
    #Import Primary Modules:
    import numpy as np
    import pandas as pd
    %matplotlib inline
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import seaborn as sns
    import folium
```
&#10;</details>
:::

::: {.cell .markdown}

------------------------------------------------------------------------
:::

::: {.cell .markdown}
# Scenario

In this assignment you will be tasked with creating plots which answer questions for analysing \"automobile_sales\" data to understand the historical trends in automobile sales during recession periods.`<br>`{=html}
recession period 1 - year 1980 `<br>`{=html}
recession period 2 - year 1981 to 1982`<br>`{=html}
recession period 3 - year 1991`<br>`{=html}
recession period 4 - year 2000 to 2001`<br>`{=html}
recession period 5 - year end 2007 to mid 2009`<br>`{=html}
recession period 6 - year 2020 -Feb to April (Covid-19 Impact)`<br>`{=html}

# Data Description

The dataset used for this visualization assignment contains *automobile_sales* data representing automobile sales and related variables during recession and non-recession period.

The dataset includes the following variables:
`<br>`{=html}1. Date: The month end date of sales observation.
`<br>`{=html}2. Recession: A binary variable indicating recession perion; 1 means it was recession, 0 means it was normal.
`<br>`{=html}3. Automobile_Sales: The number of vehicles sold during the period.
`<br>`{=html}4. GDP: The per capita GDP value in USD.
`<br>`{=html}5. Unemployment_Rate: The monthly unemployment rate.
`<br>`{=html}6. Consumer_Confidence: A synthetic index representing consumer confidence, which can impact consumer spending and automobile purchases.
`<br>`{=html}7. Seasonality_Weight: The weight representing the seasonality effect on automobile sales during the period. This variable represents the seasonal effect on automobile sales for a given month. In the automobile industry, sales often fluctuate throughout the year due to seasonal patterns---for example, sales may increase during the festive season or year-end promotions, and decrease during off-peak months like post-holiday winter periods.
A value greater than 1 indicates higher-than-average sales expected for that month due to seasonal trends (e.g., holiday season or new model launches).
A value less than 1 suggests lower-than-average sales due to seasonal slowdowns.
A value around 1 means the season has neutral or average effect on sales.
`<br>`{=html}8. Price: The average vehicle price during the period.
`<br>`{=html}9. Advertising_Expenditure: The advertising expenditure of the company.
`<br>`{=html}10.Vehicle_Type: The type of vehicles sold; Supperminicar, Smallfamiliycar, Mediumfamilycar, Executivecar, Sports.
`<br>`{=html}11.Competition: The measure of competition in the market, such as the number of competitors or market share of major manufacturers.
`<br>`{=html}12.Month: Month of the observation extracted from Date..
`<br>`{=html}13.Year: Year of the observation extracted from Date.
`<br>`{=html}
By examining various factors mentioned above from the dataset, you aim to gain insights into how recessions impacted automobile sales for your company.
:::

::: {.cell .markdown}

------------------------------------------------------------------------
:::

::: {.cell .markdown}
# Importing Data
:::

::: {.cell .markdown}
#### For your convenience, we have already written code to import the data below.
:::

::: {.cell .code}
``` python
import requests
import io
import pandas as pd

# URL of the CSV file
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/d51iMGfp_t0QpO30Lym-dw/automobile-sales.csv"

# Fetch the data from the URL
response = requests.get(URL)

# Raise an error if the request failed
response.raise_for_status()

# Convert the response content into a readable format for pandas
csv_content = io.StringIO(response.text)

# Read the CSV data into a pandas dataframe
df = pd.read_csv(csv_content)

# Print confirmation
print('Data downloaded and read into a dataframe!')

# Optional: Show the first few rows of the dataframe
print(df.head())
```
:::

::: {.cell .code}
``` python
df.describe()
```
:::

::: {.cell .code}
``` python
df.columns
```
:::

::: {.cell .markdown}

------------------------------------------------------------------------
:::

::: {.cell .markdown}
# Creating Visualizations for Data Analysis
:::

::: {.cell .markdown}
### TASK 1.1: Develop a *Line chart* using the functionality of pandas to show how Average automobile sales fluctuate from year to year
:::

::: {.cell .markdown}
<details><summary>Click here for a hint</summary>
&#10;<p>
You will require:-
<br>to group the year and calculate the average on the 'Automobile Sales', as the data has years and months column
<br>make use of .plot() with kind = 'line'
<br>donot forget to include labels and title
</details>
:::

::: {.cell .code}
``` python

```
:::

::: {.cell .markdown}
<details><summary>Click here for a solution template</summary>
&#10;```python
    #create data for plotting
    df_line = df.groupby(df['Year'])['Automobile_Sales'].mean()
    #create figure
    plt.figure(figsize=(10, 6))
    df_line.plot(kind = 'line')
    plt.xlabel('........')
    plt.ylabel('.........')
    plt.title('......................')
    plt.show()
```
</details>
:::

::: {.cell .markdown}
### Include the following on the plot

ticks on x- axis with all the years, to identify the years of recession
`<br>`{=html}annotation for at least two years of recession
`<br>`{=html}Title as Automobile Sales during Recession
`<br>`{=html}
:::

::: {.cell .markdown}
<details><summary>Click here for a hint</summary>
    <p>
    You can create the list for the range 1980 till 2023 and pass that list to the plt.xticks function or you can directly pass the range to the function.
    You might need to rotate the ticks to an angle so that they fit in well on the axis
    You can include annotation with plt.text(x, y, 'text to display') 
    </p>
</details>
:::

::: {.cell .code}
``` python

```
:::

::: {.cell .markdown}
<details>
    <summary>Click here for Solution template</summary>
&#10;```python
    plt.figure(figsize=(10, 6))
    df_line = ...............
    df_line.plot(kind = 'line')
    plt.xticks(list(range(1980,2024)), rotation = 75)
    plt.xlabel('..............')
    plt.ylabel('............')
    plt.title('...................')
    plt.text(1982, 650, '1981-82 Recession')
    plt.text(......, ..., '..............')
    plt.legend()
    plt.show()
```
&#10;</details>
:::

::: {.cell .markdown}

------------------------------------------------------------------------
:::

::: {.cell .markdown}
#### TASK 1.2: How do trends in advertising expenditure correlate with automobile sales during non-recession periods, and what insights can be derived from this relationship.
:::

::: {.cell .markdown}
<details><summary>Click here for a hint</summary>
&#10;<p>
    You will require:-
<br>Start by filtering the dataset to include only non-recession periods where the "Recession" column has a value of 0.
<br>Group the data by Year and calculate the average of "Automobile_Sales" and "Advertising_Expenditure".
<br>Ensure you reset the index after aggregation so the DataFrame remains structured properly.
<br>Use sns.lineplot() to plot trends:
<br>One line for average automobile sales (solid green line with circular markers).
<br>Another line for average advertising expenditure (dashed blue line with square markers).
<br>Add labels and a title to make the visualization clear.
<br>Include a legend and a grid for better readability.
</p>
</details>
:::

::: {.cell .code}
``` python
```
:::

::: {.cell .markdown}
<details>
    <summary>Click here for Solution template</summary>
&#10;```python
 &#10;# Assuming 'df' is your dataset
df_non_rec = df[df['Recession'] == 0]
&#10;# Calculate average automobile sales and average advertising expenditure by year (non-recession)
df_trends = df_non_rec.groupby('...', as_index=False).agg(
    Avg_Sales=('...', 'mean'),
    Avg_Ad_Spend=('...', 'mean')
)
&#10;# Create line plots for average sales and advertising expenditure over the years
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_trends, x='...', y='...', marker='o', linestyle='-', color='green', label='...')
sns.lineplot(data=df_trends, x='...', y='...', marker='s', linestyle='--', color='blue', label='...')
&#10;# Add labels, legend, title, and grid
plt.xlabel('...')
plt.ylabel('...')
plt.title('...')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
&#10;# Show the plot
plt.tight_layout()
plt.show()
&#10;
&#10;```
</details>
:::

::: {.cell .markdown}
#### From the above plot, what insights have you gained?`<br>`{=html} Type in your answer below:
:::

::: {.cell .code}
``` python
```
:::

::: {.cell .markdown}
<details>
    <summary>Inference</summary>
<p>
Inference:
The graph shows that during non-recession periods, automobile sales are more volatile than advertising expenditure. While there are moments of alignment, sales often spike independently, suggesting other factors like market demand or economic conditions also play a significant role. The correlation between advertising and sales appears inconsistent over time.<br><br>
    </p>
    </details>
:::

::: {.cell .markdown}

------------------------------------------------------------------------
:::

::: {.cell .markdown}
### TASK 1.3: Use the functionality of **Seaborn Library** to create a visualization to compare the sales trend per vehicle type for a recession period with a non-recession period.
:::

::: {.cell .markdown}
<details><summary>Click here for a hint</summary>
&#10;<p>
     To visualize the average number of vehicles sold during recession and non-recession periods, you can use a bar chart
        <br> You will need to group recession average Automobile_Sales and then plot it<br>
    Make use of sns.barplot(x=x,y=y, data = df)</p>
</details>
:::

::: {.cell .code}
``` python
```
:::

::: {.cell .markdown}
<details>
    <summary>Click here for Solution template</summary>
&#10;```python
    new_df = df.groupby('Recession')['Automobile_Sales'].mean().reset_index()
&#10;    # Create the bar chart using seaborn
    plt.figure(figsize=(.........., ............)
    sns.barplot(x='Recession', y='Automobile_Sales', hue='Recession',  data=new_df)
    plt.xlabel('............')
    plt.ylabel('...............')
    plt.title('Average Automobile Sales during Recession and Non-Recession')
    plt.xticks(ticks=[0, 1], labels=['Non-Recession', 'Recession'])
    plt.show()
```
&#10;</details>
:::

::: {.cell .markdown}
### Now you want to compare the sales of different vehicle types during a recession and a non-recession period

`<br>`{=html}We recommend that you use the functionality of **Seaborn Library** to create this visualization
:::

::: {.cell .markdown}
<details><summary>Click here for a hint</summary>
&#10;<p>
     To visualize sales of different vehicles during recession and non-recession periods, you can use a bar chart
        <br> You will need to group Recession, Vehicle_Type for average Automobile_Sales and then plot it<br>
    Make use of sns.barplot(x=x,y=y, data = df)</p>
</details>
:::

::: {.cell .code}
``` python
```
:::

::: {.cell .markdown}
<details>
<summary>Click here for Solution template</summary>
&#10;```python
&#10;grouped_df = df.groupby('Recession')['Automobile_Sales'].mean().reset_index()
# Create the grouped bar chart using seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='......', y='........', hue='Vehicle_Type', data=grouped_df)
plt.xticks(ticks=[0, 1], labels=['Non-Recession', 'Recession'])
plt.xlabel('.............')
plt.ylabel('..............')
plt.title('Vehicle-Wise Sales during Recession and Non-Recession Period')
&#10;plt.show()
&#10;```
</details>
:::

::: {.cell .markdown}
### From the above chart what insights have you gained on the overall sales of automobiles during recession? `<br>`{=html} Type your answer below:-
:::

::: {.cell .markdown}
:::

::: {.cell .markdown}
<details>
<summary>Inference</summary>
&#10;From this plot, we can understand that there is a drastic decline in the overall sales of the automobiles during recession.<br>However, the most affected type of vehicle is executivecar and sports<br><br>
</details>
:::

::: {.cell .markdown}

------------------------------------------------------------------------
:::

::: {.cell .markdown}
### TASK 1.4: Use sub plotting to compare the variations in GDP during recession and non-recession period by developing line plots for each period.

`<br>`{=html}Now, you want to find more insights from the data to understand the reason. `<br>`{=html}Plot a two line charts using subplotting to answer:-

#### How did the GDP vary over time during recession and non-recession periods?

`<br>`{=html}Make use of `<u>`{=html}add_subplot()`</u>`{=html} from Matplotlib for this comparision.
:::

::: {.cell .code}
``` python
```
:::

::: {.cell .markdown}
<details>
<summary>Click here for Solution template</summary>
&#10;```python
    #Create dataframes for recession and non-recession period
    rec_data = df[df['Recession'] == 1]
    non_rec_data = df[df['Recession'] == 0]
    &#10;    #Figure
    fig=plt.figure(figsize=(12, 6))
    &#10;    #Create different axes for subploting
    ax0 = fig.add_subplot(1, 2, 1) # add subplot 1 (1 row, 2 columns, first plot)
    ax1 = fig.add_subplot(... ,... ,... ) # add subplot 2 (1 row, 2 columns, second plot). 
    &#10;    #plt.subplot(1, 2, 1)
    sns.lineplot(x='Year', y='GDP', data=rec_data, label='Recession', ax=ax0)
    ax0.set_xlabel('Year')
    ax0.set_ylabel('GDP')
    ax0.set_title('GDP Variation during Recession Period')
    &#10;    #plt.subplot(1, 2, 2)
    sns.lineplot(x='......', y='......', data=........, label='.........',ax=...)
    ax1.set_xlabel('.....')
    ax1.set_ylabel('.......')
    ax1.set_title('..........')
    &#10;    plt.tight_layout()
    plt.show()
&#10;   #------------------------------------------------Alternatively--------------
   #Using subplot()
    plt.figure(figsize=(............, ..........))
    &#10;    #subplot 1
    plt.subplot(1, 2, 1)
    sns.lineplot(x='.........', y='......', data=.........., label='......')
    plt.xlabel('.......')
    plt.ylabel('..........')
    plt.legend()
    #subplot 1
    plt.subplot(1, 2, 2)
    sns.lineplot(x='.........', y='......', data=.........., label='......')
    plt.xlabel('.......')
    plt.ylabel('..........')
    plt.legend()
    &#10;    plt.tight_layout()
    plt.show()
```
</details>
:::

::: {.cell .markdown}
<details>
<summary>Inference</summary>
From this plot, it is evident that GDP tends to be lower and more volatile during recessions, with significant fluctuations and uncertainty. In contrast, non-recessionary periods show a relatively higher GDP level but still exhibit some degree of variability.<br><br></details>
:::

::: {.cell .markdown}

------------------------------------------------------------------------
:::

::: {.cell .markdown}
### TASK 1.5: Develop a Bubble plot for displaying the impact of seasonality on Automobile Sales.

`<br>`{=html}How has seasonality impacted the sales, in which months the sales were high or low? Check it for non-recession years to understand the trend

##### Develop a Bubble plot for displaying Automobile Sales for every month and use Seasonality Weight for representing the size of each bubble`<br>`{=html}

Title this plot as \'Seasonality impact on Automobile Sales\'
:::

::: {.cell .markdown}
<details><summary>Click here for a hint</summary>
&#10;<p>
     You can create Bubble Chart by calling the scatter()
        <br>Pass the 'Month' and 'Automobile_Sales' to the functions as x and y and then use Seasonality weight for size parameter</p>
</details>
:::

::: {.cell .code}
``` python
```
:::

::: {.cell .markdown}
<details>
<summary>Click here for Solution template</summary>
&#10;```python
    non_rec_data = df[df['Recession'] == 0]
    &#10;    size=non_rec_data['Seasonality_Weight'] #for bubble effect
    &#10;    sns.scatterplot(data=non_rec_data, x='........', y='........', size=size)
    &#10;    #you can further include hue='Seasonality_Weight', legend=False)
&#10;    plt.xlabel('Month')
    plt.ylabel('Automobile_Sales')
    plt.title('Seasonality impact on Automobile Sales')
&#10;    plt.show()
&#10;```
</details>
:::

::: {.cell .markdown}
<details>
<summary>Inference</summary>
From this plot, it is evident that seasonality has not affected on the overall sales. However, there is a drastic raise in sales in the month of April and December<br><br></details>
:::

::: {.cell .markdown}

------------------------------------------------------------------------
:::

::: {.cell .markdown}
\### TASK 1.6: Use the functionality of Matplotlib to develop a scatter plot to identify the relationship between consumer confidence and automobile sales during recessions.
\#### From the data, develop a scatter plot to identify the relationship between consumer confidence and automobile sales during recession periods.
`<br>`{=html} Title this plot as \'Consumer Confidence and Automobile Sales during Recessions\'
:::

::: {.cell .markdown}
<details><summary>Click here for a hint</summary>
&#10;<p>
     You can create dataframe where recession is '1'.
        <br>Pass the 'Consumer_Confidence' and 'Automobile_Sales' to the plt.scatter()</p>
</details>
:::

::: {.cell .code}
``` python
```
:::

::: {.cell .markdown}
<details>
<summary>Click here for Solution template</summary>
&#10;```python
    #Create dataframes for recession and non-recession period
    rec_data = df[df['Recession'] == 1]
    plt.scatter(rec_data['Consumer_Confidence'], rec_data['Automobile_Sales'])
    &#10;    plt.xlabel('.....')
    plt.ylabel('.......')
    plt.title('..........')
    plt.show()
&#10;```
</details>
:::

::: {.cell .markdown}
\### How does consumer confidence relate to automobile sales during recessions?
`<br>`{=html} Plot another scatter plot and title it as \'Relationship between Vehicle Price and Sales during Recessions\'
:::

::: {.cell .code}
``` python
```
:::

::: {.cell .markdown}
<details>
<summary>Click here for Solution template</summary>
&#10;```python
    #Create dataframes for recession and non-recession period
    rec_data = df[df['Recession'] == 1]
    plt.scatter(rec_data['Price'], rec_data['Automobile_Sales'])
    &#10;    plt.xlabel('.....')
    plt.ylabel('.......')
    plt.title('..........')
    plt.show()
&#10;```
</details>
:::

::: {.cell .markdown}
<details><summary>Inference</summary>
The graphs indicate that during recessions, higher consumer confidence tends to boost automobile sales, while higher vehicle prices generally correspond to lower sales. This highlights the strong influence of both consumer sentiment and affordability on purchasing decisions during economic downturns.<br><br></details>
:::

::: {.cell .markdown}

------------------------------------------------------------------------
:::

::: {.cell .markdown}
\### TASK 1.7: Create a pie chart to display the portion of advertising expenditure of XYZAutomotives during recession and non-recession periods.
`<br>`{=html}How did the advertising expenditure of XYZAutomotives change during recession and non-recession periods?
:::

::: {.cell .markdown}
<details><summary>Click here for a hint</summary>
&#10;<p>
     You can create two dataframe for recession and nonreccession period.
    <br> Calculate the sum of Advertising_Expenditure for both dataframes
    <br> Pass these total values to plt.pie(). May include labels as ['Recession', 'Non-Recession']
        <br>Feel Free to customie the pie further
    <br>title this plot as  - Advertising Expenditure during Recession and Non-Recession Periods</p>
</details>
:::

::: {.cell .code}
``` python
```
:::

::: {.cell .markdown}
<details>
<summary>Click here for Solution template</summary>
&#10;```python
    # Filter the data 
    Rdata = df[df['Recession'] == 1]
    NRdata = df[df['Recession'] == 0]
&#10;    # Calculate the total advertising expenditure for both periods
    RAtotal = Rdata['...........'].sum()
    NRAtotal = NRdata['...........'].sum()
&#10;    # Create a pie chart for the advertising expenditure 
    plt.figure(figsize=(8, 6))
&#10;    labels = ['Recession', 'Non-Recession']
    sizes = [RAtotal, NRAtotal]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
&#10;    plt.title('...........................')
&#10;    plt.show()
&#10;
```
</details>
:::

::: {.cell .markdown}
#### From the above plot, what insights do you find on the advertisement expenditure during recession and non recession periods?`<br>`{=html} Type your answer below:-
:::

::: {.cell .markdown}
:::

::: {.cell .markdown}
<details><summary>Inference</summary>
It seems XYZAutomotives has been spending much more on the advertisements during non-recession periods as compared to during recession times. Fair enough!<br><br></details>
:::

::: {.cell .markdown}

------------------------------------------------------------------------
:::

::: {.cell .markdown}
### TASK 1.8: Develop a pie chart to display the total Advertisement expenditure for each vehicle type during recession period.`<br>`{=html}

Can we observe the share of each vehicle type in total expenditure during recessions?
:::

::: {.cell .markdown}
<details><summary>Click here for a hint</summary>
&#10;<p>
     You will be required to group vehicle type for sum of advertisement expenditure.
    <br> the plot a pie with the data, May include relevant labels
    <br>title this plot as  - Share of Each Vehicle Type in Total Expenditure during Recessions</p>
</details>
:::

::: {.cell .code}
``` python
```
:::

::: {.cell .markdown}
<details>
    <summary>Click here for Solution template</summary>
&#10;```python
    # Filter the data 
    Rdata = df[df['Recession'] == 1]
&#10;    # Calculate the sales volume by vehicle type during recessions
    VTexpenditure = Rdata.groupby('..........')['.............'].sum()
&#10;    # Create a pie chart for the share of each vehicle type in total expenditure during recessions
    plt.figure(figsize=(..., ...))
&#10;    labels = VTexpenditure.index
    sizes = VTexpenditure.values
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
&#10;    plt.title('....................')
&#10;    plt.show()
```
    </details>
:::

::: {.cell .markdown}
<details>
<summary>Inference</summary>
During recession the advertisements were mostly focued on low price range vehicle. A wise decision!<br><br></details>
:::

::: {.cell .markdown}

------------------------------------------------------------------------
:::

::: {.cell .markdown}
\### TASK 1.9: Develop a lineplot to analyse the effect of the unemployment rate on vehicle type and sales during the Recession Period.
`<br>`{=html}Analyze the effect of the unemployment rate on vehicle type and sales during the Recession Period
\#### You can create a lineplot and title the plot as \'Effect of Unemployment Rate on Vehicle Type and Sales\'
:::

::: {.cell .markdown}
<details><summary>Click here for a hint</summary>
&#10;<p>
    Filter out the data for recession period<br>
     Make use of lineplot() from seaborn and pass the relavent data</p>
</details>
:::

::: {.cell .code}
``` python
```
:::

::: {.cell .markdown}
<details>
    <summary>Click here for Solution template</summary>
&#10;```python
# Assuming 'df' is your dataset
df_rec = df[df['Recession'] == 1]
&#10;# Set figure size
plt.figure(figsize=(16, 6))
&#10;# Create line plot showing effect of unemployment rate on automobile sales, by vehicle type
sns.lineplot(
    data=df_rec,
    x='...',               # Replace with unemployment rate column (e.g., 'unemployment_rate')
    y='...',               # Replace with automobile sales column (e.g., 'Automobile_Sales')
    hue='...',             # Replace with vehicle type column (e.g., 'Vehicle_Type')
    marker='o'
)
&#10;# Customize labels, legend, and title
plt.title('...')
plt.xlabel('...')
plt.ylabel('...')
plt.legend(title='...')
&#10;# Show plot
plt.tight_layout()
plt.show()
&#10;```
&#10;</details>
:::

::: {.cell .markdown}
#### From the above plot, what insights have you gained on the sales of superminicar, smallfamilycar, mediumminicar?`<br>`{=html} Type your answer below:-
:::

::: {.cell .markdown}
:::

::: {.cell .markdown}
<details><summary>Inference</summary>
The plot shows that automobile sales decline as unemployment rates rise during a recession, with sharp drops beyond 3%. SuperMiniCars, SmallFamilyCars, and MediumFamilyCars exhibit high volatility, reflecting their sensitivity to economic uncertainty and changing consumer priorities.<br><br>
</details>
:::

::: {.cell .markdown}

------------------------------------------------------------------------
:::

::: {.cell .markdown}
### OPTIONAL : TASK 1.10 Create a map on the hightest sales region/offices of the company during recession period
:::

::: {.cell .code}
``` python
from pyodide.http import pyfetch

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/us-states.json'
await download(path, "us-states.json")

filename = "us-states.json"
```
:::

::: {.cell .markdown}
#### You found that the datset also contains the location/city for company offices. Now you want to show the recession impact on various offices/city sales by developing a choropleth
:::

::: {.cell .code}
``` python
```
:::

::: {.cell .markdown}
<details><summary>Click for Solution</summary>
    &#10;```python
&#10;    # Filter the data for the recession period and specific cities
    recession_data = data[data['Recession'] == 1]
&#10;    # Calculate the total sales by city
    sales_by_city = recession_data.groupby('City')['Automobile_Sales'].sum().reset_index()
&#10;    # Create a base map centered on the United States
    map1 = folium.Map(location=[37.0902, -95.7129], zoom_start=4)
&#10;    # Create a choropleth layer using Folium
    choropleth = folium.Choropleth(
        geo_data= 'us-states.json',  # GeoJSON file with state boundaries
        data=sales_by_city,
        columns=['City', 'Automobile_Sales'],
        key_on='feature.properties.name',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Automobile Sales during Recession'
    ).add_to(map1)
&#10;
    # Add tooltips to the choropleth layer
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['name'], labels=True)
    )
&#10;    # Display the map
    map1
&#10;```
</details>
:::

::: {.cell .markdown}
# Congratulations! You have completed the lab
:::

::: {.cell .markdown}
## Authors
:::

::: {.cell .markdown}
[Dr. Pooja](author_link)
:::

::: {.cell .markdown}
<!---|Date (YYYY-MM-DD)|Version|Changed By|Change Description|
|-|-|-|-|
2024-01-05|0.2.1|Sowmyaa Gurusamy|Updated the lab instructions|
|2023-06-17|0.2|Pooja|Initial Lab Creation|
|2023-05-01|0.1|Shengkai|Create Lab Template|-->
:::

::: {.cell .markdown}
Copyright © 2023 IBM Corporation. All rights reserved.
:::
