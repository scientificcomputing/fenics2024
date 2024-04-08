---
title: "Determination of Navier's slip parameter and the inflow velocity using variational data assimilation"
authors:
  - name: Alena Jarolímová
    affiliations:
      - Charles University
    email: jarolimova@karlin.mff.cuni.cz
  - name: Jaroslav Hron
    affiliations:
      - Charles University
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The goal of our work is to develop a reliable model to reconstruct the velocity and pressure of blood in large arteries by using data assimilation techniques on 4D-PC MRI velocity images.
Having a mathematical model of fluid, the purpose of the assimilation is to determine various model parameters which are difficult to determine or measure directly.
While no-slip is the most popular wall boundary condition, there have been observations (Nubar, 1971) indicating that some amount of slip might be a reasonable model for the wall boundary condition in blood flow modelling.
In our recent work (Jarolímová & Hron, 2024), we proposed an optimal control method to estimate a Navier's slip parameter on the wall and the velocity profile at the inlet using a variational assimilation.
We have implemented the method using FEniCS and dolfin-adjoint and tested it for steady flows using artificially generated 3D data and we assessed the robustness of the method with respect to the numerical setting and the amount of noise in the data.
Applying the method to real patient data, we saw that including Navier's slip boundary condition helped to improve the fit of the blood flow patterns present in the magnetic resonance data for steady flows.

# References
A. Jarolímová, J. Hron (2024). Determination of Navier’s slip parameter and the inflow velocity using variational data assimilation. arXiv. doi:10.48550/arXiv.2402.04766

Y. Nubar (1971). Blood Flow, Slip, and Viscometry. Biophysical Journal, 11(3):252–264. doi:10.1016/S0006-3495(71)86212-4
