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
    print("here",line) 
    findex=int(line[7:11])  # OK, w Simons shait
    fname=line[12:16]   # sims OK
    fresname=line[17:20]   # NOK A->RA; U->RU; G->RG & C->RC
    #fresid=line[21:23]   #int(line[22:26])
    fchain=int(line[23:27])  # OK
    fx=float(line[30:38])
    fy=float(line[38:46])
    fz=float(line[46:54])
    fq=float(line[55:62])
    fr=float(line[63:70])
    #fsegid=line[72:76]
    #felement=line[76:78]

    index.append(findex)
    atomname.append(fname)
    resname.append(fresname)
    #resid.append(fresid)
    chainid.append(fchain)
    x.append(fx)
    y.append(fy)
    z.append(fz)
    charge.append(fq)
    radii.append(fr)

  return index,atomname,resname,chainid,x,y,z,charge,radii #,index

#def changeRNAresNames():
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

