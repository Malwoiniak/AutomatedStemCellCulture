
'''
Default config variables which maybe overridden by a user.

Author: Malwina Kotowicz
E-mail: malwina.kotowicz@dzne.de
'''
import os
# =================================
# PATHS 
# =================================
dir_parent = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) # get abs path, os independent 
#NOT SURE IF NEEDED
dir_grandparent = os.path.abspath(os.path.join(dir_parent, os.pardir)) #get grandparnt abs path
# dir_tubeinfo = os.path.join(dir_parent,'Tube_Info')
dir_4well_out = os.path.join(dir_parent,'4well_Out')
dir_4well_out_cellcount = os.path.join(dir_4well_out, 'cell_count')
dir_4well_out_img = os.path.join(dir_4well_out, 'img_paths')
dir_6well_out = os.path.join(dir_parent,'6well_Out')
dir_6well_out_cellcount = os.path.join(dir_6well_out, 'cell_count')
dir_6well_out_img = os.path.join(dir_6well_out, 'img_paths')
dir_bbbdiff_out = os.path.join(dir_parent,'bbbdiff_Out')
dir_bbbdiff_out_cellcount = os.path.join(dir_bbbdiff_out, 'cell_count')
dir_bbbdiff_out_img = os.path.join(dir_bbbdiff_out, 'img_paths')
dir_transwell_out = os.path.join(dir_parent,'transwell_Out')
dir_input = os.path.join(dir_parent,'Input')
dir_experimental = os.path.join(dir_input, 'experimental_data')
dir_img = os.path.join(dir_input, 'img')
dir_plt_exports = os.path.join(dir_input,'plt_exports')
dir_medium_exports = os.path.join(dir_input, 'medium_exports')
dir_json = os.path.join(dir_parent,'JSON')
#experimental data (vi count) files per plate format
dir_experimental_4well = os.path.join(dir_experimental, '4well')
dir_experimental_6well = os.path.join(dir_experimental, '6well')
dir_experimental_bbbdiff = os.path.join(dir_experimental, 'bbbdiff')
dir_experimental_transwell = os.path.join(dir_experimental, 'transwell')
all_transwell_files = os.path.join(dir_experimental_transwell, '*.xlsx')
#database export files - plate addition
dir_4well_export = os.path.join(dir_plt_exports,'4Well_export.xlsx') 
dir_6well_export = os.path.join(dir_plt_exports, '6well_export.xlsx')
dir_bbb_export = os.path.join(dir_plt_exports, 'bbbdiff_export.xlsx')
dir_transwell_export = os.path.join(dir_plt_exports, 'transwell_export.xlsx')
# database export files - medium change
dir_4well_medium_ex = os.path.join(dir_medium_exports,'4well_medium.xlsx')
dir_6well_medium_ex = os.path.join(dir_medium_exports,'6well_medium.xlsx')
dir_bbb_medium_ex = os.path.join(dir_medium_exports,'bbbdiff_medium.xlsx')
# =================================
# CELL COUNT FILES
# =================================
filerows_to_keep = [2,6,13,16,18,28]
fourwell_cols = ['Thaw Datetime','Harvest Datetime','Counted on Day']
sixwell_cols = ['Seed Datetime','End Datetime in unconditioned media','Counted on Day']
bbbdiff_cols = ['Start Datetime in conditioned media','Harvest Datetime','Counted on Day']
options_plt_format = ['4well', '6well', 'bbbdiff']
# =================================
# PLT FORMATS
# =================================
plate_grids = {
    6: [
        'A1', 'A2', 'A3',
        'B1', 'B2', 'B3'
    ],
    12: [
        'A1', 'A2', 'A3', 'A4',
        'B1', 'B2', 'B3', 'B4',
        'C1', 'C2', 'C3', 'C4'
    ],
    24: [
        'A1', 'A2', 'A3', 'A4', 'A5', 'A6',
        'B1', 'B2', 'B3', 'B4', 'B5', 'B6',
        'C1', 'C2', 'C3', 'C4', 'C5', 'C6',
        'D1', 'D2', 'D3', 'D4', 'D5', 'D6'
    ],
    48: [
        'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8',
        'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
        'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8',
        'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8',
        'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8',
        'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8'
    ],
    96: [
        'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12',
        'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12',
        'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12',
        'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12',
        'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12',
        'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',
        'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12',
        'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12'
    ]
}
# =================================
# TEER/ TRANSWELL PLATE
# =================================
teer_datetime_cols = ['TEER1 Datetime', 'TEER2 Datetime', 'TEER3 Datetime', 'TEER4 Datetime', 'TEER5 Datetime', 'TEER6 Datetime', 'TEER7 Datetime', 'TEER8 Datetime', 'TEER9 Datetime', 'TEER10 Datetime']