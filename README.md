# Flux-and-Volume-limit
The required code for flux and volume limiting datasets using the Friends of Friends (FOF) Algorithm. This specific sample was mainly used for flux and volume limiting QUOTAS and QuasarNET datasets.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing. Please take a look at the **Code Description** section for guidance on deploying the project on a live system.

## Code Description
Here is a description of the different programs and files used in this repository:
### Main Project File
* ```Creating Flux and Volume limited Sample of Quasars.ipynb:``` runs the code for firstly grouping the quasars, dropping those inefficient based on flux limitation using the Friends of Friends (FOF) algorithm, and eventually dividing them into subsamples using volume limitation.
  You can import your dataset to your liking, and change the parameters accordingly such as
  <pre>data=pd.read_csv('***.csv'),</pre>
  and replace "***.csv" with the data you wish to use.\
  Parameters defined in this code such as
  <pre>z=data['z'].values #redshift
  mbh=data['log_bh'].values #Black Hole mass
  lbol=data['log_lbol'].values #Bolometric luminosity
  edd=data['log_edd_ratio'].values #Eddington ratio
  name=data['name'] #Name of the object</pre>
  can be replaced with your desired parameters as well.
### Constants
* ```constants.py:``` Relevant cosmological and physical constants.\ You can replace the mentioned constants to match your desired model and data.\
  Constants such as the CDM and DE density or the scale factor in t_0 (a), Linking Length (LL0), and redshift (z_s),
  <pre>a=1; #Scale factor in t=t0
  LL0=0.25; #Linking length_0
  z_s=0.05; #Redshift for star</pre>
    which are all constants used for flux limitation, can be modified according to your cosmological model or the data you're working with.
### Functions
* ```functions.py:``` Functions used in the ```Creating Flux and Volume limited Sample of Quasars.ipynb``` program based on distance, luminosity, and magnitude.\
  You can modify the functions to match your model and adjust the functions such as the Hubble function,
  <pre>def H2(z) # Squared Hubble function, s^-2 , we can just use H_0 instead</pre>
  or luminosity distance,
  <pre>def Xlintegrat(z): #Comoving Distance to the object
  def Skflat(z): #S_k(chi) for Omega_curvature = 0
  def DLflat(z): #Luminosity distance for all redshifts, for Omega_curvature = 0 Or Flat Universe
  def d_L(z): #luminosity distance, estimation for lower redshifts</pre>
    to match your preferred cosmological model.


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
