---
title: "Higher-Order Time-Stepping in Multiphysics Using preCICE"
authors:
  - name: Niklas Vinnitchenko
    affiliations: Technical University of Munich
    email: niklas.vinnitchenko@tum.de
  - name: Prof. Dr. Hans-Joachim Bungartz
    affiliation: Technical University of Munich
  - name: Prof. Dr. Benjamin Uekermann
    affiliations: University of Stuttgart
  - name: M.Sc. (hons) Benjamin Rodenberg
    affiliations: Technical University of Munich
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
---

Multi-physics problems are often simulated with the help of partitioning to reduce the complexity of this task. Coupling is one necessary step when following this divide-and-conquer approach. The coupling library preCICE provides a high-level user interface to simplify the coupling of different solvers by treating them as black-boxes. Using the FEniCS-preCICE adapter makes coupling FEniCS code even more straightforward. (Rodenberg et al., 2021) To solve partitioned and time-dependent problems with higher-order, preCICE offers a feature called time interpolation. Utilizing this feature allows each coupling participant to individually use its own time stepping without complicating the code (Rüth et al., 2020).
This poster shows how one can combine time interpolation in preCICE with an FEniCS solver using higher-order time-stepping schemes. To implement higher-order Runge-Kutta methods in FEniCS, we follow an approach from Farrell et al. (2021). While usually one often has to hard-code any time-stepping scheme into an equation's weak form, our approach only demands the user to provide the Butcher tableaux of the Runge-Kutta method. The weak formulation employing the given time-stepping scheme is then algorithmically determined (Farrell et al., 2021; Wullenweber, 2021). Convergence results of programs coupling FEniCS with other software while using the approach from above are also presented in this poster. My bachelor thesis is used as a basis for this (Vinnitchenko, 2024).


# References
Farrell, P. E., Kirby, R. C. & Marchena-Menéndez, J. (2021). Irksome: Automating Runge–Kutta Time-stepping for Finite Element Methods. ACM Transactions On Mathematical Software, 47(4), 1–26. doi:10.1145/3466168



Rodenberg, B., Desai, I., Hertrich, R., Jaust, A. & Uekermann, B. (2021). FEniCS–preCICE: Coupling FEniCS to other simulation software. SoftwareX (Amsterdam), 16, 100807. doi:10.1016/j.softx.2021.100807



Rüth, B., Uekermann, B., Mehl, M., Birken, P., Monge, A. & Bungartz, H. (2020). Quasi‐Newton waveform iteration for partitioned surface‐coupled multiphysics applications. International Journal For Numerical Methods in Engineering, 122(19), 5236–5257. doi:10.1002/nme.6443



Vinnitchenko, N. (2024). Evaluation of Higher-Order Coupling Schemes with FEniCS-preCICE. https://mediatum.ub.tum.de/doc/1732367/1732367.pdf



Wullenweber, N. (2021). Higher-order time stepping schemes for solving partial differential equations with FEniCS. https://mediatum.ub.tum.de/doc/1621360/1621360.pdf
