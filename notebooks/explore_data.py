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


def convert_zip_codes(zips):
    z_str = [str(i) for i in zips]
    z_flt = zips.tolist()
    zip_code = []
    for i, j in zip(z_str, z_flt):
        if len(str(i)) == 7:
            zip_code.append(str(j)[0:5])
        if len(str(i)) == 6:
            zip_code.append(str(j * 10)[0:5])
    return zip_code


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

    # Extract Year, Month and Date and place in separate columns
    df['year'] = DatetimeIndex(df.date).year
    df['month'] = DatetimeIndex(df.date).month_name()
    df['day'] = DatetimeIndex(df.date).day

    # States and Counties
    states = df.state.unique()
    counties = df.county.unique()

    # Print Data
    print(df[:5])
    print(df.describe())
    print(states)
    print(counties)

    df_ca = df[df.state == 'California'].reset_index()
    print(df_ca)

    return


if __name__ == "__main__":
    main()