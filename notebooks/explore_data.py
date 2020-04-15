#############################################
# project:      US COVID-19 Study           #
# date:         4/13/2020                   #
# file:         explore_data.py             #
# description:  explore raw data provided   #
#               by kaggle.com of the deaths #
#               and infected in the United  #
#               States.                     #
#############################################

import os
import datetime
from pandas import read_csv, DatetimeIndex
from numpy import nan, inf
from plotly.graph_objects import Figure, Scatter
from plotly.io import renderers


def main():
    # Data File Name and file path
    filename = 'us-counties.csv'
    filepath = os.path.join('./data/raw', filename)

    # Import data into DataFrame and rename columns
    df = read_csv(filepath, dtype={'fips': str})
    df.columns = [
        'date',
        'county',
        'state',
        'zip',
        'cases',
        'deaths'
    ]
    
    print(df.dtypes)
    print(f'Number of total cases:  {df.cases.sum()}')
    print(f'Number of total deaths:  {df.deaths.sum()}')

    # Extract Year, Month and Date and place in separate columns
    df['year'] = DatetimeIndex(df.date, yearfirst=True).year
    df['month'] = DatetimeIndex(df.date, yearfirst=True).month_name()

    # States and Counties
    states = df.state.unique()
    counties = df.county.unique()
    
    # Sum of Grouped Dats
    grp_dates = df.groupby(['date', 'state'])['cases', 'deaths'].sum()
    print(grp_dates.sum())
    
    # Plot Scatter plot of Cases vs Deaths
    renderers.default='browser'
    
    fig = Figure(
        data=Scatter(
            x=df.cases,
            y=df.deaths,
            mode='markers'
        )
    )
    
    fig.show()

    return


if __name__ == "__main__":
    main()