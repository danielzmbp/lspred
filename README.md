# LS-pred

In this repository you find the training dataset and python 
notebook constructed to predict plant pathogenic lifestyle from genome/transcriptome annotations.
- `lspred_prep_data.ipynb`: notebook to prepare data for training.
- `lspred_training.ipynb`: notebook for data training.
- `lspred_testing.ipynb`: notebook for testing new data.

## Input data
- Annotate your genome with [InterProScan](https://github.com/ebi-pf-team/interproscan).
- Get genome annotations in table format with [genome-properties](https://github.com/ebi-pf-team/genome-properties).
- Run the notebook `ls-pred_testing.ipynb` with this file.

## Requirements
- pandas
- tensorflow >= 2.0
- h5py == 2.10

### Conda environment
Optionally, you create a conda environment with the packages needed to reproduce the results using the `conda-env.txt` file:

`conda create --name <myenv> --file spec-file.txt`

where `<myenv>` is the name of your desired environment.

## Wrapper script
Instead of running the notebook it is possible to run the entire prediction pipeline using the wrapper script `lspred.py`. 
For correct use you need to specify as arguments the appropriate `.tsv` file of the genome-properties annotation. It is possible to analyze several files using wildcards. 
As an example:

`python lspred.py test_files/TABLE_*.tsv`

## Preprint
Please find the preprint [here](https://www.biorxiv.org/content/10.1101/2021.01.12.426341v1).
