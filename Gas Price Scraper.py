# Importing libraries required

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

# Opening page and grabing html
my_url = ('https://www.eia.gov/dnav/ng/hist/rngwhhdm.htm')
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# HTML parser
page_soup = soup(page_html, 'html.parser')

table = []

# Finding the table
ele_table = page_soup.find("table", summary="Henry Hub Natural Gas Spot Price (Dollars per Million Btu)")
# traverse table
col_tag = 'th'
ele_rows = ele_table.find_all('tr', recursive=False)
for ele_row in ele_rows:
    row = []
    ele_cols = ele_row.find_all(col_tag, recursive=False)
    for ele_col in ele_cols:
        # Using empty string for no data column
        content = ele_col.string.strip() if ele_col.string else ''
        row.append(content)
    col_tag = 'td'
    # Saving row with data
    if any(row):
        table.append(row)
 
#Opening CSV file
file = open('GasPrice.csv','w')
writer = csv.writer(file)


#Printing table
for row in table:
    writer.writerow(row)
    print('\t'.join(row))
    
#Closing CSV file
file.close()

# Visualizing data with Bokeh Library

import pandas as pd
import seaborn as sns
from bokeh.plotting import figure, output_file, show

def make_dashboard(Date, Prices, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='Dollars per Million Btu')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="Henry Hub Natural Gas Spot Price")
    show(p)