# -*- coding: utf-8 -*-
"""
Created on Sun May 21 15:03:40 2023

@author: Campbell Timms
"""

import matplotlib.pyplot as plt
import numpy as np
import math
import scipy 
import re
import urllib.request
from urllib.error import URLError

try:
    # Read the contents of the .txt file
    with open('H-atom_Orbitals_Simulation.txt', 'r') as file:
        code = file.read()
    # Execute the code
    exec(code) 
except:
    # Same code as .txt file and if the .txt file is used incorrectly or isn't found these default values are used to run the simultation
    
    # Hydrogen Orbit
    # Sets units
    N = 50 
    hbar = 1.054571817*1e-34 #hbar: 1.054 571 817x10-34 J s
    mE = 9.10953794449800*1e-31 #mE-mass electron: 9.109537944498001e-31 kg
    e0 = 8.85419 * 1e-12 #C^2/J*m permativity of free space
    eC = 1.60218*1e-19 #C elementary charge - Coulmbs 
    a = (4*np.pi*e0* hbar**2)/(mE*(eC**2)) #Bohr radius 
    k = 8.99*1e9 #N*m^2/C^2 - Coulombs Constant
    L = a*90
    
    # Set Quantum Numbers
    n = 5 
    l = 4 
    m = 2


#Create real space arrays for polar Coords from cartesian coords

X    = np.arange(0,N+1,1)
X1D  = (L/N)*X - (L/2) #Convert axis to real space
X2D  = np.tile(X1D,(N+1,1)) 
X3D  = np.tile(X2D,(N+1,1,1))

Y2D  = np.transpose(X2D)
Y3D = np.transpose(X3D,[0,2,1]) 

Z3D = np.transpose(X3D,[2,1,0]) 

#Spherical Polar Coordinates conversaon
R3D = np.sqrt(X3D**2 + Y3D**2 + Z3D**2) 
Theta3D = np.arccos(Z3D/R3D) 
Phi3D = np.arctan2(Y3D,X3D) 

# Fixes nan due to div by inf at the origin of the orbit
Theta3D[N//2,N//2,N//2] = 0
# Phi3D[N/2+1,N/2+1,N/2+1] = 0

#Createwavefunction and solve the real space arrays

def hydrogenWaveFuction(n,l,m,a):

    # Calculate the Legandre Polynomial using Rodrigue's Formula
    # These equations were taken from the notes from my quantum mechanics class and are found in the Griffiths Textbook eq.4.32. These equations can also be found here: https://en.wikipedia.org/wiki/Legendre_polynomials#Rodrigues
    
    PmlcosTheta = scipy.special.lpmv(m, l, (np.cos(Theta3D)))
    
    #Using the Legendre Polynomial calcualte the Spherical harmonic
    #https://en.wikipedia.org/wiki/Spherical_harmonics#Orthogonality_and_normalization
    SphericalH_Nconst= (2*(l+1)/(4*np.pi))*(math.factorial(l-abs(m))/math.factorial(l+abs(m)))
    
    SphericalHarmonic = np.sqrt(SphericalH_Nconst) * np.exp(1j*m*Phi3D) * PmlcosTheta
    
    #Calculate the Radial Equation 
    #found online here: https://en.wikipedia.org/wiki/Hydrogen-like_atom
    
    #With the Generalised Laguerre Polynomials using the scipy function: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.eval_genlaguerre.html#scipy.special.eval_genlaguerre
    #Mathmatically: https://en.wikipedia.org/wiki/Laguerre_polynomials#Explicit_examples_and_properties_of_the_generalized_Laguerre_polynomials
    #Girffiths eq.4.87
    
    #Indices for the Laguerre Polynomial as found in griffiths
    p = (2*l)+1
    q = (n-l-1)+p
    
    
    #Calculating the Normalisation Constant
    first_term = (2/(n*a))**3
    second_term = math.factorial(n-l-1)/(2*n)*(math.factorial(n+l))
    Radial_Nconst = first_term * second_term
    Radial_Nconstsqrt = np.sqrt(Radial_Nconst)
    
    #Calculating the Laguerre Polynomial in terms of R3D
    radial_scaled = (2*R3D)/(n*a)
    LnaR3D     = scipy.special.genlaguerre(p,q)(radial_scaled)
    #Alternate function
    # LnaR3Deval = scipy.special.eval_genlaguerre(p,q,(radialH))
    
    Psi_nlm = Radial_Nconstsqrt*((radial_scaled)**l)*np.exp(-(R3D)/(n*a))*LnaR3D*SphericalHarmonic

    return Psi_nlm


Hydrogen_wavefunction_3D = hydrogenWaveFuction(n,l,m,a) 


# Create Potential
V = -(k*(eC**2))/(3*(R3D**3)) 
# Fixes nan due to div by inf at the origin of the orbit
V[N//2,N//2,N//2] = 0 


def plot3D(Complex3DWavefunction):
    wavefunction = abs(Complex3DWavefunction)
    max3D = np.max(wavefunction)
    min3D = np.min(wavefunction)
    Range_3Dwavefunction = max3D - min3D
    min_max_ranges = [0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.6,1.0]
    colours = ['y','tab:orange','r','tab:pink','m','g','c','b','tab:grey','k']
    transparancy = [0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,1.0]
    
    #Create Figure to plot on
    ax = plt.figure(figsize=(12, 12)).add_subplot(projection='3d')
    
    #Plot on that figure
    for i in range(len(min_max_ranges)-1):
        valueMin = min_max_ranges[i]*(Range_3Dwavefunction)
        valueMax = min_max_ranges[i+1]*(Range_3Dwavefunction)
        wavefunction = abs(Hydrogen_wavefunction_3D)
        wavefunction[(wavefunction < valueMin) | (wavefunction > valueMax)] = 0
        boolwavefunction = wavefunction > 0
        
        ax.voxels(boolwavefunction, facecolors = colours[i], alpha = transparancy[i])
        
    ax.set(xlabel='Y', ylabel='X', zlabel='Z')
    ax.set_title('Hydrogen wavefunction $\u03A8_{'+str(n)+str(l)+str(m)+'}$')
    ax.set_aspect('equal')
    plt.savefig('Hydrogen wavefunction \u03A8_{'+str(n)+str(l)+str(m)+'}')
    plt.show()
    return

plot3D(Hydrogen_wavefunction_3D)

def webcrawl(n,l,m):
    first_page_url = 'https://commons.wikimedia.org/wiki/Hydrogen_orbitals_3D'
    
    prefix = 'https://commons.wikimedia.org/wiki/'
    imName = "File:Hydrogen_eigenstate_n"+str(n)+"_l"+str(l)+"_m"+str(m)+".png"
    
#Finding the right page for the Hydrogen Wavefunction
    try: 
        page = urllib.request.urlopen(first_page_url)
                
        for line in page:
            line = line.decode().strip()
            # print(line)
            if re.search(imName, line):
                second_page_url = prefix + imName
                
        page2 = urllib.request.urlopen(second_page_url)
        hpattern = '<div class="fullImageLink" id="file"><a href="([^"]*)"'
#Opening the relevant page   
        for line in page2:
            line = line.decode().strip()
            if re.search(hpattern, line):
                im_url = (re.findall(hpattern, line)[0])
    except URLError as e:
        print(e)
#Saving the image    
    try:
        im_page = urllib.request.urlopen(im_url).read()
        with open ("Hydrogen_eigenstate_n"+str(n)+"_l"+str(l)+"_m"+str(m)+".png",'wb') as outFile:
            outFile.write(im_page)
    except URLError as e:
        print(e)
        return
    
webcrawl(n, l, m)






