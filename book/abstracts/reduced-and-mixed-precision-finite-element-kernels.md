---
title: 'Reduced- and mixed-precision finite element kernels'
authors:
  - name: M. Croci
    affiliation: Ikerbasque and Basque Center for Applied Mathematics
    email: mcroci@bcamath.org
  - name: G. N. Wells
    affiliation: University of Cambridge
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

In this talk we investigate the effect of rounding errors in the computation of finite element (FE) kernels
and we develop strategies for reduced- and mixed-precision acceleration using half-precision floating point formats.
Possible applications of this work include: reduced- and mixed-precision preconditioning, linear and nonlinear solvers, and timestepping methods.

The popularity of artificial intelligence has pushed for the design of computer architectures that
are increasingly faster at performing computations using fewer bits. For instance, 16-bit half-precision computations
are over 32 times more efficient than double precision computations on NVIDIA H100 GPU tensor cores. However,
reducing the precision leads to a significant increase in rounding errors and extreme care must be taken during algorithmic design.

With the objective of exploiting these new chip capabilities in FE methods, we focus on FE cell kernels for matrix assembly.
By analysing the algorithm used by FFCx, we show that the total rounding error is comprised of two terms:
1) A geometry term depending on the condition number of the Jacobian of the map to the reference cell.
2) A quadrature term growing with the number of quadrature nodes.
Based on this analysis, we propose a strategy for obtaining machine-accurate results at negligible efficiency loss via a mixed-precision treatment.

While this is currently work in progress, early-stage numerical experiments on Intel Sapphire Rapids CPUs show appreciable speedups compared to
their double precision equivalents and support our theoretical findings. Additionally, we show how the latest Sapphire Rapids AMX-BF16 registers
and instructions offer great promise for further incresing accuracy and speed (although compiler and/or register improvements would be needed).
