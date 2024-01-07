# Statistical methods of finding outliers

## Definition of outliers
One of the steps in data cleaning is finding outliers.

**Outlier (anomaly)** - is a case in data, that significantly outstands from major ditstribution and differs from other cases greatly.

In this project foolowing methods of finding outliers are used:

* Interquartile interval method

* Z-deviation method (sigma method)

## Interquartile interval method:
![](../images/boxplot.png)

### Method algorythm

1. Calculate 25th and 75th quantile - $Q_{25}$ and $Q_{75}$ for needed feature
2. Calculate interquartile interval 
   * $IQR = Q_{75} - Q_{25}$
3. Define upper and lower boundariess of research:
   * $upper = Q_{75} + 1.5IQR$
   * $lower = Q_{25} - 1.5IQR$
4. Find cases outlying from research boundaries

### **Method minuses:** 

Method demands researched subject to be normally dispersed.


### **Method modifications:**
We tried to use modifying data (logarythmic transformation) to make data normally (or at least symmetrically) dispersed.
Also we made amount of interquartile intervals variable from left and right boundaries.


## Z-deviation method:
![](../images/method_sigm.png)

### Method algorythm:

1. Find mean and standard deviation $\mu$ and $\sigma$ for researched feature.
2. Calculate upper and lower boudaries:
   * $upper = \mu + 3 * \sigma$
   * $lower = \mu - 3 * \sigma$
3. Find oulying cases

### **Method minuses:**
As the IQR method, this one demands data to be normally dispersed.

### **Method modifications:**
We added same options - logarythmic transformation and choice of number of intervals.

## Methods realisation:
Methods are realised as functions outliers_iqr_mod() and outliers_z_score_mod(). Both of them are located in file outliers.py and have documentation.


