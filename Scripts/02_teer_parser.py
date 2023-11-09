'''
Parse teer measurements for currently processed plates

Author: Malwina Kotowicz
E-mail: malwina.kotowicz@dzne.de
'''
import pandas as pd
from config import (plate_grids, dir_transwell_export, all_transwell_files, 
                    dir_transwell_out, teer_datetime_cols)
from utils.input_readers import parse_datetime, validate_times_teer
import glob
import os
from datetime import datetime
import warnings

def add_wells(df, barcode, plate_grids):
    """Assigns well values to the 'Well' column in df based on the 'Barcode' column.
    Plate_grids (dict): A dictionary mapping plate formats to well values.
    barcode is a value of 'Barcode' col.
    """
    #calculate the number of wells in plt with requested barcode
    plate_format = (df['Barcode'] == barcode).sum()
    wells=plate_grids[plate_format] #well values are accessed by key (plate_format)
    condition = df['Barcode'] == barcode #where requested barcode...
    df.loc[condition, 'Well'] = wells #add well values to df
    return df

def add_teer_measures(df, teer_measures, teer_datetime_cols):
    """Adds user input values to datetime columns (teer_datetime_cols) of teer measurement.
    teer_datetime_cols is a list of col names to of teer measurement datetime"""
    i=0
    for measure in range(teer_measures): # for each time teer was measured...
        #ask for input in correct format
        teer_datetime = parse_datetime(input(f'Enter datetime of {measure+1}. TEER measurement (YYYYMMDD-HHMMSS format)...\n'))
        df[teer_datetime_cols[i]] = teer_datetime #add to datetime column (per teer measurement)
        i += 1
    return df

if __name__ == '__main__':
    #silence the UserWarning related to openpyxl
    warnings.simplefilter("ignore", category=UserWarning)
    
    export_file = pd.read_excel(dir_transwell_export)
    #sort experimental files by modification time
    experimental_transwell = sorted(glob.glob(all_transwell_files), key=os.path.getmtime) 
    experimental_file = pd.read_excel(experimental_transwell[-1]) #indexing the las element, glob outputs list of filenames
    
    #adding well depending on plt format
    for barcode in export_file.Barcode.unique():
        export_file = add_wells(export_file, barcode, plate_grids)

    #add seed time
    seed_time = parse_datetime(input('Enter the datetime of seeding on TransWell plates (YYYYMMDD-HHMMSS format)...\n'))
    export_file['Seed Datetime'] = seed_time

    #add teer measures datetime
    teer_measures = validate_times_teer(int(input('How many times TEER was measured (in total)? Enter just a number (max 10)...\n')), 10)
    export_file = add_teer_measures(export_file,teer_measures, teer_datetime_cols)

    #merging with experimental data on barcode + well
    export_file = export_file.merge(experimental_file, how='left',on=['Barcode', 'Well'])
    try:
        export_file.drop(columns=['Unnamed: 0'], inplace=True) #drop old index col
    except:
        pass
    #save import file with timestamp
    export_file.to_excel(os.path.join(dir_transwell_out, f'{datetime.now().strftime("%Y%m%d-%H%M%S")}_transwell_import.xlsx'), index=False)
    #save to import file, needed for automated imports by FileMaker
    export_file.to_excel(os.path.join(dir_transwell_out, 'IMPORT_NOW.xlsx'), index=False)
print(f'Operation sucesfull. Files saved in {dir_transwell_out}')