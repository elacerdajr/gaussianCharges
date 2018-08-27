# gaussianCharges

## Description

Script to read the atomic charges in an o Gaussian 09 output file.


## Usage:     

```console
e_getQ.py gaussian.log -option
```

- Options:   npa,chelpg,mulliken,all
- Example:   e_getQ.py gaussian.log -all


## Typical output


For a 2-Me-pyrrole:

<pre>
===== MULLIKEN CHARGES <=====
#n    atom         charge
------------------------------
1     C         -0.064463
2     C         -0.062257
3     C         -0.029086
4     C          0.029534
5     N         -0.053742
6     H          0.101725
7     H         -0.048752
8     H         -0.005402
9     C          0.057707
10    H         -0.037267
11    H          0.033054
12    H          0.039473
13    H          0.039475
==============================
</pre>
