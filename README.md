# MPPKDS--keypairs_analysis

Digital Signature Performance ofa New Quantum Safe Multivariate Polynomial Public Key Algorithm --- Key Generation and Correlation

This part shows the average positive and negative correlations of MPPK/DS key pairs versus modulo values. We aim to find the key pairs with large relu correlation coefficient and use ReLU Neural Network to predict private keys.

## Description

### Key Generation
The key is generated according to paper of A new quantum-safe multivariate polynomial public key digital signature algorithm:
https://www.researchgate.net/publication/362401919_A_new_quantum-safe_multivariate_polynomial_public_key_digital_signature_algorithm

The code is edited on Tommy Zhou’s Python code. https://github.com/t0mmyz/MPPK_keygen

### Semi-covariance coefficients

Unlike the Pearson coefficient, which only provides two directions, the semi-covariance approach provides a four-direction measurement between the target and variables.

Math derivation

Pearson correlation coefficient 

$$ E((X-EX)(Y-EY)) \over\sqrt{E(X^2)-EX^2} \sqrt{E(Y^2)-EY^2} $$

$$ =  E(ReLU((X-EX)(Y-EY))) \over\sqrt{E(X^2)-EX^2} \sqrt{E(Y^2)-EY^2} $$

$$ -  E(ReLU(-(X-EX)(Y-EY))) \over\sqrt{E(X^2)-EX^2} \sqrt{E(Y^2)-EY^2}$$

= Upper correlation coefficient − Down correlation coefficient

Here the basic Rectified Linear Unit: $$ReLU(X) = max(0,X)$$
Reference: https://link.springer.com/content/pdf/10.1007/978-3-031-02097-1_10.pdf

## Executing program

The code contains four parts.

### keygen_real

Generate a public and private key pair based on chosen modulo p.

There are four parameters:\
param m: number of noise vars, currently equals to n (might subject to change)\
param n: the degree of a base polynomial\
param lam: the degree of two univariate polynomials\
param upper_limits: the upper limits in base polynomials

Use quantumrandom project to generate real random numbers:
Install quantumrandom package
   ```sh
   pip install quantumrandom
   ```
https://pypi.org/project/quantumrandom/

### key_list

Generate specified number of key pairs and store them in a .xlsx file.

### split_keys

Rearrange the columns of key pairs to a suitable matrix format.

Corresponding columns:
𝑃, 𝑄 ~ 𝑓,ℎ,𝐸<sub>𝜙</sub>, 𝐸<sub>𝜑</sub>\
𝑁<sub>0</sub>,𝑁<sub>𝑛</sub> ~ 𝑅<sub>0</sub>,𝑅<sub>𝑛</sub>

### semi_corr

Calculate upper and down covariance


