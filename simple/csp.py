from queue import Queue

def AC3(csp,allArcs,ConstraintMatrix,Domain,DomainUi,nCols):   # function AC-3(csp) returns false if an inconsistency is found and true otherwise
    q = Queue() 
    for eachArc in allArcs:
        q.put(eachArc)
    while not q.empty:      
        (Xi,Xj),typ=q.get()     # typ will the type (x or u) of Xi
        if typ=='x':
            Xi_x=Xi/nCols
            Xi_y=Xi%nCols
            posInDj=0
            for cmv in range(len(ConstraintMatrix[Xj][:])):
                if cmv==Xi:
                    break
                if ConstraintMatrix[Xj][cmv]==1:
                    posInDj+=1
            revised,Di=REVISEx(csp, Domain[(Xi_x,Xi_y)],DomainUi[Xj], posInDj)
            if revised:
                Domain[(Xi_x,Xi_y)]=Di
                if len(Domain[(Xi_x,Xi_y)])==0:
                    return False
                for Xk in range(len(ConstraintMatrix[:][Xi])):
                    if ConstraintMatrix[Xk][Xi]==0 or Xk==Xj:
                        continue
                    q.put((Xk,Xi),'u')
        elif typ=='u':
            Xj_x=Xj/nCols
            Xj_y=Xj%nCols
            posInDi=0

            for cmv in range(len(ConstraintMatrix[Xi][:])):
                if cmv==Xj:
                    break
                if ConstraintMatrix[Xi][cmv]==1:
                    posInDi+=1

            revised,Di=REVISEu(csp, DomainUi[Xi],Domain[(Xj_x,Xj_y)],posInDi)
            if revised: 
                DomainUi[Xi]=Di
                if len(DomainUi[Xi]):
                    return False
                for Xk in range(len(ConstraintMatrix[Xi][:])):
                    if ConstraintMatrix[Xi][Xk]==0 or Xk==Xj:
                        continue
                    q.put((Xk,Xi),'x')
    return True

def REVISEx(csp, Di,Dj,posInDj):     #returns true iff we revise the domain of Xi revised ← false
    revised=False
    for x in Di:
        # if """no value y in Dj allows (x ,y) to satisfy the constraint between Xi and Xj then""":
        #     """delete x from Di"""
        #     revised=True
        found=False
        for y in Dj:
            if y[posInDj]==x:
                found=True
                break
        if not found:
            Di.remove(x)
            revised=True
    return revised,Di

def REVISEu(csp, Di,Dj,posInDi):     #returns true iff we revise the domain of Xi revised ← false
    revised=False
    for x in Di:
        # if """no value y in Dj allows (x ,y) to satisfy the constraint between Xi and Xj then""":
        #     """delete x from Di"""
        #     revised=True
        found=False
        for y in Dj:
            if y==x[posInDi]:
                found=True
                break
        if not found:
            Di.remove(x)
            revised=True
    return revised,Di

