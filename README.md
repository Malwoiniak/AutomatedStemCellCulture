# Automated Stem Cell Culture
[![DOI](https://zenodo.org/badge/702971010.svg)](https://zenodo.org/doi/10.5281/zenodo.10106688)
> A Python data processing pipeline for automated human induced pluripotent stem cells (hiPSCs) expansion and differentiation.
> 
This repository holds the python modules of the data processing pipeline for the automated cell culture platform. The hiPSCs are cultivated for expansion and differentiation into brain microvascular endothelial cells (BMECs) for an in vitro blood-brain barrier (BBB) as described in [Gain efficiency with streamlined and automated data processing: Examples from high-throughput monoclonal antibody production](https://www.biorxiv.org/content/10.1101/2023.12.14.571214v1) and [Human iPSC-derived brain endothelial microvessels in a multi-well format enable permeability screens of anti-inflammatory drugs](https://www.sciencedirect.com/science/article/pii/S014296122200165X?via%3Dihub)

## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Reproducing the pipeline run](#reproducing-the-pipeline-run)
* [Contact](#contact)
* [References](#references)

## General info

This project contains data processing scripts for an automated stem cell culture (ASCC) (refer to [1] for more details). 

This a small, **a proof-of-concept** pipeline, tailored to an automated human induced pluripotent stem cell cultivation and differentiation performed in our lab, and associated database. We encourage the reader to get familiar with our paper before reproducing any pipeline steps. 

## Setup

### Installation instructions

ASCC requires Python (3.8.12), pandas and numpy. You can install the necessary dependencies by following a few simple steps:

1.	Download the full pipeline [here]( https://github.com/Malwoiniak/AutomatedStemCellCulture/archive/refs/heads/main.zip)
2.	Alternatively, you can clone the repository by running:

`git clone https://github.com/CRFS-BN/AutomatedStemCellCulture`

3.	Extract the contents of the zip files, if necessary.
4.	In terminal, navigate to the root directory of the extracted repository
5.	Create and activate a virtual environment, for example by using the Python build-in venv module:

**Linux/MacOS**
```
# Create a virtual environment named 'my_venv'
python3 -m venv my_venv

# Activate the virtual environment
source my_venv/bin/activate
```
**Windows**
```
# Create a virtual environment named 'my_venv'
python -m venv my_venv

# Activate the virtual environment
my_venv\Scripts\activate
```

6.	Install the project dependencies:

`(my_venv)$ pip install -r requirements.txt`

## Reproducing the pipeline run

After downloading the pipeline, you will note that there are already some output files produced on each pipeline step. They serve as example of apipeline run. Your files will be added to output directories after the run.

This repository contains all directories and files needed for pipeline run. Below you can find a detailed explanation on the functionality of each script. 

### 00_cellcount_parser.py

This script parses the cell count and viability file generated by ViCell (automated cell viability counter). Depending on plate grid format, scripts can be run for 4well, 6well or bbbdiff plates (this is related to stages of expansion and differentiation in our workflow, refer to [1] for more info). To do this, replace ‘4well’ with ‘6well’ or ‘bbbdiff’downstream.

#### Input files

+ From `Input/plt_exports` directory: `4well_export.xlsx`. Database export files with plates’ IDs.

+ From `Input/experimental_data/` directory: `Barcode_name.txt` files exported by ViCell 

#### Usage

00_cellcount_parser.py takes one argument:

| Argument         | Description                               | Required | Default Value |
|------------------|-------------------------------------------|----------|---------------|
| `-p plate_format ` | 'Plate format for this run of cell count (4well, 6well or bbbdiff) | Yes      | None |

1.	In terminal, move to the `Scripts/` directory of the project
2.	Run the script passing the plate numbers:

`python 00_cellcount_parser.py –p 4well` 

#### Output files

+ In ` 4well_Out/cell_count/` directory, files: `yyymmdd-hhmmss_4well_import.xlsx` and `IMPORT_NOW.xlsx`

These are the database import files containing cell count and viability assay information. This file is needed for database import script that is run downstream.

### 01_img_parser.py

This script parses the images from confocal microscope and converts the paths to json file that will then be imported to database. 

#### Input files

+ From ` Input/img/yyyyddmm_ Barcode_name` directory: all images taken for that plate (in .jpg format). Add your own images to those directories, we only provide one .jpg file for example purposes

+ From `Input/medium_exports/` directory: `4Well _medium.xlsx` database export file with samples’ IDs.

#### Usage

01_img_parser.py takes one argument:

| Argument         | Description                               | Required | Default Value |
|------------------|-------------------------------------------|----------|---------------|
| `-p plate_format ` | 'Plate format for this run of cell count (4well, 6well or bbbdiff) | Yes      | None |

1.	In terminal, move to the `Scripts/` directory of the project
2.	Run the script passing the plate numbers:

`python 01_img_parser.py –p 4well` 

#### Output files

+ In ` 4well_Out/img_paths/` directory, files: `yyymmdd-hhmmss_4well_img.xlsx` and `IMPORT_NOW.xlsx`

These are the database import files containing image paths information for accessing the .json files. This file is needed for database import script that is run downstream.

### 02_teer_parser.py

This script parses the TEER measurements and connects the information to samples’ IDs.

#### Input files

+ From ` Input/img/yyyyddmm_ Barcode_name` directory: ` transwell_export.xlsx. Database export file with samples’ IDs.

+ From `Input/ experimental_data/transwell` directory: `yyymmdd_TEER_measurement.xlsx` files containing the teer values for all plates measured at the time, with all TEER values per plate barcode.

#### Usage

1.	In terminal, move to the `Scripts/` directory of the project
2.	Run the script:

`python 02_teer_parser.py` 

#### Output files

+ In `transwell_Out /` directory, files: `yyyymmdd-hhmmss_transwell_import.xlsx` and `IMPORT_NOW.xlsx`

These are the database import files containing TEER values for TransWell plates currently processed. This file is needed for database import script that is run downstream.

#### Other files needed by scripts

| Filename | Description                               |
|------------------|-------------------------------------------|
| `Scripts/config.py` | A configuration file to host all parameters (modifiable), used by all pipeline scripts. It includes directories, filenames, machine parameters or threshold settings, among others|
| `Scripts/utils/cellcount_img_tools.py` | An utility module that provides reusable and generic functionalities, here: functions to handle parsing of vi cell count (.txt) files|
| `Scripts/utils/input_readers.py` | An utility module that provides reusable and generic functionalities, here: functions for reading and parsing user input or input files|

## Contact

Malwina Kotowicz: m_kotowicz@hotmail.com, feel free to contact me!

## References

[1] Kotowicz, M. et al., 2023. Gain efficiency with streamlined and automated data processing: Examples from high-throughput monoclonal antibody production. BioRxiv. [DOI](https://doi.org/10.1101/2023.12.14.571214)

