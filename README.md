# ALK_files_2021_PNAS


README: supporting data for 2021 manuscript PNAS Patil et. al.

## Folders

F_unbiased: This folder has the input scripts required to perform Unbiased Molecular Dynamics <br />
F_metad: This folder has the input scripts required to perform Metadynamics <br />
F_post_processing: This folder contain the python scripts used for post-processing trajectories data to calculate hydrogen bond occupancies, plot free energy landscapes, check convergence of metadynamics free energy zones and to extract structures from those  zones </br> 

## Forcefield implemented
Our MD and metadynamics simulations use charmm27.ff from GROMACS 5.0.7

## Procedure
1. MD simulation in Biophyscode <br />

md: 101ns production run in Biophyscode that wraps GROMACS 4.6 for H-bond occupancy calculations <br />




2. Enhanced sampling simulation of Metadynamics using PLUMED <br />

plumed.dat metadynamics script run in GROMACS 5.0.7 patched with PLUMED 2.3.5 using multiple walker (num_of_walkers=4) metadynamics<br />
https://sites.google.com/site/plumedweb/home <br />


metad: Aggregate 2.6us metadynamics run in GROMACS 5.0.7 patched with PLUMED 2.3.5 using multiple walker (num_of_walkers=4) metadynamics until the convergence criterion is met for the zones of interest<br />

3. Description of the post-processing codes <br />

Analysis of the trajectories was done using python and mostly MDanalysis package in python: https://www.mdanalysis.org  <br />



## Citations
If you have any suggestions or queries please feel free to reach out at : patilk@seas.upenn.edu  <br />
If you found the above scripts and/or codes helpful, please cite: <br />
1. Jordan, E. Joseph, et al. "Computational algorithms for in silico profiling of activating mutations in cancer." Cellular and Molecular Life Sciences 76.14 (2019): 2663-2679.
2. Patil, Keshav, et al. "Computational studies of anaplastic lymphoma kinase mutations reveal common mechanisms of oncogenic activation." Proceedings of the National Academy of Sciences 118.10 (2021).
