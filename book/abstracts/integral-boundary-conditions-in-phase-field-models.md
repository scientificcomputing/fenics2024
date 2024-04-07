---
title: 'Integral boundary conditions in phase field models'
authors:
  - name: Xiaofeng Xu
    affiliations:
      - King Abdullah University of Science and Technology
    email: xiaofeng.xu@kaust.edu.sa
  - name: Lian Zhang
    affiliations:
      - Shenzhen Research Institute of Big Data
    email:
  - name: Yin Shi
    affiliations:
      - Pennsylvania State University
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Modeling the chemical, electric and thermal transport as well as phase transitions and the accompanying mesoscale microstructure evolution within a material in an electronic device setting involves the solution of partial differential equations often with integral boundary conditions. Employing the familiar Poisson equation describing the electric potential evolution in a material exhibiting insulator to metal transitions, we exploit a special property of such an integral boundary condition, and we properly formulate the variational problem
and establish its well-posedness. We then compare our method with the commonly-used Lagrange multiplier method that can also handle such boundary conditions. Numerical experiments demonstrate that our new method achieves optimal convergence rate in contrast to the conventional Lagrange multiplier method. Furthermore, the linear system derived from our method is symmetric positive definite, and can be efficiently solved by Conjugate Gradient method with algebraic multigrid preconditioning.

# References
Xu, X., Zhang, L., Shi, Y., Chen, L.-Q., & Xu, J. (2023). Integral boundary conditions in phase field models. Computers & Mathematics with Applications, 135, 1–5. https://doi.org/10.1016/j.camwa.2022.11.025
