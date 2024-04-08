---
title: 'Regularized reduced order models for incompressible flows'
authors:
  - name: Francesco Ballarin
    affiliations:
      - Università Cattolica del Sacro Cuore
    email: francesco.ballarin@unicatt.it
  - name: Anna Sanfilippo
    affiliations:
      - Università di Trento
  - name: Ian Moore
    affiliations:
      - Virginia Tech
  - name: Traian Iliescu
    affiliations:
      - Virginia Tech
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Numerical simulations of incompressible flows is often computationally expensive. Reduced order modelling (ROM) has emerged in the last decades as a viable option to alleviate the resulting computational demand.
In this presentation we discuss a ROM strategy for under-resolved convection-dominated flows based on a novel regularization technique, namely the approximate deconvolution Leray ROM (ADL-ROM). We will present theoretical foundations of the resulting ADL-ROM by means of error bounds. Furthermore, we will show how the proposed ROM can be implemented in FEniCSx and RBniCSx, and discuss some numerical results on benchmark cases.
