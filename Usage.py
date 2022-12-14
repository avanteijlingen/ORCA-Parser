# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:59:58 2022

@author: avtei
"""
import matplotlib.pyplot as plt
from ORCAParse import *


print("Phenol")
Optimization = ORCAParse("Test-cases/Phenol/Opt.out")

print("ORCA exited normally:", Optimization.valid)
print("Job took:", Optimization.seconds(), "seconds")
print("Job input line:", Optimization.parse_input())

Optimization.parse_coords()
print("Atomss:", Optimization.atoms)
print("Final coordinates:")
print(Optimization.coords[-1])


Optimization.parse_energies()
print("Energy at each step:", Optimization.energies)
print("Energy at convergence:", Optimization.energies[-1], "Ha")

TDDFT = ORCAParse("Test-cases/Phenol/TDDFT.out")

TDDFT.parse_absorption()
print("Wavelengths:", TDDFT.wavelengths)
TDDFT.parse_CD()
print("CD Wavelengths:", TDDFT.CD)
X, Y = [],[]
for nm,r in zip(TDDFT.CD, TDDFT.R):
    X.append(nm)
    Y.append(0)
    X.append(nm)
    Y.append(r)
    X.append(nm)
    Y.append(0)
plt.plot(X, Y)
plt.xlabel("Wavelength (nm)")

print("\n")
print("Meisenheimer Complex")
Optimization = ORCAParse("Test-cases/MeisenheimerComplex.out")
Optimization.parse_dispersion()
print("Meisenheimer Complex D4 energy:", Optimization.dispersions[-1])
Optimization.parse_free_energy()
print("Meisenheimer Complex Gibbs free energy:", Optimization.Gibbs)
Optimization.parse_freqs()
print("Meisenheimer Complex Frequencies:", Optimization.frequencies)
print("Meisenheimer Complex entropies:", Optimization.entropies)
print("Meisenheimer Complex enthalpies:", Optimization.enthalpies)

