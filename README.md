# Flux-and-Volume-limit
The required code for flux and volume limiting datasets using the Friends of Friends (FOF) Algorithm. This specific sample was mainly used for flux and volume limiting QUOTAS and QuasarNET's dataset.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing. Refer to the **Code Description** section for guidance on deploying the project on a live system.

## Code Description
Here is a description of the different programs and files used in this repository:


* ```Creating Flux and Volume limited Sample of Quasars.ipynb:``` runs the code for firstly grouping the quasars, dropping those inefficient based on flux limitation using the Friends of Friends (FOF) algorithm, and eventually dividing them in subsamples using volume limitation.

* ```constants.py:``` Relevant cosmological and physical constants.

* ```functions.py:``` Functions used in the ```Creating Flux and Volume limited Sample of Quasars.ipynb``` program based on distance, luminosity, and magnitude.


## Requisites
This code makes use of several Python libraries:

* ```NumPy```
* ```Matplotlib```
* ```SciPy```
* ```Pandas```

## Authors

* **Arta Khosravi** - [artakh10](https://github.com/artakh10)


## Citation
If you use the code, please link this repository, and cite the related arXiv article.

## Contact
For comments, questions and etc. you can reach me at artakh10@gmail.com.
