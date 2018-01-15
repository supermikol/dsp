[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

This problem presents a robust example of actual vs biased data. As a data scientist, it will be important to examine not only the data that is available, but also the data that may be missing but highly relevant. You will see how the absence of this relevant data will bias a dataset, its distribution, and ultimately, its statistical interpretation.

Exercise 3.1 Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no chil- dren have no chance to be in the sample.
Use the NSFG respondent variable NUMKDHH to construct the actual distribu- tion for the number of children under 18 in the household.
Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household.
Plot the actual and biased distributions, and compute their means. As a starting place, you can use chap03ex.ipynb.

>> 
```
resp = nsfg.ReadFemResp()
pmf = thinkstats2.Pmf(resp.numkdhh, label='numkdhh')

# Generate Biased Pmf
bias_pmf = pmf.Copy(label='Observed')

for x, p in pmf.Items():
    bias_pmf.Mult(x, x)

bias_pmf.Normalize()

# Plots both 
thinkplot.PrePlot(2)
thinkplot.Hist(pmf, align='left', width=0.45)
thinkplot.Hist(bias_pmf, align='right', width=0.45)
thinkplot.Config(xlabel='Kids per household', ylabel='PMF')

# Prints Means
print(pmf.Mean())
print(bias_pmf.Mean())

```
Actual Mean: 1.02420515504
Biased Mean: 2.40367910066