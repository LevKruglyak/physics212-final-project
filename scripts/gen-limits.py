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

samplesCMB = loadMCSamples(f"{chain_dir}/CMB")
samplesDESIBBN = loadMCSamples(f"{chain_dir}/DESI+BBN")
samplesDESIBBNthetastar = loadMCSamples(f"{chain_dir}/DESI+BBN+thetastar")
samplesDESIBBNCMB = loadMCSamples(f"{chain_dir}/DESI+BBN+CMB")
samplesDESIBBNCMBprior = loadMCSamples(f"{chain_dir}/DESI+BBN+CMB-prior")

print(ResultTable(ncol=1,results=[samplesCMB, samplesDESIBBN, samplesDESIBBNthetastar, samplesDESIBBNCMB, samplesDESIBBNCMBprior],
                 paramList=['omegam','H0'], limit=1, titles=['CMB','DESI+BBN', r'DESI+BBN+\theta_*', "DESI+BBN+CMB", r'DESI+BBN+CMB (prior)']).tableTex())
