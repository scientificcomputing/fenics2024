---
title: 'Custom quadrature at runtime in FEniCSx'
authors:
  - name: August Johansson
    affiliations:
      - SINTEF Digital
    email: august.johansson@sintef.no
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

In this contribution, we will present a library, currently called customquad, that allows users to provide their own quadrature rules in each element of a mesh. We say that these user-provided rules are provided at runtime, in contrast to the standard rules, which are fixed when the forms are compiled by ffcx.

The main motivation for having this functionality is finite element methods on non-matching meshes. In such methods, the computational domain, often denoted by \Omega, is not approximated by the mesh used in the finite element discretization but rather in some other way. For example, this may be a level set function or splines such as NURBS. Examples of such methods include CutFEM, \phi-FEM and TraceFEM. In these methods, special quadrature rules are needed to evaluate the integrals over \Omega. The functionality is also desired in problems where locally finer quadrature rules are required, for example for error control.

The implementation constitutes changes to the ffcx core to allow the use of the user-provided quadrature in the evaluation of the basis functions using basix. User-provided normal vectors may also be passed to the forms. The assembly, which is yet only in Python, is performed utilizing the dolfinx's capability for custom assemblers; no changes to dolfinx are needed.

# References
https://github.com/augustjohansson/customquad
