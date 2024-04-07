---
title: 'Estimation of optimal inlet boundary condition for blood flow assessment in abdominal aortic aneurysm using variational data assimilation '
authors:
  - name: Sara Paratico
    affiliations:
      - id: milano
        institution:  Politecnico di Milano, Department of Electronics, Information, and Bioengineering
        city: Milano
        country: Italy
    email: sara.paratico@gmail.com
  - name: Riccardo Munafò
    affiliation: milano
  - name: Chiara Trenti
    affiliations:
      - id: lin1
        institution:  Division of Cardiovascular Medicine, Department of Health, Medicine and Caring Sciences, Linköping University, Universitetssjukhuset, 581 83 Linköping
        country: Sweeden
      - id: lin2
        institution:  Center for Medical Image Science and Visualization (CMIV), Linköping University, Universitetssjukhuset, 581 83 Linköping,
        country: Sweeden
  - name: Petter Dyverfeldt
    affiliations: lin1; lin2
  - name: Emiliano Votta
    affiliation: milano
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Blood flow in abdominal aortic aneurysms is typically quantified via computational fluid dynamics (CFD) simulations, whose reliability depends on boundary conditions (BCs). This work aims to estimate an optimal inlet boundary condition by combining numerical solutions and in vivo measurements in an optimization framework. To this aim, we tested variational data assimilation (VarDA) [1] as a tool to define optimal BCs by minimizing the mismatch between the CFD solution and velocity data measured in vivo via 4D flow MRI in an aneurysmatic abdominal aorta, while maintaining consistency with physical and constitutive laws. A transient CFD simulation was performed using a finite element method based on an incremental pressure correction scheme (IPCS) implemented through FEniCS, discretizing the Navier-Stokes equations in time using a Crank-Nicolson time-stepping scheme [2]. Zero pressure was applied as outlet BC, and a stationary parabolic velocity profile was imposed as inlet BC. Upon benchmarking on an idealized 2D geometry, the 3D geometry reconstructed from in vivo data was tackled through the VarDA algorithm developed leveraging the dolphin-adjoint library [3]. The VarDA optimization routine was run for 10 iterations to minimize a cost function defined as the L2-norm of the error with respect to 4D flow MRI measurements plus a regularization term. As 4D flow MRI data are inherently affected by relevant errors in the near-wall region, the cost function was defined over a subdomain excluding points within a threshold distance from the walls. Before and after optimization, average velocity magnitude and maximum Wall Shear Stress (WSS) were compared vs. those yielded by the in-vivo measurements. The analysis revealed a relevant improvement in the optimized results following the application of the 3DVar algorithm, suggesting a more robust selection of the inlet BC. The next step is to implement a 4D (3D space and time) spatial VarDA CFD algorithm.

# References
[2] Dokken, J. S., Johansson, A., Massing, A., & Funke, S. W. (2020). A multimesh finite element method for the Navier–Stokes equations based on projection methods. Computer Methods in Applied Mechanics and Engineering, 368. https://doi.org/10.1016/j.cma.2020.113129

[1] Funke, S. W., Nordaas, M., Evju, Ø., Alnæs, M. S., & Mardal, K. A. (2019). Variational data assimilation for transient blood flow simulations: Cerebral aneurysms as an illustrative example. International Journal for Numerical Methods in Biomedical Engineering, 35(1). https://doi.org/10.1002/cnm.3152

[3] Mitusch, S., Funke, S., & Dokken, J. (2019). dolfin-adjoint 2018.1: automated adjoints for FEniCS and Firedrake. Journal of Open Source Software, 4(38), 1292. https://doi.org/10.21105/joss.01292
