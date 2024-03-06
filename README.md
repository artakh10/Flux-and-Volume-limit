# Flux-and-Volume-limit
The required code for flux and volume limiting datasets using the Friends of Friends (FOF) Algorithm. This specific sample was mainly used for flux and volume limiting QUOTAS and QuasarNET datasets.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing. Please take a look at the **Code Description** section for guidance on deploying the project on a live system.

## Code Description
Here is a description of the different programs and files used in this repository:


* ```Creating Flux and Volume limited Sample of Quasars.ipynb:``` runs the code for firstly grouping the quasars, dropping those inefficient based on flux limitation using the Friends of Friends (FOF) algorithm, and eventually dividing them into subsamples using volume limitation. You can import your dataset to your liking, change the parameters accordingly, and replace "***.csv" with the data you wish to import.

* ```constants.py:``` Relevant cosmological and physical constants. You can replace the mentioned constants to match your desired model and data.
Constants such as the CDM and DE density or the scale factor in t_0 (a), Linking Length (LL0), and redshift (z_s), which are all constants used for flux limitation, can be modified according to your cosmological model or the data you're working with.

* ```functions.py:``` Functions used in the ```Creating Flux and Volume limited Sample of Quasars.ipynb``` program based on distance, luminosity, and magnitude. You can modify the functions to match your model and adjust the functions such as the Hubble function or luminosity distance to match your preferred cosmological model.


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
