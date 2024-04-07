---
title: 'Function scaling and convergence control in highly nonlinear Poisson-Boltzmann electrolyte models.'
authors:
  - name: Drew Parsons
    affiliations:
      - id: a
        institution: University of Cagliari and CSGI
        department: Department of Chemical and Geological Sciences
        address: Cittadella Universitaria, S.S. 554 bivio Sestu,
        region: 09042 Monserrato (CA)
        country: Italy
    email: drew.parsons@unica.it
  - name: Matteo Farci
    affiliation: a
  - name: Alin Grigoras
    affiliation: a
  - name: Dagmawi Tadesse(b)
    affiliations:
      - id: b
        institution: Murdoch University.
        department: Discipline of Physics, Chemistry and Mathematics
        address: 90 South St, Murdoch 6150
        country: West Australia
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The nonlinear Poisson-Boltzmann model of electrolyte solutions combines the Poisson equation for electrostatic potentials with a Boltzmann equilibrium of mobile ion concentrations. The Boltzmann equation c(x) = c0 exp[-qψ(x)/kT] is highly nonlinear once the electrostatic potential exceeds several thermal energy (kT) units (i.e. when ψ>100mV). This introduces two related numerical challenges. Firstly, suitable convergence criteria for the concentration functions becomes variable, depending on the boundary potential. Secondly  a controlled initial guess must be provided must be provided to avoid the FEM calculation diverging to NaN. We resolve the first by logarithmic scaling of the concentration function, as suggested by the exponential nature of the Poisson equation.  However a nontrivial complex logarithmic form is required in order to allow for the near-zero concentrations of coions, which would trigger numerical divergence in a trivial ln[c(x)] scaled function. The second challenge is resolved by iteratively applying a throttle factor that suppresses large boundary conditions back to the linear regime, which is then applied as an initial guess for the nonlinear regime. Our implementation allows for other nonelectrostatic molecular interactions [1] important for modelling real chemical [2] and electrochemical [3] systems, enabling computation of concentrated electrolytes with potentials exceeding 5000 mV.


# References
[1]  Tadesse, D., Parsons, D. F. (2024). Thermodynamics beyond dilute solution theory: Steric effects and electrowetting. In: Wandelt, K., Bussetti, G. (eds.) Encyclopedia of Solid-Liquid Interfaces. Elsevier. ISBN: 9780323856690. https://doi.org/10.1016/B978-0-323-85669-0.00137-9

[2]  Parsons, D.F., Carucci, C.,  Salis,  A. (2022). Buffer-specific eﬀects arise from ionic dispersion forces. Phys. Chem. Chem. Phys., 24, 6544. https://doi.org/10.1039/d2cp00223j

[3]  Tadesse, D., Parsons, D. F. (2022). The impact of steric repulsion on the total free energy of electric double layer capacitors. Colloids and Surfaces A, 648, 129134. https://doi.org/10.1016/j.colsurfa.2022.129134
