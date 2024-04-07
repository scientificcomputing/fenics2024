---
title: 'Control Theory based adaptive time stepping for partitioned fluid-structure interactions'
authors:
  - name: Keni Joseph Sebastian
    affiliations:
      - Fraunhofer Scientific Computing and Algorithms Institute (SCAI)
    email: keni.joseph.sebastian@scai.fraunhofer.de
  - name: Pascal Bayrasy
    affiliations:
      - Fraunhofer Scientific Computing and Algorithms Institute (SCAI)
    email:
  - name: Helena Sakellaris
    affiliations:
      - Fraunhofer Scientific Computing and Algorithms Institute (SCAI)
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The work presented in this poster explores the performance of a Control Theory based  adaptive time stepping procedure for partitioned black-box Fluid-Structure Interaction (FSI) simulations. The Computational Fluid Dynamics (CFD) and Computational Structural Mechanics (CSM) solvers are both set up in FEniCS, but treated as black-box codes providing access only to the variables at the interface. A fully implicit stabilized ALE formulation of the incompressible navier-stokes is used for the CFD solver, while the CSM solver is set up to handle various elasticity models such as linear, St.Venant Kirchoff and Neo-Hookean along with time integration schemes such as the Newmark Linear Acceleration and Newmark Constant Acceleration. Acceleration techniques for coupling such as Reduced Order Modelling (ROM) and Quasi-Newton Methods are used. Comparison of the incorporated CFD, CSM and FSI solvers are  done against various benchmark, textbook and tutorial cases, and have produced comparable results. Since no access to the time-discretization methods is provided by the black box codes, an adaptive time stepping procedure using a Proportional-Integral-Derivative (PID) controller is an ideal candidate.The results from this work provide insights into implementing adaptive time stepping using a PID controller for coupling environments which couple commercial black-box codes.

Keywords: Fluid-Structure Interaction, Finite Element Method, Control Theory, Adaptive time stepping

# References

[1] Valli, A. M. P., Carey, G. F., & Coutinho, A. L. G. A. (2002). Control strategies for timestep selection in simulation of coupled viscous flow and heat transfer. Communications in Numerical Methods in Engineering, 18(2), 131-139. https://doi.org/10.1002/cnm.475

[2] Bogaers, A. E. J., Kok, S., Reddy, B. D., & Franz, T. (2014). Quasi-Newton methods for implicit black-box FSI coupling. Computer Methods in Applied Mechanics and Engineering, 279, 113-132. https://doi.org/10.1016/j.cma.2014.06.033

[3] Degroote, J., Bruggeman, P., Haelterman, R., & Vierendeels, J. (2008). Stability of a coupling technique for partitioned solvers in FSI applications. Computers & Structures, 86(23), 2224-2234. https://doi.org/10.1016/j.compstruc.2008.05.005

[4] Wolf, K., Bayrasy, P., Brodbeck, C., Kalmykov, I., Oeckerath, A., & Wirth, N. (2017). MpCCI: Neutral Interfaces for Multiphysics Simulations. https://doi.org/10.1007/978-3-319-62458-7_7

[5] Turek, S., & Hron, J. (2007). Proposal for numerical benchmarking of fluid–structure interaction between an elastic object and laminar incompressible flow. In Fluid-Structure Interaction: Modelling, Simulation, Optimisation (Vol. 53, pp. 371-385). https://doi.org/10.1007/3-540-34596-5_15

[6] Kamensky, D. (2022). Lecture notes for MAE 207: Finite element analysis for coupled problems. Retrieved from https://drive.google.com/file/d/1o0DY1RWoXd-gOISqyRzJoDHUHvSMvSg3/view
