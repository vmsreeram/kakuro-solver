# from ast import Dict
# from asyncio.proactor_events import constants
# import copy
import getopt
import itertools
from queue import Queue
import sys
# from csp import *

# returns all possible selections and permutaions of 1,9 of length n summing to total
def possible_combinations(n, total): 
   values=[1,2,3,4,5,6,7,8,9]
   # for i in range(n):
   #    values.append(i+1)
   #    if i==9:
   #       break
   return [combination for combination in itertools.combinations(values, n) if sum(combination) == total]

def getDomain(n,total):    #sets domain as set 1-9; this will be reduced in AC3
   domain=set()
   for alll in {1,2,3,4,5,6,7,8,9}:
      domain.add(alll)
   return domain                                   #override to have domain of each xi to be 1-9
   # for comb in possible_combinations(n, total):
   #    for val in comb:
   #       domain.add(val)
   # return domain
inpVerts=[]
inpHoris=[] 

def parseInputs(inputfile):      #reads input file to get num of rows, cols, given matrices
   global inpVerts,inpHoris
   fObj = open(inputfile,"r")
   allLines=fObj.readlines()

   try:
      assert allLines[0][:5]=="rows="
   except:
      print("incorrect input format - line 1\n")
      sys.exit(1)
   nRowsStr=allLines[0][5:]
   nRows= int(nRowsStr[:(len(nRowsStr)-1)])

   try:
      assert allLines[1][:8]=="columns="
   except:
      print("incorrect input format - line 2\n")
      sys.exit(1)
   nColsStr=allLines[1][8:]
   nCols= int(nColsStr[:(len(nColsStr)-1)])
   # print(nRows,nCols)

   # inpHoris=[]                                        
   try:
      assert allLines[2]=="Horizontal\n"
   except:
      print("incorrect input format - line 3\n")
      sys.exit(1)
   try:
      for ln in range(3,nRows+3):
         sz = len(allLines[ln])
         thisLine = allLines[ln][:(sz-1)].split(",")
         assert len(thisLine)==nCols
         inpHoris.append(thisLine)
   except:
      print("incorrect input format - horizontal inputs\n")
      sys.exit(1)
   # print(inpHoris)

   # inpVerts=[]                                        
   try:
      assert allLines[nRows+3]=="Vertical\n"
   except:
      print("incorrect input format - line",nRows+4,"\n")
      sys.exit(1)
   try:
      for ln in range(nRows+4,2*nRows+4):
         sz = len(allLines[ln])
         thisLine = allLines[ln][:(sz-1)].split(",")
         assert len(thisLine)==nCols
         inpVerts.append(thisLine)
   except:
      print("incorrect input format - vertical inputs\n")
      sys.exit(1)
   # print(inpVerts)

   return nRows,nCols

ConstraintMatrix=[]
Domain=dict()
DomainUi=[]

def getConstraintMatrix(nRows,nCols):     # generates binary constraint matrix and also returns domain of each type of variables
   global inpHoris,inpVerts,ConstraintMatrix,Domain,DomainUi
   # consNum=0
   #Horizontals
   for i in range(nRows):
      zeroIndxs=[]
      target=0
      for j in range(nCols):
         if inpHoris[i][j]=='#':
            if j==nCols-1:
               if len(zeroIndxs)==0:
                  continue
               constraint=[]
               for r in range(nRows):
                  for x in range(nCols):
                     if (r==i) and (x in zeroIndxs):
                        constraint.append(1)
                     else:
                        constraint.append(0)
               ConstraintMatrix.append(constraint)
               #$
               permutn=[]
               for comb in possible_combinations(len(zeroIndxs), target):
                  for perm in itertools.permutations(comb):
                     permutn.append(perm)
               DomainUi.append(permutn)
               #$
               #
               #
               # Domain.update(...)
               zeroDomain=getDomain(len(zeroIndxs), target)
               for zeroIndex in zeroIndxs:
                  # coor=tuple(i,zeroIndex)
                  Domain.update({(i,zeroIndex): zeroDomain})

               #
               #
               zeroIndxs=[]
            else:
               continue
         elif inpHoris[i][j]!='0':
            if len(zeroIndxs)==0:
               target=int(inpHoris[i][j])
            else:
               constraint=[]
               for r in range(nRows):
                  for x in range(nCols):
                     if (r==i) and (x in zeroIndxs):
                        constraint.append(1)
                     else:
                        constraint.append(0)
               ConstraintMatrix.append(constraint)
               #$
               permutn=[]
               for comb in possible_combinations(len(zeroIndxs), target):
                  for perm in itertools.permutations(comb):
                     permutn.append(perm)
               DomainUi.append(permutn)
               #$
               #
               #
               #
               zeroDomain=getDomain(len(zeroIndxs), target)
               for zeroIndex in zeroIndxs:
                  Domain.update({(i,zeroIndex): zeroDomain})
               #
               #
               zeroIndxs=[]
               target=int(inpHoris[i][j])
         elif inpHoris[i][j]=='0':
            zeroIndxs.append(j)
            if j==nCols-1:
               constraint=[]
               for r in range(nRows):
                  for x in range(nCols):
                     if (r==i) and (x in zeroIndxs):
                        constraint.append(1)
                     else:
                        constraint.append(0)
               ConstraintMatrix.append(constraint)
               #$
               permutn=[]
               for comb in possible_combinations(len(zeroIndxs), target):
                  for perm in itertools.permutations(comb):
                     permutn.append(perm)
               DomainUi.append(permutn)
               #$
               #
               #
               #
               zeroDomain=getDomain(len(zeroIndxs), target)
               for zeroIndex in zeroIndxs:
                  Domain.update({(i,zeroIndex): zeroDomain})
               #
               #
               zeroIndxs=[]

   #Verticals
   for i in range(nCols):
      zeroIndxs=[]
      target=0
      for j in range(nRows):
         if inpVerts[j][i]=='#':
            if j==nRows-1:
               if len(zeroIndxs)==0:
                  continue
               constraint=[]
               for x in range(nRows):
                  for r in range(nCols):
                     if (r==i) and (x in zeroIndxs):
                        constraint.append(1)
                     else:
                        constraint.append(0)
               ConstraintMatrix.append(constraint)
               #$
               permutn=[]
               for comb in possible_combinations(len(zeroIndxs), target):
                  for perm in itertools.permutations(comb):
                     permutn.append(perm)
               DomainUi.append(permutn)
               #$
               #
               #
               #
               zeroDomain=getDomain(len(zeroIndxs), target)
               for zeroIndex in zeroIndxs:
                  try:
                     curr=(Domain[(zeroIndex,i)])
                     Domain.update({(zeroIndex,i): zeroDomain.intersection(curr)})
                  except:
                     Domain.update({(zeroIndex,i): zeroDomain})
               #
               #
               zeroIndxs=[]
            else:
               continue
         elif inpVerts[j][i]!='0':
            if len(zeroIndxs)==0:
               target=int(inpVerts[j][i])
            else:
               constraint=[]
               for x in range(nRows):
                  for r in range(nCols):
                     if (r==i) and (x in zeroIndxs):
                        constraint.append(1)
                     else:
                        constraint.append(0)
               ConstraintMatrix.append(constraint)
               #$
               permutn=[]
               for comb in possible_combinations(len(zeroIndxs), target):
                  for perm in itertools.permutations(comb):
                     permutn.append(perm)
               DomainUi.append(permutn)
               #$
               #
               #
               #
               zeroDomain=getDomain(len(zeroIndxs), target)
               for zeroIndex in zeroIndxs:
                  try:
                     curr=(Domain[(zeroIndex,i)])
                     Domain.update({(zeroIndex,i): zeroDomain.intersection(curr)})
                  except:
                     Domain.update({(zeroIndex,i): zeroDomain})
               #
               #
               zeroIndxs=[]
               target=int(inpVerts[j][i])
         elif inpVerts[j][i]=='0':
            zeroIndxs.append(j)
            if j==nRows-1:
               constraint=[]
               for x in range(nRows):
                  for r in range(nCols):
                     if (r==i) and (x in zeroIndxs):
                        constraint.append(1)
                     else:
                        constraint.append(0)
               ConstraintMatrix.append(constraint)
               #$
               permutn=[]
               for comb in possible_combinations(len(zeroIndxs), target):
                  for perm in itertools.permutations(comb):
                     permutn.append(perm)
               DomainUi.append(permutn)
               #$
               #
               #
               #
               zeroDomain=getDomain(len(zeroIndxs), target)
               for zeroIndex in zeroIndxs:
                  # coor=tuple(i,zeroIndex)
                  try:
                     curr=(Domain[(zeroIndex,i)])
                     Domain.update({(zeroIndex,i): zeroDomain.intersection(curr)})
                  except:
                     Domain.update({(zeroIndex,i): zeroDomain})
               #
               #
               zeroIndxs=[]

   return

# def getConsQueue(ConstraintMatrix):       
#    consQueue=Queue()
#    for i in range(len(ConstraintMatrix)):
#       for j in range(len(ConstraintMatrix[i])):
#          if ConstraintMatrix[i][j]==1:
#             consQueue.put((i,j))
#    return consQueue
   
############

def AC3(allArcs,Domain,DomainUi,nCols):   # function AC-3(csp) returns false if an inconsistency is found and true otherwise
    global ConstraintMatrix
   #  print("Start AC3")
    q = Queue() 
    for eachArc in allArcs:
        q.put(eachArc)

   #  print("q.qsize()=",q.qsize())
    while not q.qsize()==0:
        qget=q.get()
        (Xi,Xj),typ=qget     # typ will the type (x or u) of Xi
        
        if typ=='x':
            # print("type is x")
            Xi_x=Xi//nCols
            Xi_y=Xi%nCols
            posInDj=0
            for cmv in range(len(ConstraintMatrix[Xj][:])):
                if cmv==Xi:
                    break
                if ConstraintMatrix[Xj][cmv]==1:
                    posInDj+=1
            # print("preCall \nDi=",Domain[(Xi_x,Xi_y)])
            revised,Di=REVISEx(Domain[(Xi_x,Xi_y)],DomainUi[Xj], posInDj)
            # print("revised=",revised)
            # print("Di=",Di)
            if revised:
                Domain[(Xi_x,Xi_y)]=Di
                if len(Domain[(Xi_x,Xi_y)])==0:
                  #   print("end AC3 - f")
                    return False,Domain,DomainUi
               #  print("for Xk in range(len(ConstraintMatrix)):")
               #  print("len(ConstraintMatrix)=",len(ConstraintMatrix))
                for Xk in range(len(ConstraintMatrix)):
                  #   print("Xk=",Xk)
                    if ConstraintMatrix[Xk][Xi]==0 or Xk==Xj:
                        continue
                  #   print("put",((Xk,Xi),'u'))
                    q.put(((Xk,Xi),'u'))
        elif typ=='u':
            # print("type is u")
            # print("nCols=",nCols)
            Xj_x=Xj//nCols
            Xj_y=Xj%nCols

            # print("(Xj_x,Xj_y)=",end=" ")
            # print('(' + str(Xj_x) + ',' + str(Xj_y)+')')

            posInDi=0
            for cmv in range(len(ConstraintMatrix[Xi][:])):
                if cmv==Xj:
                    break
                if ConstraintMatrix[Xi][cmv]==1:
                    posInDi+=1
            # print("posInDi = ",posInDi)

            # print("preCall \nDi=",DomainUi[Xi])
            revised,Di=REVISEu(DomainUi[Xi],Domain[(Xj_x,Xj_y)],posInDi)
            # print("revised=",revised)
            # print("Di=",Di)
            if revised: 
                DomainUi[Xi]=Di
                if len(DomainUi[Xi])==0:
                  #   print("end AC3 - f")
                    return False,Domain,DomainUi
                for Xk in range(len(ConstraintMatrix[Xi][:])):
                    if ConstraintMatrix[Xi][Xk]==0 or Xk==Xj:
                        continue
                    q.put(((Xk,Xi),'x'))
   #  print("end AC3 - t")
    return True,Domain,DomainUi

def REVISEx(Di,Dj,posInDj):     #returns true iff we revise the domain of Xi revised else false
    revised=False
    DiCopy=set()
    for valu in Di:
       DiCopy.add(valu)
    for x in DiCopy:
        # if """no value y in Dj allows (x ,y) to satisfy the constraint between Xi and Xj then""":
        #     """delete x from Di"""
        #     revised=True
        found=False
        for y in Dj:
            if y[posInDj]==x:
                found=True
                break
        if not found:
            Di.discard(x)
            revised=True
    return revised,Di

def REVISEu(Di,Dj,posInDi):     #returns true iff we revise the domain of Xi revised else false
   #  print("inside REVISEu")
    revised=False
    DiCopy=Di[:]
    for x in DiCopy:
      #   print(x)
        # if """no value y in Dj allows (x ,y) to satisfy the constraint between Xi and Xj then""":
        #     """delete x from Di"""
        #     revised=True
        found=False
        for y in Dj:
            # print(y)
            if y==x[posInDi]:
                found=True
                break
        if not found:
            Di.remove(x)
            revised=True
    return revised,Di

#############

def numofConflics(unassignedVar, val, inpHoris,inpVerts,nRows,nCols,assignment): #returns 0 if no conflictsare there  if val is assigned to unassignedVars, otherwise it returns poitive integer
   rowNeighbours=[]
   colNeighbours=[]


   rowTarget=-1
   i=unassignedVar[0]
   j=unassignedVar[1]+1
   while(j<nCols):
      if inpHoris[i][j]=='0':
         rowNeighbours.append((i,j))
         j+=1
      else:
         break
   i=unassignedVar[0]
   j=unassignedVar[1]-1
   # print("i,j=(",i,",",j,")")
   while(j>=0):
      if inpHoris[i][j]=='0':
         rowNeighbours.append((i,j))
         j-=1
      elif inpHoris[i][j]!='#':
         rowTarget=int(inpHoris[i][j])
         break
      else:
         # print(".")
         return 2,rowNeighbours,colNeighbours #never


   
   colTarget=-1
   i=unassignedVar[0]+1
   j=unassignedVar[1]
   while(i<nRows):
      if(inpVerts[i][j]=='0'):
         colNeighbours.append((i,j))
         i+=1
      else:
         break
   i=unassignedVar[0]-1
   j=unassignedVar[1]
   while(i>=0):
      if(inpVerts[i][j]=='0'):
         colNeighbours.append((i,j))
         i-=1
      elif(inpVerts[i][j]!='#'):
         colTarget=int(inpVerts[i][j])
         break
      else:
         # print(".,")
         return 2,rowNeighbours,colNeighbours #never
   
   rSum=0
   foundUnassigned=False
   for nr in rowNeighbours:
      if assignment[nr]!=-1 and assignment[nr]==val:
         # print("row alldif wrong")
         return 1,rowNeighbours,colNeighbours
      elif assignment[nr]!=-1:
         rSum+=assignment[nr]
      elif assignment[nr]==-1:
         foundUnassigned=True
   # print("foundUnassigned=",foundUnassigned,"rowTarget=",rowTarget,"rSum=",rSum)
   if (not foundUnassigned) and (rSum+val!=rowTarget):
      
      # print("rsum wrong")
      return 1,rowNeighbours,colNeighbours
   
   cSum=0
   foundUnassigned=False
   for nc in colNeighbours:
      if assignment[nc]!=-1 and assignment[nc]==val:
         # print("col alldif wrong")
         return 1,rowNeighbours,colNeighbours
      elif assignment[nc]!=-1:
         cSum+=assignment[nc]
      elif assignment[nc]==-1:
         foundUnassigned=True
   if (not foundUnassigned) and (cSum+val!=colTarget):
      # print("csum wrong")
      return 1,rowNeighbours,colNeighbours
   
   return 0,rowNeighbours,colNeighbours

def AllNeighbors(Xi,inpHoris,inpVerts):            # returns a list of all neighbors of variable Xi
   Xi_nrs=[]
   i=Xi[0]
   j=Xi[1]+1
   while(j<len(inpHoris[0])):
      if inpHoris[i][j]=='0':
         Xi_nrs.append((i,j))
         j+=1
      else:
         break
   i=Xi[0]
   j=Xi[1]-1
   while(j>=0):
      if inpHoris[i][j]=='0':
         Xi_nrs.append((i,j))
         j-=1
      else:
         break
   i=Xi[0]+1
   j=Xi[1]
   while(i<len(inpHoris)):
      if(inpVerts[i][j]=='0'):
         Xi_nrs.append((i,j))
         i+=1
      else:
         break
   i=Xi[0]-1
   j=Xi[1]
   while(i>=0):
      if(inpVerts[i][j]=='0'):
         Xi_nrs.append((i,j))
         i-=1
      else:
         break
   return Xi_nrs

def AC3_Mac(allArcs,Domain,inpHoris,inpVerts,assignment):      # specifically made AC3 for mac
   #print("#")
   #print("allArcs=",allArcs)
   q = Queue() 
   for eachArc in allArcs:
      q.put(eachArc)
   #print("q.qsize()=",q.qsize())
   while not q.qsize()==0:
      # print("$")
      qget=q.get()
      # print("$$")
      Xi,Xj=qget
      revised,Di = Revise_Mac(Xi,Xj,Domain[Xi],Domain[Xj],assignment,inpHoris,inpVerts)
      if revised:
         Domain[Xi]=Di
         if(len(Di) == 0):
            return False,Domain
         Xi_nrs=AllNeighbors(Xi,inpHoris,inpVerts)
         
         for Xk in Xi_nrs:
            if Xk==Xj:
               continue
            q.put((Xk,Xi))
   #print("##")
   return True,Domain

def isThisOk(Xi,x,Xj,y,assignment,inpHoris,inpVerts):             # to check if this assignment is ok according to constraints
   # Xi_nrs = AllNeighbors(Xi,inpHoris,inpVerts)
   # Xj_nrs = AllNeighbors(Xj,inpHoris,inpVerts)
   # for xi_nr in Xi_nrs:
   #    if assignment[xi_nr]!=-1 and assignment[xi_nr]==x:
   #       return False
   # for xj_nr in Xj_nrs:
   #    if assignment[xj_nr]!=-1 and assignment[xj_nr]==y:
   #       return False
   if x==y:
         return False
   return True

def Revise_Mac(Xi,Xj,Di,Dj,assignment,inpHoris,inpVerts):         # revise returns true iff domain is changed. else false
   revised=False
   Di_Copy=set()
   for val in Di:
      Di_Copy.add(val)
   for x in Di_Copy:
      flag=True
      for y in Dj:
         if isThisOk(Xi,x,Xj,y,assignment,inpHoris,inpVerts):
            flag=False
            break
      if flag:
         Di.remove(x)
         revised=True
   return revised,Di


def mac(unassignedVar,assignment,rowNeighbours,colNeighbours,Domain,DomainUi,nCols):      # maintain arc consistency
   global ConstraintMatrix
   arc=[]
   macreturn=True
   
   Xi = unassignedVar[0]*nCols + unassignedVar[1]
   # print("Xi=",Xi)
   for i in range(len(ConstraintMatrix)):
      if ConstraintMatrix[i][Xi]==1:
         arc.append(((Xi,i),'x'))
   
   # print("inside mac - arc=",arc)
   # print("Domain=",Domain)
   # print("DomainUi=",DomainUi)
   # macreturn=AC3_Mac(arc,Domain,inpHoris,inpVerts,assignment)
   macreturn,Domain,DomainUi=AC3(arc,Domain,DomainUi,nCols)
   # print("macreturn=",macreturn)
   # print("Domain after ac3=",Domain)
   # print("DomainUi after ac3=",DomainUi)
   
   return macreturn,Domain,DomainUi

nBackTrack=0

def backTrack(assignment,Domain,DomainUi,inpHoris,inpVerts,nRows,nCols,isMac):      #function that implements backtracking search
   global nBackTrack,ConstraintMatrix
   nBackTrack+=1

   unassignedVar=(-1,-1)
   for p in assignment:
      if assignment[p]==-1:
         unassignedVar=p
         break
   else:
      return assignment

   # print("unassignedVar=",unassignedVar)
   # print("Domain[unassignedVar]=",Domain[unassignedVar])

   dom_una_cpy=set()
   for valu in Domain[unassignedVar]:
      dom_una_cpy.add(valu)
   for val in dom_una_cpy:
      # print(" val=",val)
      numConf,rowNeighbours,colNeighbours = numofConflics(unassignedVar, val, inpHoris,inpVerts,nRows,nCols,assignment)
      # print("numConf=",numConf)
      if numConf==0:
         # assignmentCopy=copy.deepcopy(assignment)
         assignment[unassignedVar]=val
         if not isMac:
            result=backTrack(assignment,Domain,DomainUi,inpHoris,inpVerts,nRows,nCols,isMac)
            if result is not None:
               return result
         else:
            # print("mac part called")
            nCol=len(inpHoris[0])
            DomainCopy=dict(Domain)
            DomainUiCopy=DomainUi[:]
            macreturn,Domain,DomainUi=mac(unassignedVar,assignment,rowNeighbours,colNeighbours,Domain,DomainUi,nCol)
            if macreturn:
               result=backTrack(assignment,Domain,DomainUi,inpHoris,inpVerts,nRows,nCols,isMac)
               if result is not None:
                  return result
            # else:
               # print("mac ret False")
            Domain=dict(DomainCopy)
            DomainUi=DomainUiCopy[:]
         assignment[unassignedVar]=-1
         # assignment=copy.deepcopy(assignmentCopy)
   return None

#############

def main(argv):
   global inpHoris,inpVerts,ConstraintMatrix,Domain,DomainUi
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except:
      print ("correct usage: python3 kakuro.py -i <inputfile> -o <outputfile>")
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         print ("python3 kakuro.py -i <inputfile> -o <outputfile>")
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   try:
      nRows,nCols=parseInputs(inputfile)              # convert input file format to array format for easy access
   except FileNotFoundError:
      print("Error: File not found\n")
      sys.exit(1)

   getConstraintMatrix(nRows,nCols)    # generate constraint matrix, Domain of X variables, Domain of U variables 


   # print("Print before AC3")
   # print("DomainUi readable=")
   # for dom in DomainUi:
   #    print(dom)

   # print("Domain readable=")
   # for dom in Domain:
   #    print(dom, " : ", Domain[dom])

   allArcs=[]
   for i in range(len(ConstraintMatrix)):
      for j in range(len(ConstraintMatrix[i])):
         if ConstraintMatrix[i][j]==1:
            allArcs.append(((j,i),'x'))

   # print("allArcs=")
   # print(allArcs)

   print("AC-3 begins")
   worked,Domain,DomainUi=AC3(allArcs,Domain,DomainUi,nCols)          # Apply arc consistency
   print("AC-3 ends")

   print("worked=",DomainUi)
   print("DomainUi readable=")
   for dom in DomainUi:
      print(dom)

   print("Domain readable=")
   for dom in Domain:
      print(dom, " : ", Domain[dom])
   assignments = dict()
   #inpHoris,inpVerts,nRows,nCols
   for i in range(nRows):
      for j in range(nCols):
         if(inpHoris[i][j]=='0'):
            assignments[(i,j)]=-1

   ans=backTrack(assignments,Domain,DomainUi,inpHoris,inpVerts,nRows,nCols,True)    # change False to True to run with MAC 
   print ("nBackTrack=",nBackTrack)

   # print("printing to output file = ",outputfile)
   fout=open(outputfile,"w")
   fout.write("rows=")
   fout.write(str(nRows))
   fout.write("\ncolumns=")
   fout.write(str(nCols))
   fout.write("\nHorizontal\n")
   for i in range(len(inpHoris)):
      for j in range(len(inpHoris[0])):
         if inpHoris[i][j] != '0':
            fout.write(inpHoris[i][j])
         else:
            fout.write(str(ans[(i,j)]))
         if j==len(inpHoris[0])-1:
            fout.write("\n")
         else:
            fout.write(",")
   fout.write("Vertical\n")
   for i in range(len(inpVerts)):
      for j in range(len(inpVerts[0])):
         if inpVerts[i][j] != '0':
            fout.write(inpVerts[i][j])
         else:
            fout.write(str(ans[(i,j)]))
         if j==len(inpVerts[0])-1:
            fout.write("\n")
         else:
            fout.write(",")


if __name__ == "__main__":
   main(sys.argv[1:])
