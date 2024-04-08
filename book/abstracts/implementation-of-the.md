---
title: 'Implementation of the k-epsilon turbulence model in FEniCS'
authors:
  - name: Juraj Marcibál
    affiliations:
      - University of Southern Denmark
    email: juraj.marcibal@gmail.com
  - name: Hans Joachim Schroll
    affiliations:
      - University of Southern Denmark
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

This poster outlines our approach to implementing the k-epsilon turbulence model within the FEniCS framework. Being frequently used in computational fluid dynamics for its ability to simulate turbulent flows, the k-epsilon model strikes a balance between computational efficiency and accuracy across a wide range of flow scenarios.

In turbulence modeling, our focus often lies on mean flow quantities—such as mean velocity and pressure—rather than instantaneous flow characteristics. This is where the Reynolds-averaged Navier-Stokes (RANS) equations come into play. However, the RANS equations are not closed; they require additional modeling for closure. The k-epsilon model addresses this by supplementing the RANS equations with two additional equations governing turbulent kinetic energy (k) and its dissipation rate (epsilon). Together, these equations form a closed system that describes the mean behaviour of turbulent flows.

The coupling between the RANS equations and the k-epsilon equations introduces complexity, further compounded by the highly non-linear nature of both the k and the epsilon equations. Our poster addresses the challenges of decoupling and linearizing these equations, followed by their seamless integration into the FEniCS computational environment.

Furthermore, our poster underscores FEniCS as a robust tool for turbulence modeling. We present findings from diverse fluid flow scenarios, comparing our simulations against empirical data or direct numerical simulations.
