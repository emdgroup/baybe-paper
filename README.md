# BayBE: A Bayesian Back End for Experimental Planning in the Low-To-No-Data Regime

This repository contains figures, data and code to reproduce the results from the publication.

## Installation
The exact state of required dependencies is stored in `requirements.txt`.

To run a notebook:
- Create a Python 3.10 environment, e.g. via
  ```terminal
  mamba create --yes --name baybe-paper python=3.10
  mamba activate baybe-paper
  ```
- Install ipykernel and add the kernel to jupyter kernels:
  ```terminal
  pip install ipykernel==6.29.5
  python -m ipykernel install --user --name=baybe-paper --display-name "BayBE Paper"
  ```
- Select the kernel when running the jupyter notebook. All required dependencies are 
  synced at the start of each notebook.