---
title: 'GPU Acceleration in FEniCSx Demonstrated on the Shallow Water Equations '
authors:
  - name: Benjamin Pachev
    affiliations:
      - The University of Texas at Austin
    email: benjaminpachev@utexas.edu
  - name: James Trotter
    affiliations:
      - Simula Research Laboratory
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Graphics cards, or graphical processing units (GPUs) offer the promise of massive speedups compared to traditional CPUs. This potential has been realized in fields such as artificial intelligence and blockchain technology. However, despite a significant body of research into GPU-accelerated finite element methods, they have yet to be widely adopted among finite element practitioners. This is driven in part by the difficulty of modifying existing codes - many of which predate the development of graphics cards - for GPU acceleration. A promising solution is offered by the addition of GPU support to general purpose finite element frameworks such as MFEM, deal.II, and libCEED. This approach mirrors that of machine learning applications, which are developed using a relatively small number of centralized frameworks. This shifts the burden of low-level GPU programming from the application users to library developers, and has enabled the universal adoption of graphics cards in machine learning.

The aim of this work is to bring GPU acceleration to FEniCSx. We have built on previous proof-of-concept work that enabled GPU acceleration of matrix assembly within FEniCSx for a subset of the UFL language in C++ (1). The current work supports the full range of the UFL language, is up-to-date with the most recent version of FEniCSx, and can be used in Python with a simple API. We demonstrate the flexibility and performance of our GPU extension FEniCSx on a suite of test-cases for the shallow water equations. These require the solution of a time-evolving, nonlinear PDE, and include real-world use cases such as hurricane forecasting and a dam failure.

# References
1. Trotter, J. D., Langguth, J., & Cai, X. (2023). Targeting performance and user-friendliness: GPU-accelerated finite element computation with automated code generation in FEniCS. Parallel Computing, 118, 103051.
