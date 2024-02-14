"""
Cosmological functions
Author: Arta Khosravi
Last update: Feb. 2024
"""

import numpy as np
import scipy as sp
from scipy.integrate import quad
import scipy.integrate as integrate
import math
from Source_FV.FV_constants import *

##---Distance based---##
def H2(z): # Hubble function, s^-2 , we can just use H_0 instead
    return (H0**2)*(((OMP)*((1 + z)**3))+ (OLP))
def Xlintegrat(z): #Comoving Distance to the object
    res=integrate.quad((lambda x : 1/(np.sqrt(H2(x)))),0,z)
    return res[0]
def Skflat(z): #S_k(chi) for Omega_curvature = 0
    return (c)*Xlintegrat(z)
def DLflat(z): #Luminosity distance for Omega_curvature = 0 Or Flat Universe #k=0 #INCLUDES "ALL" REDSHIFTS
    return Skflat(z)*(1+z)
def d_L(z): #luminosity distance #ESTIMATION FOR "LOWER" REDSHIFTS
    return H0*(1+z)/c

##---Magnitude based---##
def M_bol(l_bol): #bolometric magnitude (absolute)
    return M_bol_sun + (-2.5)*(np.log10(10**l_bol/L_sun))
def m_app(M_abs,z): #apparent magnitude
    return M_abs + (5*(np.log10(z*4295.021)))
def m_app_bol(l_bol,z): #apparent bolometric magnitude
    return M_bol(l_bol)+5*np.log10(DLflat(z))+25
def M_dist_mod(z): #Absolute magnitude using distance modulus
    return m_2010-25-5*np.log10(DLflat(z))
def m_app_BOSS(z): #apparent magnitude using distance modulus using BOSS Abs mag
    return M_abs_BOSS+25+5*np.log10(DLflat(z))
def M_BOSS_dist_mod(z): #Absolute magnitude using distance modulus using BOSS apparent mag
    return m_app_BOSS(2.2)-5*np.log10(DLflat(z))-25
def L_L(z): #Linking length
    return LL0*(1+(a*np.arctan(z/z_s)))