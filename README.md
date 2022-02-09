# LS-pred
In this repository you find the training dataset and python 
notebook constructed to predict plant pathogenic lifestyle from genome/transcriptome annotations.
- `lspred_prep_data.ipynb`: notebook to prepare data for training.
- `lspred_training.ipynb`: notebook for data training.
- `lspred_testing.ipynb`: notebook for testing new data.

The h5 model can be downloaded from: 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4541621.svg)](https://doi.org/10.5281/zenodo.4541621)

Please place this h5 file in the same directory as the notebooks or scripts before running.

## Input data
- Annotate your genome with [InterProScan](https://github.com/ebi-pf-team/interproscan).
- Get genome annotations in table format with [genome-properties](https://github.com/ebi-pf-team/genome-properties).
- Run the notebook `ls-pred_testing.ipynb` with this file.

## Requirements
- pandas
- tensorflow >= 2.0
- h5py == 2.10

### Conda environment
Optionally, you can create a conda environment with the packages needed to reproduce the results using the `conda-env.txt` file:

`conda create --name <myenv> --file conda-env.txt`

where `<myenv>` is the name of your desired environment.

## Wrapper script
It is possible to run the entire prediction pipeline using the wrapper script `lspred.py`. 
For correct use you need to specify as input file the appropriate `.tsv` file or files resulting 
from the genome-properties annotation. 

`python lspred.py test_files/TABLE_Nothophytophthora_sp.tsv `

Optionally, it is possible to specify an output format from the following:
`tsv`, `csv`, `html` with the flag `-f`; as well as an output file name to which the results are written with the flag `-o`.
As an example:

`python lspred.py -f html -o first_batch.html test_files/TABLE_*.tsv`

## Carbohydrate active enzyme (CAZY) model
The model for predicting lifestyle from CAZY enzyme annotations is found in the folder `lspred_cazy`. In order to predict lifestyle, you need to use an output `.tsv` file from [run_dbcan](https://github.com/linnabrown/run_dbcan) on your data. 

## Publication
If you find this useful please consider citing our publication found [here](https://www.mdpi.com/2076-0817/10/7/807).

Gómez-Pérez, D.; Kemen, E. Predicting Lifestyle from Positive Selection Data and Genome Properties in Oomycetes. *Pathogens* **2021**, 10, 807. https://doi.org/10.3390/pathogens10070807 

`````
@Article{pathogens10070807,
AUTHOR = {Gómez-Pérez, Daniel and Kemen, Eric},
TITLE = {Predicting Lifestyle from Positive Selection Data and Genome Properties in Oomycetes},
JOURNAL = {Pathogens},
VOLUME = {10},
YEAR = {2021},
NUMBER = {7},
ARTICLE-NUMBER = {807},
URL = {https://www.mdpi.com/2076-0817/10/7/807},
PubMedID = {34202069},
ISSN = {2076-0817},
ABSTRACT = {As evidenced in parasitism, host and niche shifts are a source of genomic and phenotypic diversification. Exemplary is a reduction in the core metabolism as parasites adapt to a particular host, while the accessory genome often maintains a high degree of diversification. However, selective pressures acting on the genome of organisms that have undergone recent lifestyle or host changes have not been fully investigated. Here, we developed a comparative genomics approach to study underlying adaptive trends in oomycetes, a eukaryotic phylum with a wide and diverse range of economically important plant and animal parasitic lifestyles. Our analysis reveals converging evolution on biological processes for oomycetes that have similar lifestyles. Moreover, we find that certain functions, in particular carbohydrate metabolism, transport, and signaling, are important for host and environmental adaptation in oomycetes. Given the high correlation between lifestyle and genome properties in our oomycete dataset, together with the known convergent evolution of fungal and oomycete genomes, we developed a model that predicts plant pathogenic lifestyles with high accuracy based on functional annotations. These insights into how selective pressures correlate with lifestyle may be crucial to better understand host/lifestyle shifts and their impact on the genome.},
DOI = {10.3390/pathogens10070807}
}
