---
title: 'PDE Constrained Shape Optimization with cashocs'
authors:
  - name: Sebastian Blauth
    affiliations:
      - Fraunhofer ITWM
    email: sebastian.blauth@itwm.fraunhofer.de
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

As the computational solution of PDE constrained shape optimization problems is still a very challenging task, there is high demand for efficient solution algorithms, particularly for complex problems arising from industrial applications. In this talk, we present cashocs, a software package which automates the solution of such problems and facilitates their efficient solution.

The software allows users to formulate their problems in the high-level Unified Form Language (UFL), which closely resembles mathematical notation. As users only have to change a few lines in their code, switching from a simulation in FEniCS to an optimization with cashocs is straightforward. Moreover, cashocs uses the UFL to derive the corresponding adjoint systems and shape derivatives with automatic differentiation, so that there is no more need for tedious and error-prone calculations by hand.

In cashocs, many state-of-the-art solution algorithms for shape and topology optimization problems are implemented, e.g., space mapping methods for shape optimization as well as quasi-Newton and nonlinear CG methods for both shape and topology optimization. Additionally, cashocs provides many sophisticated methods to ensure a sufficiently high mesh quality and even has support for automated remeshing, which is crucial for shape optimization. Finally, we present several industrial applications from fluid dynamical shape optimization which are optimized with cashocs. The results highlight the performance as well as the efficiency and applicability of cashocs even for very complex problems.
