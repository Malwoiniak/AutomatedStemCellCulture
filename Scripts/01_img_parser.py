'''
Parse yokogawa confocal images and store as json

Author: Malwina Kotowicz
E-mail: malwina.kotowicz@dzne.de
'''
import pandas as pd
import os
import json
import getpass
from config import (dir_4well_medium_ex, dir_6well_medium_ex, dir_bbb_medium_ex, dir_4well_out_img,
                    dir_6well_out_img, dir_bbbdiff_out_img, dir_img, options_plt_format, dir_json)
from utils.input_readers import process_datetime
import argparse
from utils.input_readers import valid_plate_format
from utils.cellcount_img_tools import get_json_data, add_columns
from datetime import datetime

def get_files_dir(dir_input, dir_output, dir_img, old_barcode_name):
    """Prepares a dictionary of directory and file-related parameters from users input"""

    plt_dirs = {
    'export_file': pd.read_excel(dir_input),
    'dir_output': dir_output,
    'dir_img': dir_img,
    'old_barcode_name':old_barcode_name
    }
    return plt_dirs

if __name__=='__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-p', '--plt_format', help='Plate format for this run of imaging (4well, 6well OR BBBdiff)',
                      type=lambda x: valid_plate_format(x,options_plt_format), required=True)
    ARGS = PARSER.parse_args()
    PLT_FORMAT = ARGS.plt_format

    #assuming 1st value on options_plt_format list is 4well plate...
    if PLT_FORMAT.lower() == options_plt_format[0]:
        #dir_img same for all plt format in here
        plt_dirs = get_files_dir(dir_4well_medium_ex, dir_4well_out_img, dir_img, '_4Well::Barcode')

    #2nd value is 6well plate...
    if PLT_FORMAT.lower() == options_plt_format[1]:
        plt_dirs = get_files_dir(dir_6well_medium_ex, dir_6well_out_img, dir_img, '_6Well::Barcode')
    #3rd value is bbfdiff plate
    if PLT_FORMAT.lower() == options_plt_format[2]:
        plt_dirs = get_files_dir(dir_bbb_medium_ex, dir_bbbdiff_out_img,dir_img, 'BBB_Differentiation::Barcode')
    
    #read db export file depending on plt format
    export_file = plt_dirs['export_file']
    export_file.rename(columns={plt_dirs['old_barcode_name']:'Barcode'}, inplace=True)#rename for uniform indexing across plt formats
    #output dir for img path files, depends on plt format
    dir_out = os.path.join(plt_dirs['dir_output'], f'{datetime.now().strftime("%Y%m%d-%H%M%S")}_{PLT_FORMAT}_img.xlsx')

    #access barcode and datetime for each row in df
    for index,row in export_file.iterrows():
        barcode = row['Barcode']
        time_and_date_str = row['Change Datetime'] #date of imaging = date of medium change
        #extract date (needed for folder accessing)
        date = process_datetime(time_and_date_str,"%d/%m/%Y %H:%M:%S","%Y%m%d")
        #name of each folder with confocal images
        folder_name = f'{date}_{barcode}'
        #path of each folder with confocal images
        img_dir = os.path.join(dir_img,folder_name)
        #json filename in each folder
        json_output_path = os.path.join(dir_json, f'{folder_name}_img.json')
        #img_dict = data (dict) for json writing
        img_dict = get_json_data(img_dir, '.jpg')
        #write json from img_dict in json output path (dir depends on plt format)
        with open(json_output_path,'w') as json_output:
            json.dump(img_dict,json_output, indent=2)
        
        # for each barcode and imaging date...
        condition = (export_file['Change Datetime'] == time_and_date_str) & (export_file['Barcode'] == barcode) #otherwise json path gets same values (last json path)
        export_file = add_columns(export_file,condition,'JSON_path',json_output_path) #get json file path
        export_file = add_columns(export_file,condition,'JSON_filename',os.path.basename(json_output_path)) #json filename
        #same for all rows, filename of import file that is being written currently, for control purposes
        export_file['Import_filename'] = os.path.basename(dir_out)
        export_file['Imported by'] = getpass.getuser() #some for all rows, name of user, for control purposes

        #save to import file, needed for automated imports by FileMaker
        export_file.to_excel(os.path.join(plt_dirs['dir_output'], 'IMPORT_NOW.xlsx'), index=False)
        #save import file with timestamp
        export_file.to_excel(dir_out, index=False)