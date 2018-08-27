#!/usr/bin/env python
# -*- coding: utf-8 -*-


from sys import argv
import re


def initME():
    """
    to begin with ...
    """

    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED =  '\033[91m'
    #print in the screen
    print
    global cy,cb,cr,end
    cy = YELLOW
    cb = BLUE
    cr = RED
    end = '\033[0m'
    
    print      "+++++++++++++++++++++++"
    print cb + 'Gaussian Charges Reader' + end
    print      "+++++++++++++++++++++++"
    print 
    print "> Usage:    " +cb+" e_getQ.py gaussian.log -option" +end
    print 
    print "> Options:  " +cb+" npa,chelpg,mulliken,all"+end
    
    print "> Example:  " +cb+" e_getQ.py gaussian.log -all"+end

def readARG(argv):
    """
    reading the arguments
    """
    
    global read_chelpg,read_mulliken, read_npa
    
    read_chelpg = 0
    read_mulliken = 0
    read_npa = 0
    read_all = 0
    
    if argv.count("-npa"):
        read_npa = 1
    if argv.count("-chelpg"):
        read_chelpg = 1
    if argv.count("-mulliken"):
        read_mulliken = 1 
    if argv.count("-all"):
        read_chelpg = 1
        read_mulliken = 1
        read_npa = 1
        read_all = 1
    
    checkall = read_chelpg + read_mulliken+ read_npa + read_all
    
    if checkall == 0:
        print cr + "\nERROR:"+ end+ " please select an option.\n\n" 
    
    fname   = argv[1]
    
  
    return fname

def readGAU(lines):
    """
    get the XYZ coordinates and the CHELPG charges.
    """

    nlines = len(lines)
    chelpg_g09 = 'Fitting point charges to electrostatic potential'
    npa_g09 = ' Summary of Natural Population Analysis:'
    mulliken_g09 = ' Mulliken charges:'
    
    l = lines
    atom_tag,atom_q = [],[]

   
    i = 0
    for i in range(nlines):
        #l = lines[i]
        
        atom_tag,atom_q = [],[]
        if l[i].count(mulliken_g09) and read_mulliken:
            i += 2
            while l[i].count(' Sum of Mulliken charges =')==0:
                cols = re.split('\s+',l[i])
                print cols
                atom_tag.append(cols[2])
                atom_q.append(float(cols[3])) 
                i+=1
                
            print cb+ "\n=====> MULLIKEN CHARGES <=====" +end
            print "#%-4s %-4s  %13s" %('n','atom','charge')
            print cb+ "------------------------------" +end
            for j in range(len(atom_q)):
                print "%-4d  %-4s  %13.6f" %(j+1,atom_tag[j],atom_q[j])
            print cb+"==============================\n"+end
            
        #getting charges Gaussian 09
        atom_tag,atom_q = [],[]
        if l[i].count(chelpg_g09) and read_chelpg:
            i += 4
            while l[i].count('Sum of ESP charges =')==0:
                cols = re.split('\s+',l[i])
                #print cols
                atom_tag.append(cols[2])
                atom_q.append(float(cols[3])) 
                i+=1
                
            print cr+ "\n=====> CHELPG CHARGES <=====" +end
            print "#%-4s %-4s  %13s" %('n','atom','charge')
            print cr+ "----------------------------" +end
            for j in range(len(atom_q)):
                print "%-4d  %-4s  %13.6f" %(j+1,atom_tag[j],atom_q[j])
            print cr+"============================\n"+end
        
        atom_tag,atom_q = [],[]        
        if l[i].count(npa_g09) and read_npa:
            i += 6
            while l[i].count('=========')==0:
                cols = re.split('\s+',l[i])
                #print cols
                atom_tag.append(cols[1])
                atom_q.append(float(cols[3])) 
                i+=1
                
            print cy+ "\n=====> NPA CHARGES <=====" +end
            print "#%-4s %-4s  %13s" %('n','atom','charge')
            print cy+ "-------------------------" +end
            for j in range(len(atom_q)):
                print "%-4d  %-4s  %13.6f" %(j+1,atom_tag[j],atom_q[j])
            print cy+"=========================\n"+end
            

    

###
#MAIN
###

initME()

#print argv
fname = readARG(argv)

mol = open(fname,'r')

lines = mol.readlines()

if fname.count('.log'):
    readGAU(lines)






