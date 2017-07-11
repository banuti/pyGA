#!/usr/bin/python
# provides classes for GA
print
print 'pyGA - Daniel Banuti'
print

from random import *

from GAinit import *

import GAmath as calc


class Parameter:
    
    def __init__(self):
        self.name='default'
        self.lo=0.0
        self.hi=0.0



print 'reading parameters'
parameter=[]
nochrom=0
paramfile=open('GAparam.dat', 'r')
param=paramfile.readlines()

for i in range(0,len(param)):
    if param[i][0].isalpha():       #erster char von string param[i]
            parameter.append(Parameter())
            parameter[nochrom].name=param[i].strip()
            parameter[nochrom].lo=float(param[i+1])
            parameter[nochrom].hi=float(param[i+2])
            nochrom+=1
print '%i parameters imported' %nochrom

for i in range(0, len(parameter)):
    print 'Parameter %i: %s [%f, %f]' %(i, parameter[i].name, parameter[i].lo, parameter[i].hi)
print


class Parameters:

    def __init__(self):

        print 'reading parameters'
        self.paralist=[]
        self.nochrom=0
        paramfile=open('GAparam.dat', 'r')
        
        param=paramfile.readlines()

        for i in range(0,len(param)):
            if param[i][0].isalpha():       #erster char von string param[i]
                    paralist.append(Parameter())
                    paralist[nochrom].name=param[i].strip()
                    paralist[nochrom].lo=float(param[i+1])
                    paralist[nochrom].hi=float(param[i+2])
                    nochrom+=1
        print '%i parameters imported' %nochrom


class Entity:
    
    def __init__(self):
        self.chromlen=10          # integer: length of chromosomes
        self.mutprob=0.01   # float (<=1): mutation probability

        self.fit=0.0
        self.genome=[]

        
    def buildGenome(self):
        for i in range(0, (nochrom*self.chromlen)):
            self.genome.append(calc.flip())
        

    def decodeChrom(self, chrom, chromID):
        x=calc.bin_dec(chrom)
        hi=parameter[chromID].hi
        lo=parameter[chromID].lo
        y=(((hi-lo)*x)/((2**self.chromlen-1))+lo)
        return y

    def decodeGenome(self):
        chromID=0
        param={}
        for i in range(0, nochrom):
            chrom=self.genome[chromID*self.chromlen:(chromID+1)*self.chromlen]
            dechrom=self.decodeChrom(chrom, chromID)
            param[ parameter[chromID].name ]= dechrom
            chromID+=1
        return param

    def getFit(self):
        param=self.decodeGenome()

        fitn=F(param)
        
        if fitn<0.0:
            fitn=0
        self.fit=fitn
        
    def fitOut(self):
        return self.fit

    def mutate(self):
        for i in range(0, len(self.genome)):
            if calc.decide(self.mutprob):
                if self.genome[i]==1:
                    self.genome[i]=0
                elif self.genome[i]==0:
                    self.genome[i]=1


  
class Population:
    
    def __init__(self,nopopulation):
        self.crossprob=0.6  # float (<=1): crossover probability
        self.floodfactor=0.85     # float (<=1): fitness scaling with avg

        self.avgFit=0.0
        self.maxFit=0.0
        self.minFit=0.0
        self.sumFit=0.0
        self.bestIndiv=Entity()
        self.bestIndiv.fit=0
        self.maxpop = nopopulation
        
        self.indiv=[]
        for i in range(0,self.maxpop):
            self.indiv.append(Entity())

    def buildFirstPop(self):
        for i in range(0, self.maxpop):
            self.indiv[i].buildGenome()
##            self.indiv[i].getFit()

    def makeTmp(self):
        tmp=[]
        for i in range(0, len(self.indiv)):
            tmp.append(self.indiv[i].fit)
        return tmp

    def getFit(self):
        for i in range(0, self.maxpop):
            self.indiv[i].getFit()
        
    def getAvgFit(self):
        temp=self.makeTmp()
        avg=calc.avg(temp)
        self.avgFit=avg
        
    def avgFitOut(self):
        return self.avgFit

    def getFitSum(self):
        temp=self.makeTmp()
        sum=calc.fitsum(temp)
        self.sumFit=sum

    def fitSumOut(self):
        return self.sumFit
    
    def getMaxFit(self):
        temp=self.makeTmp()
        max=calc.maximum(temp)
        self.maxFit=max
        maxindex=temp.index(max)
        self.bestIndiv=self.indiv[maxindex]

        
    def maxFitOut(self):
        return self.maxFit

    def getMinFit(self):
        temp=self.makeTmp()
        min=calc.minimum(temp)
        self.minFit=min
        
    def minFitOut(self):
        return self.minFit

    def mixPop(self):
        shuffle(self.indiv)
        
    def crossover(self):
            
        gendummy=[]
        for i in range(0, (len(self.indiv)-1), 2):
                if calc.decide(self.crossprob):
                    cross=calc.rangeint(1, len(self.indiv[0].genome)-1)
                else:
                    cross=0
                tmp_l=[]
                tmp_m=[]
                
                l=i
                m=i+1

                tmp_l[:cross]=self.indiv[m].genome[:cross]  
                tmp_l[cross:]=self.indiv[l].genome[cross:]
                tmp_m[:cross]=self.indiv[l].genome[:cross]  
                tmp_m[cross:]=self.indiv[m].genome[cross:]
                gendummy.append(tmp_m)
                gendummy.append(tmp_l)

        for i in range(0, self.maxpop):
            self.indiv[i].genome=gendummy[i]

        
    def selection(self):
        self.getFitSum()
        probs=[]
        for i in range(0, self.maxpop):
            if self.sumFit>0:
                scaledIndivFit=(self.indiv[i].fit-(self.floodfactor*self.avgFit))
                scaledSumFit=(self.sumFit-(self.floodfactor*self.avgFit*self.maxpop))
                if scaledIndivFit<0:
                    scaledSumFit+=abs(scaledIndivFit)
                    scaledIndivFit=0

                reprodProb=scaledIndivFit   #/scaledSumFit)
                probs.append(reprodProb)
            else:
                probs.append(0)
      
        wheel=[]
        index=0
        for i in range(0, self.maxpop):
            wheel.append(0.0)
            if i!=0:
                wheel[i]+=wheel[i-1]
            wheel[i]+=probs[i]

        for i in range(0, len(wheel)):
            wheel[i]=wheel[i]/wheel[self.maxpop-1]

        return wheel


    def mutate(self):
        for i in range(0, self.maxpop):
            self.indiv[i].mutate()
       


            
class World:
    
    def __init__(self,population=1000,generations=100):

        self.maxpop=population         # integer: maximum population
        self.maxgen=generations          # integer: number of generations


        self.gener=[]
        self.worldBest=Entity()
        self.worldBest.fit=0.0
        
        self.chromlen=100        # integer: length of chromosomes
        self.mutprob=0.001       # float (<=1): mutation probability
        self.crossprob=0.8       # float (<=1): crossover probability
        self.floodfactor=0.85    # float (<=1): fitness scaling with avg
        self.vaccbestprob=0.1    # float (<=1): spread best from previous generation
        self.outfile=file('pyGA.log','w')

    def addGener(self):
        self.gener.append(Population(self.maxpop))

    def reproduction(self, gindex):
        wheel=self.gener[gindex].selection()
        for i in range(0, self.maxpop):
            choice=calc.rnd()
            for j in range(0, len(wheel)):
                if choice<wheel[j]:
                    self.gener[gindex+1].indiv[i].fit=self.gener[gindex].indiv[j].fit
                    self.gener[gindex+1].indiv[i].genome=self.gener[gindex].indiv[j].genome
                    break

    def grabBest(self, gindex):
        if self.gener[gindex].bestIndiv.fit>self.worldBest.fit:
            self.worldBest.fit=self.gener[gindex].bestIndiv.fit
            self.worldBest.genome=self.gener[gindex].bestIndiv.genome
            
  
    def makeTmp(self):
        tmp=[]
        for i in range(0, len(self.gener)):
            tmp.append(self.gener[i].maxFit)
        return tmp

        

    def maxFitOut(self):
        return self.maxFit

          
    def runworld(self):


        #header
        self.outfile.write('Gen \t MaxFit \t AvgFit \t')
        for i in range(0, len(parameter)):
            self.outfile.write(' %s \t' %parameter[i].name)
        self.outfile.write('\n')

        for i in range(0, self.maxgen):

            self.addGener()
            if i==0:
                self.gener[0].buildFirstPop()
            else:
                self.reproduction(i-1)
                self.gener[i].mixPop()
                self.gener[i].crossover()
                self.gener[i].mutate()

            self.gener[i].getFit()
            self.gener[i].getMaxFit()
            self.gener[i].getAvgFit()
            avg=self.gener[i].avgFitOut()
            max=self.gener[i].maxFitOut()
            spread=max/avg
            self.grabBest(i)

            self.bestparam=self.gener[i].bestIndiv.decodeGenome()
            print 'Gener %2i:   Avg = %2.4f   Max = %2.4f   Spread = %2.4f' %(i, avg, max, spread)

            if (abs(spread-1.0)<0.0000001): 
                break
            
            
            line=str(i)+' \t '+str(avg)+' \t '+str(max)
            for i in range(0, len(parameter)):
                line+=' \t ' +str( self.bestparam[parameter[i].name] )
            line+='\n'
            self.outfile.write(line)

        line=''
        line+='MaxFit = '+str(self.worldBest.fit)+'\t'
        for i in range(0, len(parameter)):
            line+='\t %s = %f' %(parameter[i].name, self.bestparam[parameter[i].name])
        self.outfile.write(line)


    def showreport(self):

        print
        print 'Number of Generations: %i' %(len(self.gener))
        print
        print 'Best Fitness %f with Parameters: ' %self.worldBest.fit
        for i in range(0, len(parameter)):
            print '%s\t= %f' %(parameter[i].name, self.bestparam[parameter[i].name])
