import sys
#index,atomname,resname,chainid,x,y,z,charge,radii=pqrread('outTwoHP_colSP.pqr',sys.argv[0],10)
#writepqr2xzyr('outTwoHP_colSP.xyzr',resname,x,y,z,radii)

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
    firstL=str(line[0:1])
    if firstL=="A":
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
  return index,atomname,resname,chainid,x,y,z,charge,radii #,index

def writepqr2xzyr(filename,resname,x,y,z,radii):  # outTwoHP_colSP.xyzr  pqr2xyzr.py
  file = open(filename,'w')
  for pid in range(0,len(resname)):
    xpos = x[pid]
    ypos = y[pid]
    zpos = z[pid]
    radiit=radii[pid]
    st = "%8.3f%1s%8.3f%1s%8.3f%1s%2.4f\n"%(xpos,'',ypos,'',zpos,'',radiit)
    file.write(st)
  file.close()

def reWritepqr(filename,atomname,resname,chainid,x,y,z,charge,radii):
  file = open(filename,'w')
  for pid in range(0,len(resname)):
    atomn= atomname[pid]
    resn = resname[pid]
    chaini = chainid[pid]
    xpos = x[pid]
    ypos = y[pid]
    zpos = z[pid]
    chargit=charge[pid]
    radiit=radii[pid]
    st = "%-6s%5d %-4s%1s%3s %3d %8.3f%1s%8.3f%1s%8.3f%6.2f%6.2f\n"%('ATOM  ',(pid+1),atomn,'',resn,chaini,xpos,'',ypos,'',zpos,chargit,radiit)
    file.write(st)
  file.close()
index,atomname,resname,chainid,x,y,z,charge,radii=pqrread('outTwoHP_colSP2.pqr',int(sys.argv[1]),10)
writepqr2xzyr('outTwoHP_colSP.xyzr',resname,x,y,z,radii)
reWritepqr('outTwoHP_colSP.pqr',atomname,resname,chainid,x,y,z,charge,radii)


