#############################################
# project:      US COVID-19 Study           #
# date:         4/17/2020                   #
# file:         run.py                      #
# description:  is the entry point for the  #
#               for the analysis and study  #
#############################################

def main():
    """
    -- main --
    
    This function is used to launch the analysis for the US COVID-19.  It will
    create visualizations of the data to gather insights.
    
        1.  Import data and transform it to what is needed for analysis
        2.  Create visualizations and save them in reports
    """
    
    import sys
    from src.data.import_data import process_data
    
    print('Beginning Analysis')
    
    # Assign Filename #
    #   If there is a command line argument it will override the given
    #   filename.
    filename = 'us-counties.csv'
    if sys.argv[1:]:
        filename = sys.argv[1:]
        
    print(f'Processing: {filename}')
    
    
    
    return


if __name__ == "__main__":
    main()