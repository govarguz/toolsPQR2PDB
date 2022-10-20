"""
@author: Horacio V. Guzman, Ph.D.
@project: pyF4all
@date: 11.05.2020

horacio.v.g@gmail.com

**********************************************************************************************************************************
PDB - read and write pdb format, writes it into a specific pdb format to be read by pdb2pqr. While also, rewritting pqr filetypes
**********************************************************************************************************************************

"""

from math import sqrt

def pdbread(filename,natoms,header):

  index=[]
  atomname=[]
  resname=[]
  chainid=[]
  resid=[]
  x=[]
  y=[]
  z=[]
  alpha=[]
  beta=[]
  segid=[]
  element=[]

  file = open(filename,'r')
  for i in range(header):
    line = file.readline()
  for i in range(natoms):
    line = file.readline() 
    findex=int(line[7:11])
    fname=line[12:16]
    fresname=line[17:20]
    fresid=line[21:23]
    fchain=int(line[23:27])
    fx=float(line[30:38])
    fy=float(line[38:46])
    fz=float(line[46:54])
    falpha=float(line[55:60])
    fbeta=float(line[60:66])
    fsegid=line[72:76]
    felement=line[76:78]

    index.append(findex)
    atomname.append(fname)
    if fresname=='  A':
      fresname=' RA'
    elif fresname=='  C':
      fresname=' RC'	
    elif fresname=='  U':
      fresname=' RU'
    elif fresname=='  G':
      fresname=' RG'
    else:
      print("No more RNA residue names have been found")			
    resname.append(fresname)
    resid.append(fresid)
    chainid.append(fchain)
    x.append(fx)
    y.append(fy)
    z.append(fz)
    alpha.append(falpha)
    beta.append(fbeta)
    segid.append(fsegid)
    element.append(felement)

  return index,atomname,resname,resid,chainid,x,y,z,alpha,beta,segid,element

def pqrread(filename,natoms,header):   #outTwoHP_colSP.pqr

  index=[]
  atomname=[]
  resname=[]
  chainid=[]
  resid=[]
  x=[]
  y=[]
  z=[]
  charge=[]
  radii=[]
  file = open(filename,'r')
  for i in range(header):
    line = file.readline()
  for i in range(natoms):
    line = file.readline() 
    #print("here",line) 
    findex=int(line[7:11])
    fname=line[12:16]   
    fresname=line[17:20]
    fchain=int(line[23:27])
    fx=float(line[30:38])
    fy=float(line[38:46])
    fz=float(line[46:54])
    fq=float(line[55:62])
    fr=float(line[63:70])

    index.append(findex)
    atomname.append(fname)
    resname.append(fresname)
    chainid.append(fchain)
    x.append(fx)
    y.append(fy)
    z.append(fz)
    charge.append(fq)
    radii.append(fr)

  return index,atomname,resname,chainid,x,y,z,charge,radii

def writepqr2xzyr(filename,resname,x,y,z,radii): 
  file = open(filename,'w')
  for pid in range(0,len(resname)):
    xpos = x[pid]
    ypos = y[pid]
    zpos = z[pid]
    radiit=radii[pid]		
    st = "%8.3f%1s%8.3f%1s%8.3f%1s%2.4f\n"%(xpos,'',ypos,'',zpos,'',radiit)
    file.write(st)
  file.close()

def pdbreadIndexRange(filename,startI,natoms,header):

  index=[]
  atomname=[]
  resname=[]
  chainid=[]
  resid=[]
  x=[]
  y=[]
  z=[]
  alpha=[]
  beta=[]
  segid=[]
  element=[]

  file = open(filename,'r')
  for i in range(header):
    line = file.readline()
  for i in range(startI):
    line = file.readline()
  for i in range(startI+1,natoms):
    line = file.readline() 
    fname=line[12:16]
    fresname=line[17:20]
    fresid=line[21:22]
    fchain=int(line[23:26])
    fx=float(line[30:38])
    fy=float(line[38:46])
    fz=float(line[46:54])
    falpha=float(line[55:60])
    fbeta=float(line[60:66])
    fsegid=line[72:76]
    felement=line[76:78]

    atomname.append(fname)
    resname.append(fresname)
    resid.append(fresid)
    chainid.append(fchain)
    x.append(fx)
    y.append(fy)
    z.append(fz)
    alpha.append(falpha)
    beta.append(fbeta)
    segid.append(fsegid)
    element.append(felement)
  return atomname,resname,resid,chainid,x,y,z,alpha,beta,segid,element

def writepdb(filename,atomname,resname,resid,chainid,x,y,z,alpha,beta):
  file = open(filename,'w')
  for pid in range(0,len(resname)):
    xpos = x[pid]
    ypos = y[pid]
    zpos = z[pid]
    atomn= atomname[pid]
    resn = resname[pid]
    resi = resid[pid]
    chaini = chainid[pid]
    alph=alpha[pid]
    bet=beta[pid]		
    st = "%-6s%5d %-4s%3s%1s%1s %3d%3s%8.3f%1s%8.3f%1s%8.3f%6.2f%6.2f\n"%('ATOM  ',(pid),atomn,resn,'',resi,chaini,'',xpos,'',ypos,'',zpos,alph,bet)
    file.write(st)
  file.write('END\n')
  file.close()