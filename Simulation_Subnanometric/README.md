# Calculating the RMSD

Here we will be calculating the RMSD of the Cu atoms from one of the Cu clusters, but have the RMSD of the graphene sheet deducted from the Cu5 clusters, to account for the graphene sheet moving as well.

INSIDE PYTHON
```
from read import openStruct

#Here we read in our structure file
structure = openStruct("CU_AIMD-MD.TRAJ-pos-1.xyz")

from rmsd_dip import rmsd, plotRMSD

#Here we calculate the RMSD of the graphene sheet and individial atoms. We are starting from 0 ps, and using a time step of 0.02 ps.
val1 = rmsd(structure, range(120), 0, 0.02)
val2 = rmsd(structure, [120], 0, 0.02)
val3 = rmsd(structure, [121], 0, 0.02)
val4 = rmsd(structure, [122], 0, 0.02)
val5 = rmsd(structure, [123], 0, 0.02)
val6 = rmsd(structure, [124], 0, 0.02)

#Finally, we plot the RMSD of the Cu atoms
plotRMSD([val2, val3, val4, val5, val6], [val1], ["Cu1", "Cu2", "Cu3", "Cu4", "Cu5"], "ps")

```

# Calculating the Average Minimum Cu-C Distance

Here we will be calculating the average minimum Cu-C distance, for all Cu atoms, so we can see how at its minimum, the Cu atoms are moving closer or further apart from the graphene sheet.

INSIDE PYTHON
```
from read import openStruct

#Here we read in our structure file
structure = openStruct("CU_AIMD-MD.TRAJ-pos-1.xyz")

from distanceanalysis import minDist
from distanceanalysis import plotaveDist

#Here we calculate the minimum C-Cu distances, and averaging it over all Cu atoms
X = minDist(structure,range(120),range(120,130))

#Here we plot the average minimum C-Cu distance, starting from frame 0 ps and going in time steps of 0.02 ps
plotaveDist(X,0,0.02,"ps")
```
