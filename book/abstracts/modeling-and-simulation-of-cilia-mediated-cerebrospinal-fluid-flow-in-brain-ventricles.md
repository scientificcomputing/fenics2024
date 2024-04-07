---
title: 'Modeling and Simulation of Cilia-Mediated Cerebrospinal Fluid Flow in Brain Ventricles'
authors:
  - name: Halvor Herlyng
    affiliations:
      - Simula Research Laboratory
    email: hherlyng@simula.no
  - name: Ada J. Ellingsrud
    affiliations:
      - Simula Research Laboratory
    email:
  - name: Marie E. Rognes
    affiliations:
      - Simula Research Laboratory
    email:
  - name: Nathalie Jurisch-Yaksi
    affiliations:
      - Norwegian University of Science and Technology
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Flow of cerebrospinal fluid in zebrafish brain ventricles is studied in this work. Motivated by experimental observations, we consider motile cilia and cardiac beating as the driving flow mechanisms. A mathematical model of the flow is developed and coupled with a transport model, to study flow patterns and the transport of molecules of interest inside brain ventricles.

The Stokes equations are used to model the flow, with the motile cilia acting as a force on the fluid through a stress boundary condition that allows the fluid to slip at the wall. Transport is modeled with an advection-diffusion equation coupled to the velocity field obtained from solving the Stokes equations. The flow and transport models are discretized with finite element methods. For the Stokes equations, we consider a divergence-conforming discretization based on Brezzi-Douglas-Marini and Discontinuous Galerkin elements. The advection-diffusion equation is discretized with Discontinuous Galerkin elements.

We implement and solve the discretized equations numerically to simulate flow and transport in a zebrafish brain ventricles geometry obtained with medical imaging. The numerical results are compared with experimental data on flow and transport, indicating that the model developed here is able to reproduce physical phenomena observed in experiments.
