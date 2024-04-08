---
title: 'Time discretization methods for coupled PDEs'
authors:
  - name: Robert Altmann
    affiliations:
      - Otto-von-Guericke-Universität Magdeburg
    email: abdullah.mujahid@simtech.uni-stuttgart.de
  - name: Abdullah Mujahid
    affiliations:
      - Universität Stuttgart
    email:
  - name: Benjamin Unger
    affiliations:
      - Universität Stuttgart
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Many physical phenomena are modeled as a coupled system of PDEs, for example, poroelasticity which is an elliptic-parabolic system.
To exploit the better structural properties of the sub systems, decoupling the system is an attractive idea.
Moreover, with the decoupled systems, one can design efficient preconditioners for higher order in time discretization.

In this talk, we introduce a framework for time discretization of coupled PDEs using BDF and RK methods.
This framework includes monolithic, iterative and non-iterative methods.
