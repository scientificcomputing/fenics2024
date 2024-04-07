---
title: 'Mesh-independent topology optimization in FEniCSx'
authors:
  - name: Michal Habera
    affiliations:
      - Rafinex
    email: michal.habera@rafinex.com
  - name: Jack S. Hale
    affiliations:
      - University of Luxembourg
    email:
  - name: Johannes Neumann
    affiliations:
      - Rafinex
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Compliance-driven topology optimization is a problem with many industrial applications. Countless algorithmic and discretization approaches have been proposed since its development in the engineering community in the past century. Many of the proposed methods follow heuristic arguments to avoid checkerboarding, while the independence of the optimal solution on mesh refinement in terms of the solution and number of iterations is rarely tested.

A method based on weighted H^1 scalar product is presented and we discuss its relation to some of the most commonly used methods from the perspective of performance, robustness, mesh-independence and ease of implementation in FEniCSx. We provide comparisons for standard benchmark problems (cantilever beam and L-shape bracket). We also demonstrate industrial challenges for large-scale topology optimization with manufacturing constraints.
