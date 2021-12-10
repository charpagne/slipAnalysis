# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:17:36 2020

@author: Arsenic
"""

import numpy as np
from matplotlib import pyplot as plt, colors, colorbar, cm
import crystallography
import seaborn as sns
sns.set(style="whitegrid")

lattice = 'FCC'

# load grain euler angles from TSL OIM
grain = 48
phi1= np.genfromtxt("grainfile2.txt",usecols=[1]).astype(float)
phi= np.genfromtxt("grainfile2.txt",usecols=[2]).astype(float)
phi2= np.genfromtxt("grainfile2.txt",usecols=[3]).astype(float)
phi1 = np.insert(phi1, 0, 0)
phi = np.insert(phi, 0, 0)
phi2 = np.insert(phi2, 0, 0)
eulers = np.column_stack((phi1,phi,phi2))  # Euler angles are in degrees
numGrains = eulers.shape[0]

# plot schmid factors
eulers_grain = eulers[grain]
if lattice == 'BCC':
    for plane_type in ('110','112','123','134'):
        schmidFactors = np.array(crystallography.calc_sfs(eulers_grain,plane_type,lattice))
        if plane_type == '110':
            legend_x =np.array(['(110)\n[-111]','(110)\n[1-11]',
                           '(101)\n[-111]','(101)\n[11-1]',
                           '(011)\n[1-11]','(011)\n[11-1]',
                           '(10-1)\n[111]','(10-1)\n[1-11]',
                           '(1-10)\n[111]','(1-10)\n[11-1]',
                           '(01-1)\n[111]','(01-1)\n[-111]'])
            fig1 = plt.figure(figsize=(9,4))
            sfbars = plt.bar(x=np.arange(1,schmidFactors.shape[0]+1), height=schmidFactors, 
                             width=0.8, align='center', data=None,tick_label = legend_x,color='gold')
            plt.grid(False)
            fig1.savefig('grain_%s_sf_%s.png' %(grain,int(plane_type)), format='png', dpi=1000 )
        if plane_type == '112':
            legend_x =np.array(['(112)\n[11-1]','(121)\n[1-11]','(211)\n[-111]',
                            '(11-2)\n[111]','(1-21)\n[111]','(-211)\n[111]',
                           '(-112)\n[1-11]','(2-11)\n[11-1]','(12-1)\n[-111]',
                           '(1-12)\n[-111]','(21-1)\n[1-11]','(-121)\n[11-1]'])
            fig2 = plt.figure(figsize=(9,4))
            sfbars = plt.bar(x=np.arange(1,schmidFactors.shape[0]+1), height=schmidFactors, 
                             width=0.8, align='center', data=None,tick_label = legend_x,color='navy')
            plt.grid(False)
            fig2.savefig('grain_%s_sf_%s.png' %(grain,int(plane_type)), format='png', dpi=1000 )
        if plane_type == '123':
            legend_x =np.array(['(123)\n[11-1]','(312)\n[-111]','(231)\n[1-11]',
                            '(-123)\n[1-11]','(3-12)\n[11-1]','(23-1)\n[-111]',
                           '(1-23)\n[-111]','(31-2)\n[1-11]','(2-31)\n[11-1]',
                           '(12-3)\n[111]','(-312)\n[111]','(2-31)\n[111]',
                           '(321)\n[-111]','(213)\n[11-1]','(132)\n[1-11]',
                           '(-321)\n[111]','(21-3)\n[111]','(1-32)\n[111]',
                           '(3-21)\n[11-1]','(-213)\n[1-11]','(13-2)\n[-111]',
                           '(32-1)\n[1-11]','(2-13)\n[-111]','(-132)\n[11-1]'])
            fig3 = plt.figure(figsize=(18,4))
            sfbars = plt.bar(x=np.arange(1,schmidFactors.shape[0]+1), height=schmidFactors, 
                             width=0.8, align='center', data=None,tick_label = legend_x,color='mediumvioletred')
            plt.grid(False)
            fig3.savefig('grain_%s_sf_%s.png' %(grain,int(plane_type)), format='png', dpi=1000 )
        if plane_type == '134':
            legend_x =np.array(['(134)\n[11-1]','(413)\n[-111]','(341)\n[1-11]',
                            '(-134)\n[1-11]','(4-13)\n[11-1]','(34-1)\n[-111]',
                           '(1-34)\n[-111]','(41-3)\n[1-11]','(3-41)\n[11-1]',
                           '(13-4)\n[111]','(-413)\n[111]','(3-41)\n[111]',
                           '(431)\n[111]','(314)\n[111]','(143)\n[111]',
                           '(-431)\n[111]','(31-4)\n[111]','(1-43)\n[111]',
                           '(4-31)\n[111]','(-314)\n[111]','(14-3)\n[111]',
                           '(43-1)\n[111]','(3-14)\n[111]','(-143)\n[111]'])
            fig4 = plt.figure(figsize=(18,4))
            sfbars = plt.bar(x=np.arange(1,schmidFactors.shape[0]+1), height=schmidFactors, 
                             width=0.8, align='center', data=None,tick_label = legend_x,color='darkgreen')
            plt.grid(False)
            fig4.savefig('grain_%s_sf_%s.png' %(grain,int(plane_type)), format='png', dpi=1000 )

    # plot plane traces
    file = open(('grain_%s_plane-traces.txt' %grain),'w')
    file.write("grain:%s" %grain + "\n") 
    for plane_type in ('110','112','123','134'):
        planes = crystallography.gen_planes(plane_type)
        traces = []
        fig5 = plt.figure(figsize=(5,5))
        color=iter(cm.nipy_spectral(np.linspace(0,1,planes.shape[0])))
        ax = plt.subplot(111)
        ax.set_ylim([-1.2, 1.2])   # set the bounds to be 10, 10
        ax.set_xlim([-1.2, 1.2])
        plt.grid(False)
        for plane in range(planes.shape[0]):
            c=next(color)
            file.write("plane:%s%s%s" %(planes[plane,0],planes[plane,1],planes[plane,2]) + "\t")
            traces.append(crystallography.plane_trace_components(planes[plane],eulers_grain))
            file.write(str(crystallography.plane_trace_components(planes[plane],eulers_grain)) + "\n")
            x_values = (traces[plane][0], -traces[plane][0])
            y_values = (traces[plane][1],-traces[plane][1])
            plt.plot(x_values, y_values, '-',c=c, label=(str(planes[plane,0]) + str(planes[plane,1]) + str(planes[plane,2])))
            plt.axis('off')
            plt.gca().legend(loc='center left', bbox_to_anchor=(1, 0.5))
        fig5.savefig('grain%s_traces_%s.png' %(grain,int(plane_type)),format='png', dpi=200, bbox_inches='tight')
    file.close()
    #
    file = open(('grain_%s_gamma-angles.txt' %grain),'w')
    file.write("grain:%s" %grain + "\n") 
    for plane_type in ('110','112','123','134'):
        planes = crystallography.gen_planes(plane_type)
        directions = crystallography.gen_directions()
        for plane in range(planes.shape[0]):
            file.write("plane:%s%s%s" %(planes[plane,0],planes[plane,1],planes[plane,2]) + "\n")
            for direction in range(directions.shape[0]):
                if np.dot(planes[plane],directions[direction]) == 0:
                    file.write("direction: %s%s%s"  %(directions[direction,0],directions[direction,1],directions[direction,2]) + "\t")
                    gamma_angle = crystallography.get_gamma_angle(planes[plane],directions[direction],eulers_grain)
                    file.write(str(gamma_angle) + "\n")
    file.close()
    
    
if lattice == 'FCC':
    schmidFactors = np.array(crystallography.calc_sfs(eulers_grain,'111',lattice))
    legend_x = np.array(['(-111)\n[0-11]','(-111)\n[101]','(-111)\n[110]',
                           '(111)\n[0-11]','(111)\n[-101]','(111)\n[-110]',
                           '(-1-11)\n[011]','(-1-11)\n[101]','(-1-11)\n[-110]',
                           '(1-11)\n[011]','(1-11)\n[-101]','(1-11)\n[110]'])
    fig1 = plt.figure(figsize=(9,4))
    sfbars = plt.bar(x=np.arange(1,schmidFactors.shape[0]+1), height=schmidFactors, 
                             width=0.8, align='center', data=None,tick_label = legend_x,color='navy')
    plt.grid(False)
    fig1.savefig('grain_%s_sf.png' %(grain), format='png', dpi=1000)

    # calculate traces through their angle
    file = open(('grain_%s_plane-traces.txt' %grain),'w')
    file.write("grain:%s" %grain + "\n") 
    planes = crystallography.gen_planes('111')
    traces = []
    for plane in range(planes.shape[0]):
        file.write("plane:%s%s%s" %(planes[plane,0],planes[plane,1],planes[plane,2]) + "\t")
        traces.append(crystallography.plane_trace_components(planes[plane],eulers_grain))
        file.write(str(crystallography.plane_trace_components(planes[plane],eulers_grain)) + "\n")
    file.close()
    #
    file = open(('grain_%s_gamma-angles.txt' %grain),'w')
    file.write("grain:%s" %grain + "\n") 
    planes = crystallography.gen_planes('111')
    directions = crystallography.gen_directions(lattice)
    for plane in range(planes.shape[0]):
        file.write("plane:%s%s%s" %(planes[plane,0],planes[plane,1],planes[plane,2]) + "\n")
        for direction in range(directions.shape[0]):
            if np.dot(planes[plane],directions[direction]) == 0:
                file.write("direction: %s%s%s" %(directions[direction,0],directions[direction,1],directions[direction,2]) + "\t")
                gamma_angle = crystallography.get_gamma_angle(planes[plane],directions[direction],eulers_grain)
                file.write(str(gamma_angle) + "\n")
    file.close()
    
        # plot plane traces
    file = open(('grain_%s_plane-traces.txt' %grain),'w')
    file.write("grain:%s" %grain + "\n") 
    planes = crystallography.gen_planes('111')
    traces = []
    fig5 = plt.figure(figsize=(5,5))
    color=iter(cm.nipy_spectral(np.linspace(0,1,planes.shape[0])))
    ax = plt.subplot(111)
    ax.set_ylim([-1.2, 1.2])   # set the bounds to be 10, 10
    ax.set_xlim([-1.2, 1.2])
    plt.grid(False)
    for plane in range(planes.shape[0]):
        c=next(color)
        file.write("plane:%s%s%s" %(planes[plane,0],planes[plane,1],planes[plane,2]) + "\t")
        traces.append(crystallography.plane_trace_components(planes[plane],eulers_grain))
        file.write(str(crystallography.plane_trace_components(planes[plane],eulers_grain)) + "\n")
        x_values = (traces[plane][0], -traces[plane][0])
        y_values = (traces[plane][1],-traces[plane][1])
        plt.plot(x_values, y_values, '-',c=c, label=(str(planes[plane,0]) + str(planes[plane,1]) + str(planes[plane,2])))
        plt.axis('off')
        plt.gca().legend(loc='center left', bbox_to_anchor=(1, 0.5))
    fig5.savefig('grain%s_traces.png' %(grain),format='png', dpi=200, bbox_inches='tight')
    file.close()
    #
    file = open(('grain_%s_gamma-angles.txt' %grain),'w')
    file.write("grain:%s" %grain + "\n") 
    planes = crystallography.gen_planes('111')
    directions = crystallography.gen_directions()
    for plane in range(planes.shape[0]):
        file.write("plane:%s%s%s" %(planes[plane,0],planes[plane,1],planes[plane,2]) + "\n")
        for direction in range(directions.shape[0]):
            if np.dot(planes[plane],directions[direction]) == 0:
                file.write("direction: %s%s%s"  %(directions[direction,0],directions[direction,1],directions[direction,2]) + "\t")
                gamma_angle = crystallography.get_gamma_angle(planes[plane],directions[direction],eulers_grain)
                file.write(str(gamma_angle) + "\n")
    file.close()