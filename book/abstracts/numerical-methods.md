---
title: 'Numerical Methods for the Cahn-Hilliard Equation with a Logarithmic Potential'
authors:
  - name: Pavan Inguva
    affiliations:
      - Massachusetts Institute of Technology
    email: inguvakp@mit.edu
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The Cahn-Hilliard equation is a fourth-order nonlinear PDE that forms the basis of many phase-field models (PFMs). The Cahn-Hilliard equation, and its variants, find application in analyzing a variety of multiphase and multicomponent systems such as multiphase fluid dynamics, microstructure evolution, and vesicle formation. To fully specify the Cahn-Hilliard equation, a thermodynamic potential needs to be supplied. In most cases, a quartic polynomial is used which is suffices for mathematical analysis. However, to accurately model physical systems, a thermodynamic potential that accurately describes the physics of a real system is necessary. The Flory-Huggins equation, based on regular solution theory, has both a simple functional form and is commonly used to study many real systems such as polymer solutions. The Flory-Huggins equation is commonly referred to as a logarithmic potential in the PFM literature.

The numerical solution of PFMs using the Flory-Huggins equation for realistic parameter values (i.e., large values of the Flory-Huggins interaction parameter) is challenging due to numerical convergence issues. This presentation explores strategies for developing numerical methods that can accurately and efficiently solve the Cahn-Hilliard equation with. We consider various aspects of the solution procedure such as the choice of the discretization scheme and nonlinear solver method. Strategies are first considered using finite differences to facilitate analysis and subsequently implemented in FEniCS. Results for the two- and three-component Cahn-Hilliard equations in both one and two dimensions are presented.
