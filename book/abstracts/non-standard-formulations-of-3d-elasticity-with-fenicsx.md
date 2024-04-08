---
title: 'Non-standard formulations of 3D elasticity with FEniCSx'
authors:
  - name: Andreas Zilian
    affiliations:
      - University of Luxembourg
    email: andreas.zilian@uni.lu
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

In addition to the well-known classical displacement-based and mixed displacement-stress formulations of 3D elasticity a number of non-standard formulations can be derived.
We will discuss and compare (a) the tangential-displacement normal-normal-stress (TDNNS) form [1], (b) a novel stress-only formulation [2], and (c) a spectral formulation using principal strain and stress quantities [3] including their respective requirements on boundary conditions as well as implementation aspects with FEniCSx. Numerical examples and demos based on the extension package `dolfiny` are presented.

# References
[1] Pechstein, A & Schöberl, J. Tangential-displacement and normal-normal-stress continuous mixed finite elements for elasticity. Math. Models Methods Appl. Sci. 2011;21(8):1761–1782. doi:10.1142/S0218202511005568

[2] Sky, A & Zilian, A. Symmetric unisolvent equations for linear elasticity purely in stresses. 2024. doi:10.48550/arXiv.2402.00480

[3] Simo, JC & Taylor, RL, Quasi-incompressible finite elasticity in principal stretches. Continuum basis and numerical algorithms, Computer Methods in Applied Mechanics and Engineering, 85(3), 1991. doi:10.1016/0045-7825(91)90100-K
