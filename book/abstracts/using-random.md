---
title: 'Using random circular models to simulate stochastic anisotropic flow in aquifer systems with FEniCSx'
authors:
  - name: Sona Salehian Ghamsari
    affiliation:  Institute of Computational Engineering, Department of Engineering, Faculty of Science, Technology, and Medicine, University of Luxembourg
    email: sona.salehianghamsari@uni.lu
  - name: Guendalina Palmirotta
    affiliation: Department of Mathematics, Faculty of Science, Technology, and Medicine, University of Luxembourg
  - name: Tonie Van Dam
    affiliation: Department of Geology and Geophysics, College of Mines and Earth Sciences, University of Utah
  - name: Jack S. Hale
    affiliation: Institute of Computational Engineering, Department of Engineering, Faculty of Science, Technology, and Medicine, University of Luxembourg
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The flow of water in many aquifers is driven by strong anisotropy created by preferential flow features such as cracks and faults. This anisotropy can be modelled by introducing anisotropic hydraulic conductivity tensor (AHC) into the equations of poroelasticity. Our overall goal is to assimilate InSAR remote sensing data into a model of an aquifer system in order to infer information about AHC.

Previous studies have modelled the hydraulic conductivity as a spatially varying isotropic Gaussian process (Alghamdi et al. 2020). In this work we develop a flexible stochastic prior model of the AHC tensor that respects its underlying symmetry and positive definiteness. Our method for calibrating and constructing a random model for the AHC tensor consists of three steps; 1) We fit a Bayesian model consisting of a mixture of circular von Mises distributions to fracture outcrop data. 2) We fit a Bayesian model of two independent log-normals to existing estimates of the hydraulic conductivity in the principal directions. Then in the last step 3) these stochastic models are then simultaneously fed into an extended version of the model by Shivanand et al. (2024) for constructing random symmetric positive definite tensors. This model leverages the spectral decomposition to enable the separate encoding of size and orientation. The overall methodology is demonstrated via a stochastic finite element model of the Anderson Junction aquifer test developed in our previous study (Salehian et al. 2024) following the aquifer pumping test described in Heilweil and Hsieh (2006).


# References
Alghamdi, A., Hesse, M. A., Chen, J., Ghattas O., 2020. Bayesian Poroelastic Aquifer Characterization from InSAR Surface Deformation Data. Part 1: Maximum A Posteriori Estimate. Water Resources Research 50, 10, e2020WR027391. doi:10.1029/2020WR027391



Salehian Ghamsari, S., van Dam, T., and Hale, J.S., 2024. Can the anisotropic hydraulic conductivity of an aquifer be determined using surface displacement data? A case study. Preprint.



Shivanand, S.K., Rosić, B., and Matthies, H.G., 2024. Stochastic modelling of symmetric positive definite material tensors. Preprint, arXiv:2109.07962.6.



Heilweil, V.M., and Hsieh, P.A., 2006. Determining Anisotropic Transmissivity Using a Simplified Papadopulos Method. Groundwater 44, 749–753. doi:10.1111/j.1745-6584.2006.00210.x.
