'''
Util functions for reading and parsing user input or input files

Author: Malwina Kotowicz
E-mail: malwina.kotowicz@dzne.de
'''

from datetime import datetime
import argparse
import os

def parse_datetime(dt_str):
    try:
        return datetime.strptime(dt_str, '%Y%m%d-%H%M%S')
    except ValueError:
        raise argparse.ArgumentTypeError('Invalid date and time format, use YYYYMMDD-HHMMSS')

def txt_filereader(directory, barcode, filerows_to_keep):
    """reads 'barcode.txt' file located in directory by keeping only rows passed (filerows_to_keep)"""

    with open(os.path.join(directory,'{}.txt').format(barcode), 'r') as f:
        lines = [line.strip() for pos, line in enumerate(
            f.readlines()) if pos in filerows_to_keep] #pos is indexing the lines in file
    return lines

def valid_plate_format(input_plt_format,options_plt_format):
    """Check if plt format input is in the list of possible values"""
    if input_plt_format.lower() not in options_plt_format:
        raise argparse.ArgumentTypeError(f'Invalid input: {input_plt_format}, possible values: {options_plt_format}')
    return input_plt_format

def validate_times_teer(input_int, max_times):
    """Checks if correct teer measurements vals entered"""
    if 1 <= input_int <= max_times:
        pass
    else:
        raise ValueError('Invalid value. Possible values: a number between 1 and 10.')
    return input_int

def process_datetime(input_str, input_str_format, output_date_format):
    """Gets the date in output_str_format from a string of timestamp in input_str_format"""
    time_and_date = datetime.strptime(input_str, input_str_format)
    date = datetime.strftime(time_and_date, output_date_format)
    return date