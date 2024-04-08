---
title: 'Checkpoint schedules for adjoint solvers'
authors:
  - name: Daiane Dolci
    affiliation: Imperial College London
    email: d.dolci@imperial.ac.uk
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The use of adjoint calculations to compute the gradient of a quantity of interest resulting from the solution of a system of partial differential equations (PDEs) is widespread and well-established. Adjoint PDEs are solved in reverse time and depend on forward data. Storing the entire forward state in preparation for the adjoint calculation has a memory footprint linear in the number of time steps, exhausting the computer systems. For memory usage control in adjoint solvers, checkpointing algorithms store only the state required to restart the forward calculation from a limited set of steps.

There exists a diversity of checkpointing algorithms whose applicability and optimality depend on the nature and parameters of the problem to be solved. From the perspective of users who wish to construct adjoint solvers, this creates the need to swap out different checkpointing algorithms in response to changes in equations, discretisations, and computer systems. To address this issue, the checkpoint_schedules Python package (Dolci et al., 2024) offers multiple interchangeable checkpointing algorithms through a unified interface. checkpoint_schedules can be used in conjunction with an adjoint framework, such as differentiation algorithmic tlm_adjoint (Maddison et al., 2019) or pyadjoint (Mitusch et al., 2019) and a compatible PDE framework, such as Firedrake (Ham et al., 2023) or FEniCS (Alnaes et al., 2015), enabling users to create adjoint solvers for their choice of PDE, numerical methods, and checkpointing algorithm, all without recoding the underlying algorithms.

In this work, we aim to present the concept of checkpoint_schedules abstraction and how we reach its integration into adjoint solvers. Furthermore, we will explain how this package integrates with Firedrake's adjoint via pyadjoint (Mitusch et al., 2019) and its functionality through examples using different checkpointing algorithms available in checkpoint_schedules.

# References
Alnaes, M. S., Blechta, J., Hake, J., Johansson, A., Kehlet, B., Logg, A., Richardson, C., Ring, J., Rognes, M. E., & Wells, G. N. (2015). The FEniCS project version 1.5. Archive of Numerical Software, 3. doi:10.11588/ans.2015.100.20553 .

Dolci, D. I., Maddison, J. R., Ham, D. A., Pallez, G., & Herrmann, J. (2024). checkpoint_schedules: schedules for incremental checkpointing of adjoint simulations. Journal of Open Source Software, 9(95), 6148. doi:10.21105/joss.06148

Ham, D. A., Kelly, P. H. J., Mitchell, L., Cotter, C. J., Kirby, R. C., Sagiyama, K., Bouziani, N., Vorderwuelbecke, S., Gregory, T. J., Betteridge, J., Shapero, D. R., Nixon-Hill, R. W., Ward, C. J., Farrell, P. E., Brubeck, P. D., Marsden, I., Gibson, T. H., Homolya, M., Sun, T.,  MacRae, A. T. T., Luporini, F., Gregory,A., Lange, M., Funke, S. W., Rathgeber, F ,  Bercea, G-T Markall, G. R. (2023). Firedrake user manual (First edition). Imperial College London; University of Oxford; Baylor University; University of Washington. doi:10.25561/104839

Maddison, James R., Goldberg, D. N., & Goddard, B. D. (2019). Automated calculation of higher order partial differential equation constrained derivative information. SIAM Journal on Scientific Computing, 41(5), C417–C445. doi:10.1137/18M1209465

Mitusch, S., Funke, S., & Dokken, J. (2019). dolfin-adjoint 2018.1: automated adjoints for FEniCS and Firedrake. Journal of Open Source Software, 4(38), 1292. doi:10.21105/joss.01292
