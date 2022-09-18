class geneticanalysis:
    k = 0
    c = ""
    count_check= 0
    stopcodon = ["TAA","TAG","TGA"]
    def __init__(self,seq):
        self.seq = seq
        self.u =len(self.seq)
        self.count = 0

    def is_valid(self):
        for i in self.seq:
            if (i == "A" or i=="G" or i=="C" or i=="T"):
                pass
            else:
                self.k = 1
                return False

    def is_potentialgene(self):
        if self.is_valid() == False:
            return 0
        else:
            if (self.u)%3 == 0:
                if self.codon(self.u - 3) in self.stopcodon:
                    if self.codon(0) == "ATG":
                        for i in range(3,self.u-5,3):
                            if self.codon(i) not in self.stopcodon:
                                self.count +=1
                                if (self.u-5)//3 == self.count:
                                  return 1
                            else:
                                return 0
                    else:
                     return 0          
                else:
                 return 0                  
            else:
                return 0

    def validdna(self):
      if self.is_valid() == False:
        print(self.seq + " is  invalid sequence") 
      else:
        print(self.seq + " is a valid sequence")  
    
    def codon(self,k):
      self.c =""
      for i in range(k,k+3):
        self.c += self.seq[i]
      return self.c 
       

    def potentialgene(self):
        if self.is_valid() == False:
            print( "{} is a invalid sequence,is not a potential gene".format(self.seq))
            
        else:
            if self.is_potentialgene()!=0:
                print(self.seq + " is a potential gene")
                
            else:
                print(self.seq + " is not a potential gene")
                   


    def aacount(self):
        if self.is_valid()==False:
            print("{} is a invalid sequence,therefore no protiens".format(self.seq))
            
        elif self.is_potentialgene() == 0:
               print("{} is not a potential gene,therefore no protiens".format(self.seq))
               

        if self.is_potentialgene()!= 0:      
            print("{} will produce a protien of length {}".format(self.seq,self.u//3-1))
            
GA = geneticanalysis("ATGGCAAGCTCGACTTGA")
GA.validdna()
GA.potentialgene()
GA.aacount()
