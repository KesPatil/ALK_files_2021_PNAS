#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 09:31:50 2019

@author: keshavpatil
"""


import numpy as np
from time import time
import MDAnalysis as mda
from MDAnalysis.tests.datafiles import XTC, GRO
import MDAnalysis.analysis.rms
from MDAnalysis.analysis.rms import rmsd
from MDAnalysis.analysis import align
import MDAnalysis.analysis.hbonds
import matplotlib.pyplot as plt
import itertools as it

start_time = time()
var_gro = '/Users/keshavpatil/Desktop/ALK/protein_alk.gro' 
var_xtc1 = '/Users/keshavpatil/Desktop/ALK/zone1.xtc' 
var_xtc2 = '/Users/keshavpatil/Desktop/ALK/zone2.xtc' 
var_xtc3 = '/Users/keshavpatil/Desktop/ALK/zone3.xtc'
var_xtc4 = '/Users/keshavpatil/Desktop/ALK/zone4.xtc'
u1 = mda.Universe(var_gro, var_xtc1)
u2 = mda.Universe(var_gro, var_xtc2)
u3 = mda.Universe(var_gro, var_xtc3)
u4 = mda.Universe(var_gro, var_xtc4)


alpha_C = u1.select_atoms("resid 75:93")
act_loop = u1.select_atoms("resid 185:208")

c1 = 75
c2 = 93
c3 = 185
c4 = 208
###############################################################################
###############################################################################
######################-----ZONE1----###########################################
h11= MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(u1, 'resid 75:93','resid 75:93',
								   update_selection1=False,
								   update_selection2=False,
								   detect_hydrogens='distance',
								   distance = 3.2,
								   angle = 150,
								   distance_type="heavy")
h11.run()								   


						  								  
sum_freq = 0
occu_h11 = []
for i in range(c1,c2+1):
    for j in range(0,len(h11.count_by_type())):
        if h11.count_by_type()['donor_resid'][j] == i or h11.count_by_type()['acceptor_resid'][j] == i :
            sum_freq = sum_freq + h11.count_by_type()['frequency'][j]
    lst  = [sum_freq,i,alpha_C.residues[i-c1]]        
    occu_h11.append(lst)
    sum_freq = 0   




h12= MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(u1, 'resid 185:208','resid 185:208',
								   update_selection1=False,
								   update_selection2=False,
								   detect_hydrogens='distance',
								   distance = 3.2,
								   angle = 150,
								   distance_type="heavy")
h12.run()	
sum_freq = 0
occu_h12 = []
for i in range(c3,c4+1):
    for j in range(0,len(h12.count_by_type())):
        if h12.count_by_type()['donor_resid'][j] == i or h12.count_by_type()['acceptor_resid'][j] == i :
            sum_freq = sum_freq + h12.count_by_type()['frequency'][j]
    lst  = [sum_freq,i,act_loop.residues[i-c3]]        
    occu_h12.append(lst)
    sum_freq = 0 
    
h13= MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(u1, 'resid 75:93','resid 185:208',
								   update_selection1=False,
								   update_selection2=False,
								   detect_hydrogens='distance',
								   distance = 3.2,
								   angle = 150,
								   distance_type="heavy")
h13.run()	
sum_freq = 0
occu_h13 = []
for i in it.chain(range(c1,c2+1), range(c3,c4+1)):
    for j in range(0,len(h13.count_by_type())):
        if h13.count_by_type()['donor_resid'][j] == i or h13.count_by_type()['acceptor_resid'][j] == i :
            sum_freq = sum_freq + h13.count_by_type()['frequency'][j]
    if i < c3:        
        lst  = [sum_freq,i,alpha_C.residues[i-c1]]        
        occu_h13.append(lst)
    if i > c2+1:
        lst  = [sum_freq,i,act_loop.residues[i-c3]]        
        occu_h13.append(lst)
        
    sum_freq = 0  
    
###################-----ADDING THE OCCUPANCIES FOR ZONE1----------#############
occu_zn_1 = []  

for i in range(0,len(occu_h13)):
    if i < len(occu_h11):
        freq = occu_h11[i][0] + occu_h13[i][0]
        lst = [freq, alpha_C.residues[i]]
        occu_zn_1.append(lst)
    if i >= len(occu_h11):
        freq = occu_h12[i-len(occu_h11)][0] + occu_h13[i][0]
        lst = [freq, act_loop.residues[i-len(occu_h11)]]
        occu_zn_1.append(lst)
        
        
################################################################################
#############################-----ZONE2----#####################################								  
h21= MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(u2, 'resid 75:93','resid 75:93',
								   update_selection1=False,
								   update_selection2=False,
								   detect_hydrogens='distance',
								   distance = 3.2,
								   angle = 150,
								   distance_type="heavy")
h21.run()								   


						  								  
sum_freq = 0
occu_h21 = []
for i in range(c1,c2+1):
    for j in range(0,len(h21.count_by_type())):
        if h21.count_by_type()['donor_resid'][j] == i or h21.count_by_type()['acceptor_resid'][j] == i :
            sum_freq = sum_freq + h21.count_by_type()['frequency'][j]
    lst  = [sum_freq,i,alpha_C.residues[i-c1]]        
    occu_h21.append(lst)
    sum_freq = 0   




h22= MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(u2, 'resid 185:208','resid 185:208',
								   update_selection1=False,
								   update_selection2=False,
								   detect_hydrogens='distance',
								   distance = 3.2,
								   angle = 150,
								   distance_type="heavy")
h22.run()	
sum_freq = 0
occu_h22 = []
for i in range(c3,c4+1):
    for j in range(0,len(h22.count_by_type())):
        if h22.count_by_type()['donor_resid'][j] == i or h22.count_by_type()['acceptor_resid'][j] == i :
            sum_freq = sum_freq + h22.count_by_type()['frequency'][j]
    lst  = [sum_freq,i,act_loop.residues[i-c3]]        
    occu_h22.append(lst)
    sum_freq = 0 
    
h23= MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(u2, 'resid 75:93','resid 185:208',
								   update_selection1=False,
								   update_selection2=False,
								   detect_hydrogens='distance',
								   distance = 3.2,
								   angle = 150,
								   distance_type="heavy")
h23.run()	
sum_freq = 0
occu_h23 = []
for i in it.chain(range(c1,c2+1), range(c3,c4+1)):
    for j in range(0,len(h23.count_by_type())):
        if h23.count_by_type()['donor_resid'][j] == i or h23.count_by_type()['acceptor_resid'][j] == i :
            sum_freq = sum_freq + h23.count_by_type()['frequency'][j]
    if i < c3:        
        lst  = [sum_freq,i,alpha_C.residues[i-c1]]        
        occu_h23.append(lst)
    if i > c2+1:
        lst  = [sum_freq,i,act_loop.residues[i-c3]]        
        occu_h23.append(lst)
        
    sum_freq = 0  
    
###################-----ADDING THE OCCUPANCIES FOR ZONE2----------#############
occu_zn_2 = []  

for i in range(0,len(occu_h23)):
    if i < len(occu_h21):
        freq = occu_h21[i][0] + occu_h23[i][0]
        lst = [freq, alpha_C.residues[i]]
        occu_zn_2.append(lst)
    if i >= len(occu_h21):
        freq = occu_h22[i-len(occu_h21)][0] + occu_h23[i][0]
        lst = [freq, act_loop.residues[i-len(occu_h21)]]
        occu_zn_2.append(lst)
        
###############################################################################
###########################----ZONE3-----------################################
###############################################################################
h31= MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(u3, 'resid 75:93','resid 75:93',
								   update_selection1=False,
								   update_selection2=False,
								   detect_hydrogens='distance',
								   distance = 3.2,
								   angle = 150,
								   distance_type="heavy")
h31.run()								   


						  								  
sum_freq = 0
occu_h31 = []
for i in range(c1,c2+1):
    for j in range(0,len(h31.count_by_type())):
        if h31.count_by_type()['donor_resid'][j] == i or h31.count_by_type()['acceptor_resid'][j] == i :
            sum_freq = sum_freq + h31.count_by_type()['frequency'][j]
    lst  = [sum_freq,i,alpha_C.residues[i-c1]]        
    occu_h31.append(lst)
    sum_freq = 0   




h32= MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(u3, 'resid 185:208','resid 185:208',
								   update_selection1=False,
								   update_selection2=False,
								   detect_hydrogens='distance',
								   distance = 3.2,
								   angle = 150,
								   distance_type="heavy")
h32.run()	
sum_freq = 0
occu_h32 = []
for i in range(c3,c4+1):
    for j in range(0,len(h32.count_by_type())):
        if h32.count_by_type()['donor_resid'][j] == i or h32.count_by_type()['acceptor_resid'][j] == i :
            sum_freq = sum_freq + h32.count_by_type()['frequency'][j]
    lst  = [sum_freq,i,act_loop.residues[i-c3]]        
    occu_h32.append(lst)
    sum_freq = 0 
    
h33= MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(u3, 'resid 75:93','resid 185:208',
								   update_selection1=False,
								   update_selection2=False,
								   detect_hydrogens='distance',
								   distance = 3.2,
								   angle = 150,
								   distance_type="heavy")
h33.run()	
sum_freq = 0
occu_h33 = []
for i in it.chain(range(c1,c2+1), range(c3,c4+1)):
    for j in range(0,len(h33.count_by_type())):
        if h33.count_by_type()['donor_resid'][j] == i or h33.count_by_type()['acceptor_resid'][j] == i :
            sum_freq = sum_freq + h33.count_by_type()['frequency'][j]
    if i < c3:        
        lst  = [sum_freq,i,alpha_C.residues[i-c1]]        
        occu_h33.append(lst)
    if i > c2+1:
        lst  = [sum_freq,i,act_loop.residues[i-c3]]        
        occu_h33.append(lst)
        
    sum_freq = 0  
    
###################-----ADDING THE OCCUPANCIES FOR ZONE3----------#############
occu_zn_3 = []  

for i in range(0,len(occu_h33)):
    if i < len(occu_h31):
        freq = occu_h31[i][0] + occu_h33[i][0]
        lst = [freq, alpha_C.residues[i]]
        occu_zn_3.append(lst)
    if i >= len(occu_h31):
        freq = occu_h32[i-len(occu_h31)][0] + occu_h33[i][0]
        lst = [freq, act_loop.residues[i-len(occu_h31)]]
        occu_zn_3.append(lst)
        
###############################################################################
###########################----ZONE4-----------################################
###############################################################################
h41= MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(u4, 'resid 75:93','resid 75:93',
								   update_selection1=False,
								   update_selection2=False,
								   detect_hydrogens='distance',
								   distance = 3.2,
								   angle = 150,
								   distance_type="heavy")
h41.run()								   


						  								  
sum_freq = 0
occu_h41 = []
for i in range(c1,c2+1):
    for j in range(0,len(h41.count_by_type())):
        if h41.count_by_type()['donor_resid'][j] == i or h41.count_by_type()['acceptor_resid'][j] == i :
            sum_freq = sum_freq + h41.count_by_type()['frequency'][j]
    lst  = [sum_freq,i,alpha_C.residues[i-c1]]        
    occu_h41.append(lst)
    sum_freq = 0   




h42= MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(u4, 'resid 185:208','resid 185:208',
								   update_selection1=False,
								   update_selection2=False,
								   detect_hydrogens='distance',
								   distance = 3.2,
								   angle = 150,
								   distance_type="heavy")
h42.run()	
sum_freq = 0
occu_h42 = []
for i in range(c3,c4+1):
    for j in range(0,len(h42.count_by_type())):
        if h42.count_by_type()['donor_resid'][j] == i or h42.count_by_type()['acceptor_resid'][j] == i :
            sum_freq = sum_freq + h42.count_by_type()['frequency'][j]
    lst  = [sum_freq,i,act_loop.residues[i-c3]]        
    occu_h42.append(lst)
    sum_freq = 0 
    
h43= MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(u4, 'resid 75:93','resid 185:208',
								   update_selection1=False,
								   update_selection2=False,
								   detect_hydrogens='distance',
								   distance = 3.2,
								   angle = 150,
								   distance_type="heavy")
h43.run()	
sum_freq = 0
occu_h43 = []
for i in it.chain(range(c1,c2+1), range(c3,c4+1)):
    for j in range(0,len(h43.count_by_type())):
        if h43.count_by_type()['donor_resid'][j] == i or h43.count_by_type()['acceptor_resid'][j] == i :
            sum_freq = sum_freq + h43.count_by_type()['frequency'][j]
    if i < c3:        
        lst  = [sum_freq,i,alpha_C.residues[i-c1]]        
        occu_h43.append(lst)
    if i > c2+1:
        lst  = [sum_freq,i,act_loop.residues[i-c3]]        
        occu_h43.append(lst)
        
    sum_freq = 0  
    
###################-----ADDING THE OCCUPANCIES FOR ZONE4----------#############
occu_zn_4 = []  

for i in range(0,len(occu_h43)):
    if i < len(occu_h41):
        freq = occu_h41[i][0] + occu_h43[i][0]
        lst = [freq, alpha_C.residues[i]]
        occu_zn_4.append(lst)
    if i >= len(occu_h41):
        freq = occu_h42[i-len(occu_h41)][0] + occu_h43[i][0]
        lst = [freq, act_loop.residues[i-len(occu_h41)]]
        occu_zn_4.append(lst)
	
###############################################################################
###############################################################################
###############################################################################                                   
###############---SAVING THE RESULTS------#####################################
        
occu_zn_1 = np.array(occu_zn_1)
occu_zn_2 = np.array(occu_zn_2)
occu_zn_3 = np.array(occu_zn_3)
occu_zn_4 = np.array(occu_zn_4)

								   
np.savetxt('zone1_occupancy.out', occu_zn_1,fmt='%s')
np.savetxt('zone2_occupancy.out', occu_zn_2,fmt='%s')
np.savetxt('zone3_occupancy.out', occu_zn_3,fmt='%s')
np.savetxt('zone4_occupancy.out', occu_zn_4,fmt='%s')
#hbond_sum = a1 + a2 + a3
#n_bins = 20 
#
#np.savetxt('zone1.out', hbond_sum)
#plt.hist(hbond_sum, bins=n_bins)
#plt.show()
end_time = time()
time_taken = end_time - start_time