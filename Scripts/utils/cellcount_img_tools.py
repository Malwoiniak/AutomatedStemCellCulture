'''
universal functions to handle parsing of vi cell count (.txt) files

Author: Malwina Kotowicz
E-mail: malwina.kotowicz@dzne.de
'''

import pandas as pd
import regex as re
import os

def match_replace(regex, lines_to_match, str_to_replace, replacement):

    """ Searches each element of list of str, replaces part of matched substring (str_to_replace) 
    with sth else (replacement)"""

    time_pattern = re.compile(regex)

    lines_correct = []
    for line in lines_to_match:
        matches = time_pattern.findall(line) #search matches in lines
        if matches:
            for match in matches:#for each mached substring
                #for each line, replace the substring with other str
                new_line = line.replace(match, match.replace(str_to_replace, replacement))
                lines_correct.append(new_line)
        else:
            lines_correct.append(line)#if no matches, just append line
    return lines_correct

def get_df_cellcount(lines_correct):

    """Splits processed lines (lines_corect) by colon to get cols and vals for df"""
    data = [line.split(':') for line in lines_correct]#col names and vals separated by colon
    #get df of data
    df_cellcount = pd.DataFrame(data)
    #transpose so that each col has val
    df_cellcount_trans = df_cellcount.transpose()
    #first row of df = use as headers
    df_cellcount_trans.columns = df_cellcount_trans.iloc[0]
    #now drop rows that served as headers before
    df_cellcount_trans = df_cellcount_trans.drop(df_cellcount_trans.index[0])
    df_cellcount_trans = df_cellcount_trans.applymap(lambda x: x.strip()) #strip vals from leading /trailing space
    df_cellcount_trans.columns = df_cellcount_trans.columns.str.strip() #strip cols from leading /trailing space
    return df_cellcount_trans

def add_multiple_cols(df, list_of_cols, list_of_values):
    """adds col with val to df"""
    for col,val in zip(list_of_cols,list_of_values):
        df[col] = val
    return df

def get_json_data(img_dir, img_extension):
    """Gets a dict of imgs in passed dir. Filename = key, file path = value
    Used for json generation"""
    img_dict = {}
    for root, dirs, files in os.walk(img_dir):
        for file in files:
    
            if file.endswith(img_extension):
                img_key = os.path.splitext(file)[0]
                img_path = os.path.join(root,file)
                img_dict[img_key] = img_path
    img_dict = dict(sorted(img_dict.items()))
    return img_dict

def add_columns(df, condition, col_name, col_val):
    """Adds values to cols based on passed condition"""
    df.loc[condition,col_name ] = col_val
    return df