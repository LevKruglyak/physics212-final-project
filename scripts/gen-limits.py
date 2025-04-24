import numpy as np
from getdist.mcsamples import loadMCSamples
from getdist.types import ResultTable

chain_dir = r'/Users/levkruglyak/Documents/Harvard/Physics212/final/chains'
root      = 'CMB'
samples = loadMCSamples(f"{chain_dir}/{root}")

pars = ["thetastar", "ombh2", "omch2"]
means = np.array([samples.mean(p) for p in pars])
print("means =", means)
cov = samples.cov(pars)
print("covariance =\n", cov)
