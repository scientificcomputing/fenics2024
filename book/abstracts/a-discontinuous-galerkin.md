---
title: 'A Discontinuous Galerkin solver in FEniCS for the 2D Incompressible Navier Stokes Equations'
authors:
  - name: Keni Joseph Sebastian
    affiliations:
      - University of Koblenz
    email: kenijosephsebastian@uni-koblenz.de
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The work discussed in this presentation explores the performance of a Discontinuous Galerkin (DG) based Computational Fluid Dynamics (CFD) solver implemented in FEniCS. The DG method is analysed and implemented in FEniCS for processes such as diffusion/heat equation, advection, linear convection-diffusion, non-linear convection-diffusion such as vector viscous burger, before finally being implemented for 2D Incompressible Navier Stokes (NS) Equations. A Symmetric Interior Penalty (SIP) method is used to the treat the diffusion terms, Lax-Friedrichs flux as the Numerical flux for the convection terms, and central flux as the numerical flux for the pressure gradient and velocity divergence terms occurring in the stokes and NS equations. The Fractional step theta scheme in its fully unconditional setting is used for the time integration. The DG solver is compared against various benchmark and tutorials cases solved using Continuous Galerkin (CG) method. For the 2D incompressible NS case, the DG solver produces results in good agreement with the DFG 2D-3 benchmark in FeatFlow as well as the FEniCS tutorial of flow through L-shaped channel.
Keywords: Discontinuous Galerkin, Computational Fluid Dynamics, Fractional step theta

# References
[1] Hartmann, R. (2008). Numerical Analysis of Higher Order Discontinuous Galerkin Finite Element Methods. In VKI Lecture Series (Vol. 2008-0, pp. 1-107). ISBN 13 978-2-930389-88-5. Retrieved from https://elib.dlr.de/57074/1/Har08b.pdf

[2] Fehn, N., Wall, W. A., & Kronbichler, M. (2018). Robust and efficient discontinuous Galerkin methods for under-resolved turbulent incompressible flows. Journal of Computational Physics, 372, 667–693. doi:10.1016/j.jcp.2018.06.037

[3] Gross, S., & Reusken, A. (2011). Numerical Methods for Two-phase Incompressible Flows (1st ed.). Springer Berlin, Heidelberg. doi:10.1007/978-3-642-19686-7

[4] Featflow - Department of Mathematics. DFG flow around cylinder benchmark 2D-3, fixed time interval (Re=100). Retrieved from https://wwwold.mathematik.tu-dortmund.de/~featflow/en/benchmarks/cfdbenchmarking/flow/dfg_benchmark3_re100.html
