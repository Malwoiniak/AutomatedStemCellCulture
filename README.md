# Automated Stem Cell Culture
> A Python data processing pipeline for automated human induced pluripotent stem cells (hiPSCs) expansion and differentiation.
> 
This repository holds the python modules of the data processing pipeline for the automated cell culture platform. The hiPSCs are cultivated for expansion and differentiation into brain microvascular endothelial cells (BMECs) for an in vitro blood-brain barrier (BBB) as described in [Efficiency unleashed: Streamlined and automated data processing in high-throughput monoclonal antibody production](link_to_preprint) and [Human iPSC-derived brain endothelial microvessels in a multi-well format enable permeability screens of anti-inflammatory drugs](https://www.sciencedirect.com/science/article/pii/S014296122200165X?via%3Dihub)

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

ASCC requires Python (3.7+), pandas and numpy. You can install the necessary dependencies by following a few simple steps:

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
