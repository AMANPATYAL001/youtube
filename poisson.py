import math
import numpy as np
import matplotlib.pyplot as plt

class PoissonGraphs:
    def __init__(self) -> None:
        pass

    def poisson_func(self,u,x):
        return round((u**x)*(math.e**(-u))/math.factorial(x),4)

    def diff_mean_graphs(self):
        x,prob5,prob10,prob15,prob50=[],[],[],[],[]

        ''' list x is the no. of events(and also the x-axis)
         prob5,prob10,prob15,prob50,prob90 - poisson dist. value with mean=5,10,15,50,90 '''

        plt.clf()

        for i in range(65):
            x.append(i)
            
            prob5.append(self.poisson_func(5,i))
            prob10.append(self.poisson_func(10,i))
            prob15.append(self.poisson_func(15,i))
            prob50.append(self.poisson_func(50,i))
            
        
            plt.plot(x,prob5)
            plt.plot(x,prob10)
            plt.plot(x,prob15)
            plt.plot(x,prob50)
            plt.bar(x,prob50,color='violet')

            plt.title('Graphs with different mean values ( lambda )')

            plt.axline((5, 0), (5, 0.18), linewidth=1, color='limegreen',linestyle='--')
            plt.axline((10, 0), (10, 0.18), linewidth=1, color='limegreen',linestyle='--')
            plt.axline((15, 0), (15, 0.18), linewidth=1, color='limegreen',linestyle='--')
            plt.axline((50, 0), (50, 0.18), linewidth=1, color='limegreen',linestyle='--')
            
            plt.xticks(list(range(0,70,5)))
            plt.pause(0.001)

        plt.show()

    def pmf_and_cdf(self):
        for j in list(range(10,25,5))[::-1]:      # j = the mean value
            x,probx,probCdf=[],[],[]  
            
            ''' list probx are poisson values at corresponding x values
                list probCdf are cummulative values at coreesponding x values '''      

            plt.clf()
            for i in range(40):
                x.append(i)
                probx.append(self.poisson_func(j,i))
                probCdf.append(sum(probx))
                plt.title('Poisson Distribution mean at '+str(j))
                
                
                plt.subplot(2, 1, 1)
                plt.bar(x,probx,color='pink')
                plt.plot(x,probx,color='red')
                plt.axline((j, 0), (j,0.10), linewidth=2, color='limegreen',linestyle='--')
                plt.xticks(list(range(0,40)))
                
                plt.title('P(x=0)+P(x=1)+P(x=2)+P(x=3)+P(x=4)+P(x=5)+P(x=6)+P(x=7)+P(x=8) = P(x<=8) {for almost case }\n\nP(x=8)+P(x=9)+P(x=10)+P(x=11)+P(x=12)+P(x=13)+P(x=14)+ ..... = P(x>=8) {for atleast case }\n\n Distribution function of X, is the probability that X will take a value less than or equal to x')
                plt.subplot(2, 1, 2)
                plt.plot(x,probCdf,color='blue')
                plt.bar(x,probCdf,color='darkorange')
                plt.plot(x,probx,color='red')
                plt.axline((j, 0), (j, 1), linewidth=2, color='limegreen',linestyle='--')

                plt.xticks(list(range(0,40)))      
                plt.pause(0.001)
            
        plt.show()

obj=PoissonGraphs()
# obj.diff_mean_graphs()
# obj.pmf_and_cdf()
import argparse

parser = argparse.ArgumentParser(description='Poisson Dist. Graphs')
FUNCTION_MAP = {'dmg' : obj.diff_mean_graphs,
                'pac' : obj.pmf_and_cdf }

parser.add_argument('command', choices=FUNCTION_MAP.keys())

args = parser.parse_args()

func = FUNCTION_MAP[args.command]
func()