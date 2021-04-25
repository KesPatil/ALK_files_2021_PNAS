
# ALK_files_2021_PNAS

<p align="justify">
README: supporting data for 2021 manuscript PNAS Patil et. al. There are three folders F_unbiased that includes the files to perform Unbiased Molecular Dynamics, F_metad contains files to perform metadynamics, F_post_processing contains files to perform post processing <br />
</p>
## Folders
<p align="justify">
F_unbiased: This folder has the input scripts required to perform Unbiased Molecular Dynamics <br />
1. 
F_metad: This folder has the input scripts required to perform Metadynamics <br />
1. 

F_post_processing: This folder contain the python scripts used for post-processing trajectories data to calculate hydrogen bond occupancies, plot free energy landscapes, check convergence of metadynamics free energy zones and to extract structures from those  zones </br> 
1.
</p>
## Forcefield implemented

Our MD and metadynamics simulations use charmm27.ff from GROMACS 5.0.7

## Procedure
### 1. MD simulation in GROMACS <br />
<p align="justify">
The MD simulations are performed in GROMACS. The paper mentions Biophyscode which actually is a wrapper on Gromacs. Please feel free to try out Biophyscode, a creation from Radhakrishnan lab. https://biophyscode.github.io. Please note: Following is the walk-through on how to introduce mutations in protein and run a simulation using Biophyscode:
</p>
"https://biophyscode.github.io/molecular_dynamics_lab/"


All the requisite files needed to run the simulations are  included in the F_unbiased. Submit the job to run the MD using the command <br />

gmx grompp -f md.mdp -c npt.gro -t npt.cpt -p topol.top -o md_0_1.tpr


### 2. Enhanced sampling simulation of Metadynamics using PLUMED <br />

We patch GROMACS 5.0.7 with PLUMED 2.3.5 and use multiple walker (num_of_walkers=4) metadynamics. For installation procedure of PLUMED and the subsequent patching with GROMACS, see here: https://www.plumed.org/doc-v2.6/user-doc/html/_installation.html <br />
 
<p align="justified">
In the folder F_metad we have the scripts required to run the metadynamics. Please note: Metadynamics has to be run using the output .gro and .cpt files of the unbiased MD  simulations. The folder containts the .mdp file, plumed.dat, topol.top, and .itp files <br />
plumed.dat metadynamics script run in GROMACS 5.0.7 patched with PLUMED 2.3.5 using multiple walker (num_of_walkers=4) metadynamics. We set in the PLUMED script, the energy in kcal/mol and length in Å. The parameters used in this study to perform Well-Tempered multiple walker metadynamics (WTMD) are:bias factor γ = T +∆T/T = 20, height = 0.6 and pace = 500. <br />
https://sites.google.com/site/plumedweb/home <br />
</p>

Aggregate of 2.6us metadynamics run in GROMACS 5.0.7 patched with PLUMED 2.3.5 using multiple walker (num_of_walkers=4) metadynamics until the convergence criterion is met for the zones of interest (See section C1 in the SI of  Patil et. al. PNAS 2021<br />

The output of the metadynamics run are the HILLS files. We will have four of them since we used four walkers. To get the free energy file from the HILLS use <div class="text-white bg-blue mb-2">
  .sum_hills
</div> sum_hills action of PLUMED (https://www.plumed.org/doc-v2.5/user-doc/html/sum_hills.html) <br />

### 3. Description of the post-processing codes <br />
Analysis of the trajectories was done using python and mostly MDanalysis package in python: https://www.mdanalysis.org  <br />

 The folder F_post_processing contains three codes: <br />
 
 1. Free_energy_convergence.ipynb is the code to plot the free energy landscapes using fes.dat file and also to give the free energy estimate of the zone of interest using the equation 4 under section C1 in SI. <br />
 2. hbonds.py is the code that takes in trajectory files from the zones as input and outputs things required for the next code - plot_zone.py (to reproduce plots in Fig 3A and 3B in main text)  <br />
 3. plot_zone.py takes in the output from hbonds.py and reproduces the plots in Fig 3A and 3B in main text)  <br />

## Citations
If you have any suggestions or queries please feel free to reach out at : patilk@seas.upenn.edu  <br />
If you found the above scripts and/or codes helpful in your work, please cite: <br />
1. Jordan, E. Joseph, et al. "Computational algorithms for in silico profiling of activating mutations in cancer." Cellular and Molecular Life Sciences 76.14 (2019): 2663-2679.
2. Patil, Keshav, et al. "Computational studies of anaplastic lymphoma kinase mutations reveal common mechanisms of oncogenic activation." Proceedings of the National Academy of Sciences 118.10 (2021).
