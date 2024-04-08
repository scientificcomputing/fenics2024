---
title: 'Nonclassical electromagnetism with FEniCSx'
authors:
  - name: Cristian Ciraci
    affiliations:
      - Istituto Italiano di Tecnologia
    email: cristian.ciraci@iit.it
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The Finite Element Method (FEM) is ubiquitous in computational physics: it is a powerful and versatile method for solving Maxwell's equations, enabling the analysis and design of electromagnetic devices and systems. A key advantage of the FEM is its ability to handle a heterogeneous mesh refinement, allowing for higher accuracy in regions of interest, while keeping the overall computational cost contained. This feature is especially advantageous in nanophotonics. Moreover, the FEM is also very well suited for multi-physics problems, i.e., where electromagnetism is coupled with elasticity, heat transfer, fluid dynamics, etc.
While some commercial options exist (which can be prohibitively expensive and have limited parallelization or scripting options), open-source alternatives are very limited (often offering modules for electro- and magneto-statics only).
Here, we use FEniCSx (https://fenicsproject.org/) to solve a series of multi-physics problms, in which Maxwell's equations are coupled to a hydrodynamic-like equation for the description of nonlcassical plasmonic effects in nanoparticles, in the limit of the Thomas-Fermi approximation [1] and the quantum hydrodynamic theory [2].


# References
[1] C. Ciracì, J. B. Pendry, D. R. Smith, Hydrodynamic Model for Plasmonics: A Macroscopic Approach to a Microscopic Problem. ChemPhysChem 14, 1109–1116 (2013).

[2] C. Ciracì, F. Della Sala, Quantum hydrodynamic theory for plasmonics: Impact of the electron density tail. Physical Review B 93, 205405 (2016).
