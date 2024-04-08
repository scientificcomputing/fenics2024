---
title: 'Modeling the shock-to-detonation transition at the mesoscale : a reactive molecular dynamics informed continuum model with FEniCS-based simulation'
authors:
  - name: Paul Bouteiller
    affiliations:
      - id: cea
        institution: CEA-DAM DIF
        department: F-91297 Arpajon CEDEX
        country: France
    email: paul.bouteiller99@gmail.com
  - name: Paul Lafourcade
    affiliation: cea
  - name: Paul Lafourcade
    affiliation: cea
  - name: Jean-Bernard Maillet
    affiliation: cea
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

This abstract outlines a study on developing mesoscale reactive models for energetic materials like TATB and HMX. Specifically, a simplified chemical reactive model for TATB identified from adiabatic decompositions at the atomic scale using classical Molecular Dynamic (MD) simulations accurately represents the material's behavior with just four components. This model facilitates the calibration of Arrhenius laws and heats of reaction by tracking the evolution of component concentrations and temperature under different conditions.

Further, the study extends the model to include equations of state (EOS) for each reaction intermediate to account for pressure changes during reactions, critical for modeling the shock-to-detonation transition. This involves calibrating MACAW-based and Jones-Wilkins-Lee (JWL) EOS against MD simulations. The full model is implemented in our in house code, leveraging the FEniCSx open-source library, designed to address the elastoplastic finite strain problem with phase transitions using the finite element method (FEM). This multi-field problem is tackled sequentially by integrating a conventional explicit strategy with standard isoparametric elements for displacement, whereas, the evolution of the concentrations of various constituents is resolved on a cell-by-cell basis through Discontinuous Galerkin elements. This setup allows for seamless dimensional scalability and the integration of various evolution laws.

The research demonstrates the model's capability in simulating shock-to-detonation transition and investigating hotspot criticality, highlighting its potential for predicting the dynamic behavior of energetic materials under non equilibrium conditions.
