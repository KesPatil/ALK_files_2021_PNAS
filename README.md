# ALK_files_2021_PNAS


README: supporting data for 2021 manuscript PNAS Patil et. al. There are three folders F_unbiased that includes the files to perform Unbiased Molecular Dynamics, F_metad contains files to perform metadynamics, F_post_processing contains files to perform post processing <br />

## Folders

F_unbiased: This folder has the input scripts required to perform Unbiased Molecular Dynamics <br />
1. 
F_metad: This folder has the input scripts required to perform Metadynamics <br />
1. 

F_post_processing: This folder contain the python scripts used for post-processing trajectories data to calculate hydrogen bond occupancies, plot free energy landscapes, check convergence of metadynamics free energy zones and to extract structures from those  zones </br> 
1.

## Forcefield implemented
Our MD and metadynamics simulations use charmm27.ff from GROMACS 5.0.7

## Procedure
### 1. MD simulation in GROMACS <br />

The MD simulations are performed in GROMACS. The paper mentions Biophyscode which actually is a wrapper on Gromacs. Please feel free to try out Biophyscode, a creation from Radhakrishnan lab. https://biophyscode.github.io. Please note: Following is the walk-through on how to introduce mutations in protein and run a simulation using Biophyscode:


"XXXXXX Krishna please write here how to use Biophyscode to introduce mutations in protein structure and how to run a simulation in Biophyscode XXXXX"

All the requisite files are included in the F_unbiased. Submit the job to run the MD using the command <br />

gmx grompp -f md.mdp -c npt.gro -t npt.cpt -p topol.top -o md_0_1.tpr


### 2. Enhanced sampling simulation of Metadynamics using PLUMED <br />

We patch GROMACS 5.0.7 with PLUMED 2.3.5 and use multiple walker (num_of_walkers=4) metadynamics. Following is the procedure to do that.





plumed.dat metadynamics script run in GROMACS 5.0.7 patched with PLUMED 2.3.5 using multiple walker (num_of_walkers=4) metadynamics. We set in the PLUMED script, the energy in kcal/mol and length in Å. The parameters used in this study to perform Well-Tempered multiple walker metadynamics (WTMD) are:bias factor γ = T +∆T/T = 20, height = 0.6 and pace = 500. <br />
https://sites.google.com/site/plumedweb/home <br />


Aggregate of 2.6us metadynamics run in GROMACS 5.0.7 patched with PLUMED 2.3.5 using multiple walker (num_of_walkers=4) metadynamics until the convergence criterion is met for the zones of interest (See section C1 in the SI of  Patil et. al. PNAS 2021<br />

The output of the metadynamics run are the HILLS files. We will have four of them since we used four walkers. To get the free energy file from the HILLS use > sum_hills action of PLUMED (https://www.plumed.org/doc-v2.5/user-doc/html/sum_hills.html) <br />

### 3. Description of the post-processing codes <br />
Analysis of the trajectories was done using python and mostly MDanalysis package in python: https://www.mdanalysis.org  <br />

 xxx in the F_post_processing is the code to plot the free energy landscapes using HILLS files formed after the succesful run of Metadynamics



## Citations
If you have any suggestions or queries please feel free to reach out at : patilk@seas.upenn.edu  <br />
If you found the above scripts and/or codes helpful in your work, please cite: <br />
1. Jordan, E. Joseph, et al. "Computational algorithms for in silico profiling of activating mutations in cancer." Cellular and Molecular Life Sciences 76.14 (2019): 2663-2679.
2. Patil, Keshav, et al. "Computational studies of anaplastic lymphoma kinase mutations reveal common mechanisms of oncogenic activation." Proceedings of the National Academy of Sciences 118.10 (2021).
