# MPPKDS--keypairs_analysis

Digital Signature Performance ofa New Quantum Safe Multivariate Polynomial Public Key Algorithm --- Key Generation and Correlation

This part shows the average positive and negative correlations of MPPK/DS key pairs versus modulo values. We aim to find the key pairs with large relu correlation coefficient and use ReLU Neural Network to predict private keys.

## Description

### Key Generation
The key is generated according to paper of A new quantum-safe multivariate polynomial public key digital signature algorithm:
https://www.researchgate.net/publication/362401919_A_new_quantum-safe_multivariate_polynomial_public_key_digital_signature_algorithm

The code is edited on Tommy Zhou’s Python code.

### Semi-covariance coefficients

Unlike the Pearson coefficient, which only provides two directions, the semi-covariance approach provides a four-direction measurement between the target and variables.

Math derivation

Person correlation coefficient 

$$ E((X-EX)(Y-EY)) \over\sqrt{E(X^2)-EX^2} \sqrt{E(Y^2)-EY^2} $$
$$ = E(ReLU((X-EX)(Y-EY))) \over\sqrt{E(X^2)-EX^2} \sqrt{E(Y^2)-EY^2} $$
$$- E(ReLU(-(X-EX)(Y-EY))) \over\sqrt{E(X^2)-EX^2} \sqrt{E(Y^2)-EY^2}$$

### Twin primes


## Getting Started

The code contains three parts.

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)
