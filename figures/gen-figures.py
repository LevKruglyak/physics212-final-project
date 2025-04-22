# --- 0.  Select the PGF backend *before* importing pyplot ------------
import matplotlib as mpl
mpl.use("pgf")
mpl.rcParams.update({
    "text.usetex": True,
    "font.size":        11,
    "font.family": "serif",
    "text.latex.preamble": r"""
        \usepackage[T1]{fontenc}
        \usepackage{mlmodern}
    """,
})

from getdist import plots
import matplotlib.pyplot as plt
import numpy as np
from getdist.mcsamples import loadMCSamples

chain_dir = r'/Users/levkruglyak/Documents/Harvard/Physics212/final/chains'
root      = 'CMB'

samples = loadMCSamples(f"{chain_dir}/{root}")
H0   = samples.getParams().H0
omegam   = samples.getParams().omegam
h    = H0 / 100.0
C    = np.mean(omegam * h**3)

g = plots.get_single_plotter(width_inch=4, ratio=0.75)
g.plot_2d([samples], ['H0', 'omegam'], filled=True)   

ax = g.subplots[0][0]
omegam_g = np.linspace(*ax.get_ylim(), 400)     
H0_g = 100.0*(C/omegam_g)**(1/3)
ax.plot(H0_g, omegam_g, ls='--', lw=1, color='gray')
g.export(fname="figures/CMB-H0-omegam")

from getdist.types import ResultTable
print(ResultTable(ncol=1,results=[samples], paramList=['H0', 'omegam'], limit=1, titles=['CBM (Planck)']).tableTex())
