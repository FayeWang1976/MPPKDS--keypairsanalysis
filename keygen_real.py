#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 21:26:26 2023

@author: wangzhehan
"""

import quantumrandom
import numpy as np
import random

def safe_prime():
    """
    Generate a random safe prime p which satifies p = 2^xq + 1, where q is also a prime
    :return: p
    """
    # First 3-10 safe primes for demo only, real key-gen should be using much larger primes
    prime_list_temp = [11, 23, 47, 59, 83, 107, 167, 179]
    # Use *** as current choice
    return random.choice(prime_list_temp)
    # return random.choice(prime_list_temp)


def keygen(m, n, lam, upper_limits):
    """
    Use the MPPKDS algorithm to generate public and private key pairs
    :param m: number of noise vars, currently equals to n (might subject to change)
    :param n: the degree of a base polynomial
    :param lam: the degree of two univariate polynomials
    :param upper_limits: the upper limits in base polynomials
    :return: two dicts: private key and public key
    """

    # Select random
    safe_p = safe_prime()
    phi_p = safe_p - 1

    # Calculate the overall upper limit for base poly
    tuple_limit = 1
    for i in upper_limits:
        tuple_limit *= i + 1

    # Base polynomial
    coeff = []
    for i in range(0, (n+1)*tuple_limit):
        a = quantumrandom.randint(0, phi_p-1)
        coeff.append(int(a))
    beta = np.array(np.array_split(coeff, n+1))
    print(beta)
    # Univariate polynomials
    f = []
    h = []
    for i in range(0, lam+1):
        b1 = quantumrandom.randint(0, phi_p-1)
        b2 = quantumrandom.randint(0, phi_p-1)
        f.append(int(b1))
        h.append(int(b2))
    f = np.array(f)
    h = np.array(h)

    # phi and psi
    phi = np.zeros((n + lam + 1, tuple_limit))
    psi = np.zeros((n + lam + 1, tuple_limit))

    for i in range(n + 1):
        for j in range(lam + 1):
            noise_f = np.multiply(beta[i, :], f[j])
            noise_h = np.multiply(beta[i, :], h[j])
            phi[i + j, :] = np.add(phi[i + j, :], noise_f)
            psi[i + j, :] = np.add(psi[i + j, :], noise_h)

    phi = np.remainder(phi, phi_p)
    psi = np.remainder(psi, phi_p)

    # E_phi and E_psi value
    e_phi = []
    e_psi = []
    for i in range(0, n + lam - 1):
        c1 = quantumrandom.randint(0, phi_p - 1)
        c2 = quantumrandom.randint(0, phi_p - 1)
        e_phi.append(int(c1))
        e_psi.append(int(c2))
    e_phi = np.array(e_phi)
    e_psi = np.array(e_psi)

    # R_0 and R_n value
    r_0 = int(quantumrandom.randint(0, (phi_p - 2) / 2)) * 2
    r_n = int(quantumrandom.randint(0, (phi_p - 2) / 2)) * 2

    # Generate noise
    noise_0 = np.remainder(np.multiply(beta[0, :], r_0), phi_p)
    noise_n = np.remainder(np.multiply(beta[n, :], r_n), phi_p)

    # Upper phi and Upper psi
    upper_phi = phi[1:n + lam, :]
    upper_psi = psi[1:n + lam, :]

    # P and Q generation
    p = np.zeros((n + lam - 1, tuple_limit))
    q = np.zeros((n + lam - 1, tuple_limit))
    for i in range(n + lam - 1):
        p[i, :] = np.multiply(np.concatenate(
            (upper_phi[i, 0] - e_phi[i], upper_phi[i, 1:]), axis=None), r_0)
        q[i, :] = np.multiply(np.concatenate(
            (upper_psi[i, 0] - e_psi[i], upper_psi[i, 1:]), axis=None), r_n)
    p = np.remainder(p, phi_p)
    q = np.remainder(q, phi_p)

    private_key = {
        "f": f,
        "h": h,
        "R_0": r_0,
        "R_n": r_n,
        "E_phi": e_phi,
        "E_psi": e_psi,
    }
    public_key = {
        "P": p,
        "Q": q,
        "N_0": noise_0,
        "N_n": noise_n,
    }

    return private_key, public_key


if __name__ == '__main__':
    m = 2
    n = 2
    lam = 1
    upper_limits = [1, 1]

    s, v = keygen(m, n, lam, upper_limits)
    print("private key", s)
    print("public key", v)
