---
title: 'Property-preserving numerical approximation of a degenerate multiphase fluid flow model with variable densities'
authors:
  - name: Daniel Acosta Soba
    affiliations:
      - Universidad de Cádiz (Spain)
    email: daniel.acosta@uca.es
  - name: Francisco Guillén González
    affiliations:
      - Universidad de Sevilla (Spain)
    email:
  - name: J. Rafael Rodríguez Galván
    affiliations:
      - Universidad de Cádiz (Spain)
    email:
  - name: Jin Wang
    affiliations:
      - University of Tennessee at Chattanooga (USA)
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The aim of this talk is to present a well-suited approximation of a phase-field model of the mixture of two fluids with variable densities [1]. This model couples a Cahn-Hilliard equation with degenerate mobility, whose phases represent each of the mixing fluids, with a Navier-Stokes equation by means of several external forces and convection terms. We develop a numerical approximation of the continuous model based on an stabilized upwind discontinuous Galerkin (DG) method that preserves the incompressibility of the velocity of the fluid in a local sense. The resulting discrete scheme is mass-conservative, pointwise-bounded and energy-stable. Finally, we implement this approximation using FEniCSx to carry out several numerical experiments whose results are in accordance with the theoretical analysis.

# References
[1] Acosta-Soba, D., Guillén-González, F., Rodríguez-Galván, J. R., & Wang, J. (2023). Property-preserving numerical approximations of a Cahn-Hilliard-Navier-Stokes model with variable densities and degenerate mobility. arXiv preprint. doi:10.48550/arXiv.2310.01522.
