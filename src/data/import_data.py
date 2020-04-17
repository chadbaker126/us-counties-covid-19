#############################################
# project:      US COVID-19 Study           #
# date:         4/16/2020                   #
# file:         import_data.py              #
# description:  reads and imports data as a #
#               pandas dataframe and saves  #
#               new csv's for easier        #
#               processing.                 #
#############################################

def process_data(filename):
    
    # Import functions and libraries #
    import os
    import datetime
    from pandas import read_csv, DatetimeIndex
    
    # Raw Data File Path (String) #
    raw_filepath = os.path.join('./data/raw', filename)
    
    # Import Data (DataFrame) #
    df_raw = read_csv(raw_filepath, dtype={'fips': str})
    df_raw.columns = [
        'date',
        'county',
        'state',
        'zips',
        'cases',
        'deaths'
    ]
    
    
    
    return