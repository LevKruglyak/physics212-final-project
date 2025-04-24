import matplotlib as mpl
mpl.rcParams["text.usetex"] = True
mpl.rcParams["font.family"] = "serif"
mpl.rcParams["font.serif"] = "Computer Modern Roman"
mpl.rcParams["text.latex.preamble"] = r"""
        \usepackage[T1]{fontenc}
        \usepackage{mlmodern}
"""

from getdist import plots
import matplotlib.pyplot as plt
import numpy as np
from getdist.mcsamples import loadMCSamples
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import csv

plt.rc('font', size=11)
plt.rc('axes', titlesize=11)
plt.rc('axes', labelsize=11)
plt.rc('xtick', labelsize=11)
plt.rc('ytick', labelsize=11)
plt.rc('legend', fontsize=11)
plt.rc('figure', titlesize=11) 

chain_dir = r'/Users/levkruglyak/Documents/Harvard/Physics212/final/chains'

root      = 'CMB'
samplesCMB = loadMCSamples(f"{chain_dir}/CMB")
samplesDESIBBN = loadMCSamples(f"{chain_dir}/DESI+BBN")
samplesDESIBBNthetastar = loadMCSamples(f"{chain_dir}/DESI+BBN+thetastar")

H0   = samplesCMB.getParams().H0
omegam   = samplesCMB.getParams().omegam
h    = H0 / 100.0
C    = np.mean(omegam * h**3)

g = plots.get_single_plotter(width_inch=6.5)
g.plot_2d([samplesDESIBBN, samplesDESIBBNthetastar, samplesCMB],
          ['H0','omegam'], filled=True)
omegam_g = np.linspace(*g.subplots[0][0].get_ylim(), 400)
H0_g     = 100.0*(C/omegam_g)**(1/3)
g.add_line(H0_g, omegam_g, ls='--', lw=1)
g.add_legend([r'DESI+BBN',
              r'DESI+BBN+$\theta_*$',
              r'CMB (Planck 2018 + lensing)',
              r'constant $\Omega_mh^3$ direction'],
             legend_loc='upper right')  

plt.xlabel(r'$H_0\;[\mathrm{km\,s}^{-1}\,\mathrm{Mpc}^{-1}]$')
plt.ylabel(r'$\Omega_\mathrm{m}$')
plt.savefig(fname="figures/H0-omegam")

data = np.loadtxt(f'{chain_dir}/CMB.progress', usecols=(0,3))
x = data[:, 0]
y = data[:, 1]

plt.figure(figsize=(6, 2.5), dpi=100)
plt.yscale('log')
plt.title(r'MCMC $R-1$ for CMB (Planck 2018 + lensing)')
plt.plot(x, y, linestyle='-',linewidth=1, color='blue', label=r'$R-1$')
plt.xlabel('Number of Accepted Samples')
plt.ylabel(r'$R-1$')
plt.axhline(y=0.01, color='gray', linestyle='--', linewidth=1)
plt.tight_layout()
plt.savefig(fname='figures/CMB-R-1.pdf')

root      = 'DE-EOS'
samplesCMB = loadMCSamples(f"{chain_dir}/{root}")
g = plots.get_single_plotter(width_inch=4, ratio=0.75)
g.plot_2d([samplesCMB], ['w', 'wa'], filled=True)
ax = g.subplots[0][0]
ax.set_xlim(-1.0, 0.0)   
ax.set_ylim(-3.0, 0.0)
g.export(fname='figures/DESI-CMB-w-wa')

