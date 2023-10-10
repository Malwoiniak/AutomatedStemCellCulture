
'''
Parse vi cell count file for currently processed plates

Author: Malwina Kotowicz
E-mail: malwina.kotowicz@dzne.de
'''
import pandas as pd
import regex as re
from config import (dir_experimental_4well, dir_experimental_6well, dir_experimental_bbbdiff, dir_4well_out_cellcount,
                    dir_6well_out_cellcount, dir_bbbdiff_out_cellcount, filerows_to_keep, dir_4well_export,
                    fourwell_cols, options_plt_format, dir_6well_export, sixwell_cols, dir_bbb_export, 
                    bbbdiff_cols)
import os
from datetime import datetime
import argparse
from utils.input_readers import parse_datetime, txt_filereader, valid_plate_format
from utils.cellcount_img_tools import match_replace, get_df_cellcount, add_multiple_cols
import warnings

def get_plt_spec_info(text1, text2, export_file, df_cols, dir_experimental, dir_out):
        """Get plate specific information to use downstream depending on user's input
        (saved as dict)"""
        plt_values =  {
        'text1':text1,
        'text2': text2,
        "export_file":  pd.read_excel(export_file),
        "df_cols": df_cols,
        "dir_experimental": dir_experimental,
        "dir_out": dir_out
        }

        return plt_values

if __name__ == '__main__':

    #silence the UserWarning related to openpyxl
    warnings.simplefilter("ignore", category=UserWarning)

    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-p', '--plate_format', help='Plate format for this run of cell count (4well, 6well OR BBBdiff)', 
                        type=lambda x: valid_plate_format(x, options_plt_format), required=True)
    ARGS = PARSER.parse_args()
    PLT_FORMAT = ARGS.plate_format

    #assuming 1st val in options_plt_format list being 4well...
    if PLT_FORMAT.lower() == options_plt_format[0]:
        plt_values = get_plt_spec_info('tube thaw datetime','harvest datetime',dir_4well_export, fourwell_cols,
                          dir_experimental_4well, dir_4well_out_cellcount)

    #2nd value being 6well...
    elif PLT_FORMAT.lower() == options_plt_format[1]:
        plt_values = get_plt_spec_info('seeding datetime','end datetime in unconditioned media',dir_6well_export, sixwell_cols,
                          dir_experimental_6well, dir_6well_out_cellcount)

    else: #otherwise bbbdiff plate
        plt_values = get_plt_spec_info('start datetime in conditioned media','harvest datetime',dir_bbb_export, bbbdiff_cols,
                          dir_experimental_bbbdiff, dir_bbbdiff_out_cellcount)
    #create an empty df to append data to in each iter
    df_final = pd.DataFrame(columns = plt_values['export_file'].columns)
    for barcode in plt_values['export_file'].Barcode: #get barcodes of parsed plates
        begin_date = parse_datetime(input(f'Barcode: {barcode}\nEnter {plt_values["text1"]} in YYYYMMDD-HHMMSS format...\n')) #convert to datetime
        end_date = parse_datetime(input(f'Barcode: {barcode}\nEnter {plt_values["text2"]} in YYYYMMDD-HHMMSS format...\n')) #convert to datetime
        day_count = int(input('Enter day of cell count (relative to the experiment)...\n'))

        arguments = [begin_date, end_date, day_count]
        # each 4well barcode has cell count file barcode.txt, read only lines needed
        lines = txt_filereader(plt_values["dir_experimental"], barcode, filerows_to_keep)
        # process the lines, hour in datetime of run has colons, replace with empty str
        lines_correct = match_replace(':(?:[012345]\d):(?:[012345]\d)',lines, ':', "" )
        #get df of lines_correct
        df_cellcount_trans = get_df_cellcount(lines_correct)
        df_cellcount_trans.rename(columns={'Sample ID':'Barcode'})#vi cell file sample id == barcode
        #merge with export from database
        df_cellcount_merged = df_cellcount_trans.merge(plt_values['export_file'],how='left', on='Barcode')
        df_cellcount_merged = add_multiple_cols(df_cellcount_merged, plt_values["df_cols"],arguments)#add cols with vals from users input
        df_final = df_final.append(df_cellcount_merged, ignore_index = True)
        #save import file with timestamp
        df_final.to_excel(os.path.join(plt_values["dir_out"],f'{datetime.now().strftime("%Y%m%d-%H%M%S")}_{PLT_FORMAT.lower()}_import.xlsx'), index=False)
        #save to import file, needed for automated imports by FileMaker
        df_final.to_excel(os.path.join(plt_values["dir_out"], 'IMPORT_NOW.xlsx'), index=False)