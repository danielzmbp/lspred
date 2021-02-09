# LS-pred

In this repository you find the training dataset and python 
notebook constructed to predict plant pathogenic lifestyle from genome/transcriptome annotations.
- `lspred_prep_data.ipynb`: notebook to prepare data for training.
- `ls-pred_training.ipynb`: notebook for data training.
- `ls-pred_testing.ipynb`: notebook for testing new data.

## Input data
- Annotate your genome with [InterProScan](https://github.com/ebi-pf-team/interproscan).
- Get genome annotations in table format with [genome-properties](https://github.com/ebi-pf-team/genome-properties).
- Run the notebook `ls-pred_testing.ipynb` with this file.

## Requirements
- pandas
- tensorflow >= 2.0
- h5py == 2.10

## Preprint
Please find the preprint [here](https://www.biorxiv.org/content/10.1101/2021.01.12.426341v1).
