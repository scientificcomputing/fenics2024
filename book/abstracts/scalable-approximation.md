---
title: 'Scalable approximation and solvers for ionic electrodiffusion in cellular geometries'
authors:
  - name: Pietro Benedusi
    affiliations:
      - USI
    email: benedp@usi.ch
  - name: Ada J. Ellingsrud
    affiliations:
      - Simula
    email:
  - name: Halvor Herlyng
    affiliations:
      - Simula
    email:
  - name: Marie E. Rognes
    affiliations:
      - Simula
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The activity and dynamics of excitable cells are fundamentally regulated and moderated by extracellular and intracellular ion concentrations and their electric potentials. The increasing availability of dense reconstructions of excitable tissue at extreme geometric detail pose a new and clear scientific computing challenge for computational modelling of ion dynamics and transport. In this paper, we design, develop and evaluate a scalable numerical algorithm for solving the time-dependent and nonlinear KNP-EMI equations describing ionic electrodiffusion for excitable cells with an explicit geometric representation of intracellular and extracellular compartments and interior interfaces. We also introduce and specify a set of model scenarios of increasing complexity suitable for benchmarking. Our solution strategy is based on an implicit-explicit discretization and linearization in time, a mixed finite element discretization of ion concentrations and electric potentials in intracellular and extracellular domains, and an algebraic multigrid-based, inexact block-diagonal preconditioner for GMRES. Numerical experiments with up to 10^8 unknowns per time step and up to 256 cores demonstrate that this solution strategy is robust and scalable with respect to the problem size, time discretization and number of cores.
