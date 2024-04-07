---
title: 'Equilibration-based a-posteriori error estimators within the FEniCSx finite element framework'
authors:
  - name: Maximilian Brodbeck
    affiliations:
      - University of Stuttgart
    email: maximilian.brodbeck@isd.uni-stuttgart.de
  - name: Fleurianne Bertrand
    affiliations:
      - University of Technology Chemnitz
    email:
  - name: Tim Ricken
    affiliations:
      - University of Stuttgart
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Numerical solutions of, e.g. poro-elasticity or heat-conduction suffer from the deterioration of the overall accuracy when re-entrant corners, internal respective boundary layers or shock-like fronts are present (Verführth, 1994). A-posteriori error estimates offers a systematic way of retaining accuracy by localised mesh refinements. Following the seminal idea of Prager and Synge (1947), such error estimates can be constructed based on the comparison of discontinuous fluxes, calculated from the approximation, and any H(div) conforming function, satisfying the equilibrium condition. This function is typically called the equilibrated flux.

In order to retain computational efficiency, the equilibrated flux is calculated locally. Focusing on conforming finite-element-discretisation, this requires the solution of constrained minimization problems on local patches (Ern & Vohralik, 2015). The computational efficiency can be increased by splitting the equilibration into an explicit step followed by an unconstrained minimisation on a modified H(div) space with patch-wise support (Bertrand et al., 2023).

Within this contribution, we discuss efficient implementations of different equilibration procedures within the finite element framework FEniCSx. Special attention will be paid to requirements resulting from the application of equilibration based error estimation in poro-elasticity.

# References
Verfürth, R. (1994). A posteriori error estimation and adaptive mesh-refinement techniques. J. Comput. Appl. Math., 50, p. 67-83. https://doi.org/10.1016/0377-0427(94)90290-9



Prager, W. & Synge, J. L. (1947). Approximations in elasticity based on the concept of function space. Quart. Appl. Math., 5, p. 241–269. Retrieved from https://www.jstor.org/stable/43633616



Ern, A. & Vohralik, M. (2015). Polynomial-Degree-Robust A Posteriori Estimates in a Unified Setting for Conforming, Nonconforming, Discontinuous Galerkin, and Mixed Discretizations. SIAM J. Numer. Anal., 53 , p. 1058-1081. https://doi.org/10.1137/130950100



Bertrand, F., Carstensen, C., Gräßle, B. & Tran, N. T. (2023). Stabilization-free HHO a posteriori error control. Numer. Math., 154, p. 369–408. https://doi.org/10.1007/s00211-023-01366-8
