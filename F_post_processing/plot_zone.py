#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 21:13:48 2019

@author: keshavpatil
"""



import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


with open('zone1_occupancy.out') as f:
    
    lines = f.readlines()
    
new_lines = []    
# Get rid of empty lines
for line in lines:
    # Strip whitespace, should leave nothing if empty line was just "\n"
    if not line.strip():
        continue
    # We got something, save it
    else:
        new_lines.append(line)
        
y11 = []
y21 = []
y31 = []
y41 = []
y51 = []
y61 = []
ini = 22

#for i in range(0,len(lines)):
for i in range(ini,ini+21):
    
    words = lines[i].split()
    
    y11.append(round(float(words[0]),3)) #y1 takes in the occupancy
    y31.append(words[2]) #y3 takes in the residue names
    y41.append(words[3])

for i in range(0,len(y31)):
    y21.append(y31[i][0:3])

for i in range(0,len(y41)):
    y51.append(y41[i][0:2])
    
for i in range(0,len(y21)):
    y61.append(y21[i] + "-" + y51[i])

###############################################################################
##########----------------ZONE2-----------------###############################

with open('zone2_occupancy.out') as f:
    
    lines = f.readlines()
    
new_lines = []    
# Get rid of empty lines
for line in lines:
    # Strip whitespace, should leave nothing if empty line was just "\n"
    if not line.strip():
        continue
    # We got something, save it
    else:
        new_lines.append(line)
        
y12 = []
y22 = []
y32 = []
y42 = []
y52 = []
y62 = []
#for i in range(0,len(lines)):
for i in range(ini,ini+21):
    
    words = lines[i].split()
    
    y12.append(round(float(words[0]),3)) #y1 takes in the occupancy
    y32.append(words[2]) #y3 takes in the residue names
    y42.append(words[3])

for i in range(0,len(y32)):
    y22.append(y32[i][0:3])

for i in range(0,len(y42)):
    y52.append(y41[i][0:2])
    
for i in range(0,len(y22)):
    y62.append(y22[i] + "-" + y52[i])

    
   
###############################################################################
##########----------------ZONE3-----------------###############################

with open('zone3_occupancy.out') as f:
    
    lines = f.readlines()
    
new_lines = []    
# Get rid of empty lines
for line in lines:
    # Strip whitespace, should leave nothing if empty line was just "\n"
    if not line.strip():
        continue
    # We got something, save it
    else:
        new_lines.append(line)
        
y13 = []
y23 = []
y33 = []
y43 = []
y53 = []
y63 = []
#for i in range(0,len(lines)):
for i in range(ini,ini+21):
    
    words = lines[i].split()
    
    y13.append(round(float(words[0]),3)) #y1 takes in the occupancy
    y33.append(words[2]) #y3 takes in the residue names
    y43.append(words[3])

for i in range(0,len(y33)):
    y23.append(y32[i][0:3])

for i in range(0,len(y43)):
    y53.append(y41[i][0:2])
    
for i in range(0,len(y23)):
    y63.append(y22[i] + "-" + y53[i])

###############################################################################
##########----------------ZONE4-----------------###############################

with open('zone4_occupancy.out') as f:
    
    lines = f.readlines()
    
new_lines = []    
# Get rid of empty lines
for line in lines:
    # Strip whitespace, should leave nothing if empty line was just "\n"
    if not line.strip():
        continue
    # We got something, save it
    else:
        new_lines.append(line)
        
y14 = []
y24 = []
y34 = []
y44 = []
y54 = []
y64 = []
#for i in range(0,len(lines)):
for i in range(ini,ini+21):
    
    words = lines[i].split()
    
    y14.append(round(float(words[0]),3)) #y1 takes in the occupancy
    y34.append(words[2]) #y3 takes in the residue names
    y44.append(words[3])

for i in range(0,len(y34)):
    y24.append(y34[i][0:3])

for i in range(0,len(y44)):
    y54.append(y44[i][0:3])


for i in range(0,len(y44)):
    if y24[i] == 'GLY':
        y24[i] = 'G'
    if y24[i] == 'ALA':
        y24[i] = 'A'
    if y24[i] == 'VAL':
        y24[i] = 'V'
    if y24[i] == 'LEU':
        y24[i] = 'L'
    if y24[i] == 'ILE':
        y24[i] = 'I'
    if y24[i] == 'MET':
        y24[i] = 'M'
    if y24[i] == 'PHE':
        y24[i] = 'F'
    if y24[i] == 'TRP':
        y24[i] = 'W'
    if y24[i] == 'PRO':
        y24[i] = 'P'
    if y24[i] == 'SER':
        y24[i] = 'S'
    if y24[i] == 'THR':
        y24[i] = 'T'
    if y24[i] == 'CYS':
        y24[i] = 'C'
    if y24[i] == 'TYR':
        y24[i] = 'Y'
    if y24[i] == 'ASN':
        y24[i] = 'N'
    if y24[i] == 'GLN':
        y24[i] = 'Q'
    if y24[i] == 'ASP':
        y24[i] = 'D'
    if y24[i] == 'GLU':
        y24[i] = 'E'
    if y24[i] == 'LYS':
        y24[i] = 'K'
    if y24[i] == 'ARG':
        y24[i] = 'R'
    if y24[i] == 'HIS':
        y24[i] = 'H'
        
        
        
for i in range(0,len(y24)):
    y64.append(y24[i]  + str(int(y54[i]) + 1083 ))



#set width of bar
barWidth = 0.15



# set the positions of bar on X axis    
r1 = np.arange(len(y12))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

# Make the plot
plt.figure(figsize=(12,4))
plt.bar(r1, y11, color='r', width=barWidth, edgecolor='white', label='zone1')
plt.bar(r2, y12, color='#FFFF00', width=barWidth, edgecolor='white', label='zone2')
plt.bar(r3, y13, color='k', width=barWidth, edgecolor='white', label='zone3')
plt.bar(r4, y14, color='#FFB6C1', width=barWidth, edgecolor='white', label='zone4')



# Add xticks on the middle of the group bars
plt.ylabel('Hbond occupancy', fontweight='bold')
plt.xlabel('Residue', fontweight='bold')
plt.xticks([r + 1.5*barWidth for r in range(len(y11))], y64,fontsize=7,fontweight='bold')
plt.legend()

plt.savefig('zone_examine(new_actloop_c).png', bbox_inches = 'tight', dpi = 300)


plt.show()





















  





   
    
    