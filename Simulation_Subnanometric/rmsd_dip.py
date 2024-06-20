import numpy as np

class rmsd:
    def __init__(self,coordinates,selection,start=None,step=None,save='Y',num=None):

        coordinates = coordinates.coordinates
   
        RMSD = []
        Time = []
        self.rmsd = []

        if start==None:
            start = 0

        if step == None:
            step = 1

        if num==None:
            num = 1

        if save=='Y':
            open_file = open("RDF_%d.csv"%num,"w")

        for i in range(len(coordinates)):  

            midRMSD = [0,0,0]
            for j in selection:
                midRMSD[0] += (coordinates[i][j][1] - coordinates[0][j][1])**2
                midRMSD[1] += (coordinates[i][j][2] - coordinates[0][j][2])**2
                midRMSD[2] += (coordinates[i][j][3] - coordinates[0][j][3])**2
            midRMSD = np.sqrt(np.sum(np.array(midRMSD))/len(selection))

            if save=='Y':
                print(i*step+start,midRMSD,file=open_file)

            RMSD.append(midRMSD)
            Time.append(i*step + start)
        if save=='Y':
            open_file.close()

        self.rmsd = [Time,RMSD]

class plotRMSD:
    def __init__(self,value,value2,labels=None,unit=None,location=None,width=None,height=None,thickness=None,fontsize=None,padding=None):
        import matplotlib
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
        from matplotlib.offsetbox import AnchoredText
        from matplotlib.pyplot import figure

        X = []
        Y = []
        Y2 = []
     

        for i in range(len(value)):
            X.append((value[i].rmsd)[0])
            Y.append((value[i].rmsd)[1])
        for i in range(len(value2)):
            Y2.append((value2[i].rmsd)[1])

        Y1 = []
   

        for i in range(len(Y)):
            for j in range(len(Y[i])):
                Y[i][j] = np.abs(Y[i][j] - Y2[0][j])

        if width==None:
            width=1920
        if height==None:
            height=1440

        if thickness==None:
            thickness = 6
        if fontsize==None:
            fontsize=58
        if padding==None:
            padding=28

        if unit==None:
            unit="ps"

        width = int(width/80)
        height = int(height/80)

        fig = plt.figure()
        fig.set_size_inches(width,height)
        ax1 = fig.add_subplot(111)
        if labels==None:
            for i in range(len(X)):
                plt.plot(X[i],Y[i],lw=thickness,label="%d"%(i+1))
        else:
            for i in range(len(X)):
                plt.plot(X[i],Y[i],lw=thickness,label=labels[i])

        #plt.ylim([-0.2, 6])

        #plt.axvline(x=35,ls=':',lw=10,color="black")
        #plt.axvline(x=0,ls=':',lw=10,color="black")
        #plt.axvline(x=62,ls=':',lw=10,color="black")

        plt.xlabel("Time (%s)"%unit,fontsize=fontsize,labelpad=padding)
        plt.ylabel("RMSD (Å)",fontsize=fontsize,labelpad=padding)

        plt.xticks(fontsize=50)
        plt.yticks(fontsize=50)

        ax1.tick_params(width=3*thickness,length=10)
        for axis in ['top','bottom','left','right']:
            ax1.spines[axis].set_linewidth(int(1.7*thickness))
        ax1.tick_params(axis='both', which='major', pad=int(padding/1.33))
        
        fig.savefig('RMSD.png', dpi=100, bbox_inches='tight')

        plt.show()

                    

            

            

                            
    
    
