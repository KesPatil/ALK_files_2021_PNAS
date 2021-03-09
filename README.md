# ALK_files_2021_PNAS


README: supporting data for 2021 manuscript PNAS Patil et. al.

## Folders
F_md: 101ns production run in Biophyscode that wraps GROMACS 4.6 for H-bond occupancy calculations <br />
F_unb: 100ns production run in GROMACS 5.0.7 to prepare files for Metadynamics <br />
F_metad: aggregate 2.6us metadynamics run in GROMACS 5.0.7 patched with PLUMED 2.3.5 using multiple walker (num_of_walkers=4) metadynamics<br />


## Forcefield implemented
charmm27.ff from GROMACS 5.0.7

## Code
Simulations were constructed and simulated according to the method described in the manuscript. <br />
Analysis of the trajectories was done using python and mostly MDanalysis package in python: https://www.mdanalysis.org


