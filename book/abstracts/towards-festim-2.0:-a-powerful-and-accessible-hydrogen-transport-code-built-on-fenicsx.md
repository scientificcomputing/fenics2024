---
title: 'Towards FESTIM 2.0: A powerful and accessible hydrogen transport code built on FEniCSx'
authors:
  - name: J. Dark
    affiliation: CEA IRFM/GCFPM  Cadarache Saint-Paul-les-Durance F-13108 France
    email: james.dark@cea.fr
  - name: R. Delaporte-Mathurin
    affiliation: Université Sorbonne Paris Nord Laboratoire des Sciences des Procédés et des Matériaux LSPM CNRS UPR 3407 Villetaneuse F-93430 France
  - name: S. Meschini
    affiliation: Plasma Science and Fusion Center Massachusetts Institute of Technology Cambridge MA 02139 USA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

FESTIM (Finite Element Simulation of Tritium In Materials) is a flexible, open-source finite element code developed in Python to model hydrogen transport within materials (Delaporte-Mathurin et al., 2024). It is an effective and open tool and capable of facilitating multi-dimensional simulations involving multiple materials using the FEniCS library.

With the launch of FeniCSx, the chance was seized to re-define FESTIM's object-oriented framework, clearing away accumulated technical debt and paving the way for smoother future enhancements. The revamped implementation supports the modelling of multiple species, allowing for more physical phenomena such as multi-level trapping and isotopic exchange. Simultaneously, this new open development phase has prompted us to establish a robust community infrastructure, enabling the alignment of the code with the community's requirements.

The updated approach for simulating the diffusion and trapping of hydrogen is presented alongside other enhancements made to re-build FESTIM with FEniCSx. Additionally, our strategy for employing innovative DG methods is outlined to accurately model the discontinuous concentrations that occur at the boundaries between different materials.


# References
Delaporte-Mathurin, R., Dark, J., Ferrero, G., Hodille, E. A., Kulagin, V., & Meschini, S. (2024). Festim: An open-source code for Hydrogen Transport Simulations. International Journal of Hydrogen Energy, 63, 786–802. https://doi.org/10.1016/j.ijhydene.2024.03.184
