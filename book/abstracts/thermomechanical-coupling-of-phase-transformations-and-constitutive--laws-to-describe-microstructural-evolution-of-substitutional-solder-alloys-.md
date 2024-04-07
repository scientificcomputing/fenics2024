---
title: 'Thermomechanical coupling of phase transformations and constitutive  laws to describe microstructural evolution of substitutional solder alloys '
authors:
  - name: Wolfgang Flachberger
    affiliations:
      - Chair of Mechanics - University of Mining Leoben
    email: wolfgang.flachberger@unileoben.ac.at
  - name: Thomas Antretter
    affiliations:
      - Chair of Mechanics - University of Mining Leoben
    email:
  - name: Jiri Svoboda
    affiliations:
      - Institute of Physics of Materials - Academy of Sciences of the Czech Republic
    email:
  - name: Silvia Leitner
    affiliations:
      - Materials Center Leoben Forschung GmbH
    email:
  - name: Manuel Petersmann
    affiliations:
      - Kompetenzzentrum Automobil- und Industrieelektronik GmbH
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

This study introduces a Lagrangian formulation for straightforward coupling of diffusional phase transformations with continuum mechanics through the mixed finite element method. The adoption of the Lagrange formalism is motivated by the inherent capability of FEniCSx to generate weak forms form variational minimization problems (as, for example, demonstrated by the hyperelasticity demo). The research focuses on examining the interplay between mechanical stresses and phenomena like segregation and damage observed at microscale levels within microelectronic solder materials.
In contrast to prevailing methodologies like the Phase Field Method (PFM), our approach can also be used without laplacian regularization which, results in a more “sharp” phase transition. Surprisingly, we demonstrate that our proposed model can be interpreted as limiting case of Cahn Hilliard diffusion.
We investigate a binary system governed by four differential equations, employing an implicit, fully coupled scheme to solve them. Our diffusion model accurately predicts phase growth and damage-related phenomena, including the trapping of components at grain boundaries and other imperfections. Moreover, we couple the diffusion model with a constitutive model for mechanical material behavior, enabling bidirectional influence between diffusion and mechanics.
This comprehensive coupling facilitates an intricate exploration of various phenomena observed in microelectronic soldering at small scales. Through this interdisciplinary approach, we aim to contribute valuable insights into the intricate dynamics governing microscale material behavior, with potential implications for advanced manufacturing processes and material design.
