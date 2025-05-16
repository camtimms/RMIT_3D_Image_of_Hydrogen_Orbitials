
How to run this software.
Video Explaination: https://www.youtube.com/watch?v=o1g1Cxv6mwk

1. Open H-atom_Orbitals_Simulation

2. Edit each of the parameters as you please.

	Summary of parameters:

		Resolution: 			N = Length of each 3D axis which creates the number of voxels (pixels)^3.
		Planck's constant: 		hbar (J s)
		Electron mass:			mE (kg)
		Permativity of free space: 	e0 (C^2/J*m) 
		Elementary charge: 		eC (C) - Coulmbs 
		Bohr radius: 			a = (4*np.pi*e0* hbar**2)/(mE*(eC**2)) 
		Coulombs Constant: 		k = (N*m^2/C^2)
		Length: 			L = Length of axis in real space

		Set Quantum Numbers
		Their ranges are as follows:
		n = 1,2,3...
		l = 0,1,2,...(n-1) 
		m = -l,(-l+1),...,+l

3. Run the code which will read this file with your set parameters and generate a simulation of that Hydrogen Wavefunction and find the corresponding image.
	-note: due to the complexity of the functions generating the simulation doesn take minutes. So please be paitent. A recomended value for N for a rough plot is N = 20 which takes roughly 15 s. 
 
The image were obtained from this website: https://commons.wikimedia.org/wiki/Hydrogen_orbitals_3D

If you would like to learn more about the what we're simulating head here: https://en.wikipedia.org/wiki/Hydrogen-like_atom



Code requirements for the assignment:
All values are lines which the required infomration.

Data types: 28,44,121,130
Control Flow: 130,158,161
Files: 2 x output images (.png), 1 x input file (.txt)
Functions: 65,116,148
Visualisation: 32,70,141
Web Data Crawling: 158,168
