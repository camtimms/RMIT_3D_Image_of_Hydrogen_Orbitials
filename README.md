# Hydrogen‑Atom Orbitals Simulation

A Python-based 3D voxel simulation of hydrogen‑like atomic orbitals.  
This project computes and visualizes the absolute value of the hydrogenic wavefunction Ψₙₗₘ in real space, and optionally downloads the corresponding eigenstate image from Wikimedia Commons.

---

## 🎥 Video Demonstration

Watch a step‑by‑step walkthrough here:  
https://www.youtube.com/watch?v=o1g1Cxv6mwk

---

## 🛠️ Prerequisites

- Python 3.8+  
- Required packages (install via pip):
  ```bash
  pip install numpy scipy matplotlib

## 📂 Repository Structure

<pre>
  ├── H-atom_Orbitals_Simulation.txt   # Input file with simulation parameters
  ├── simulation.py                    # Main Python script
  ├── README.md                        # Project documentation (this)
  └── outputs/
      ├── *.png                        # Generated wavefunction and potential plots
      └── File:Hydrogen_eigenstate_n...png  # Downloaded Wikimedia eigenstate images
 </pre>

## ⚙️ Configuration

All simulation parameters live in `H-atom_Orbitals_Simulation.txt`. If that file is missing or malformed, default values in `simulation.py` will be used.

### Parameter Summary

| Parameter                | Symbol | Units           | Description                                                                 |
|--------------------------|--------|------------------|-----------------------------------------------------------------------------|
| Resolution               | N      | —                | Number of voxels per axis (total grid size = (N+1)³).                      |
| Planck’s reduced constant| ℏ (hbar) | J·s             | ℏ = 1.054571817×10⁻³⁴                                                       |
| Electron mass            | mₑ     | kg               | mₑ = 9.10953794449800×10⁻³¹                                                |
| Permittivity of free space| ε₀ (e0)| C²/(J·m)         | ε₀ = 8.85419×10⁻¹²                                                          |
| Elementary charge        | e      | C                | e = 1.60218×10⁻¹⁹                                                           |
| Bohr radius              | a      | m                | a = (4π ε₀ ℏ²)/(mₑ e²)                                                      |
| Coulomb constant         | k      | N·m²/C²          | k = 8.99×10⁹                                                                |
| Simulation box half‑size | L      | m                | Real-space axis spans [–L/2, +L/2].                                         |
| Principal quantum number | n      | —                | n = 1, 2, 3, …                                                              |
| Azimuthal quantum number | l      | — (0 ≤ l < n)    | Orbital angular momentum                                                    |
| Magnetic quantum number  | m      | — (–l ≤ m ≤ +l)  | Magnetic projection                                                         |

## 🚀 Installation & Quick Start

1. Clone this repository:
```bash
git clone https://github.com/<your‑username>/H-atom_Orbitals_Simulation.git
```
cd H-atom_Orbitals_Simulation

2. Edit H-atom_Orbitals_Simulation.txt to set your desired parameters (or skip to use defaults).

3. Run the simulation:
```bash
python simulation.py
```

- The script will:

  1. Read your parameters (or fall back to defaults).

  2. Build a 3D grid in Cartesian coordinates.

  3. Compute R, θ, φ for each voxel.

  4. Evaluate Ψₙₗₘ (using associated Legendre and generalized Laguerre polynomials).

  5. Plot 3D isosurfaces of |Ψ| and save as outputs/Hydrogen_wavefunction_Ψₙₗₘ.png.

  6. Compute and save the Coulomb potential V = –k e²/(3 R³).

  7. Optionally web‑crawl Wikimedia for File:Hydrogen_eigenstate_n<n>_l<l>_m<m>.png.

  ## 📈 Example Usage

  ```text
  # In H-atom_Orbitals_Simulation.txt:
  N = 20
  n = 2
  l = 1
  m = 0
  # (Other parameters omitted to use defaults)
  
  $ python simulation.py
  # → outputs/Hydrogen_wavefunction_Ψ210.png
  # → outputs/Hydrogen_eigenstate_n2_l1_m0.png  (downloaded)
  ```

On a 20³ grid, the plot completes in ≈15 s on a modern desktop. Increase N for higher resolution at the cost of computation time (scales ~N³).
