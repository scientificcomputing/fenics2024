---
title: 'Improved post-processing of transient heat transfer experiments using the finite element method'
authors:
  - name: Bram Hulhoven
    affiliations:
      - University of Cambridge
    email: bh479@cam.ac.uk
  - name: Joseph Dean
    affiliations:
      - University of Cambridge
    email:
  - name: Nicholas Atkins
    affiliations:
      - University of Cambridge
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

In transient heat transfer experiments, the temperature of a test substrate exposed to forced convection is measured in response to a near step change in freestream temperature. However, the quantity of engineering interest is the heat transfer coefficient (HTC), which also requires the corresponding heat flux at the substrate’s surface for its calculation. Since the heat flux is not measured directly, it is commonly reconstructed from the measured temperature field using the impulse response method by Oldfield [1], which assumes 1D semi-infinite conduction and therefore introduces lateral conduction errors on highly curved surfaces or at steep gradients in the boundary conditions. This presentation highlights the improved accuracy that can be obtained if the heat flux is instead calculated using a finite element (FE) model. The heat flux is solved for directly using a mixed method, which is implemented using FEniCSx. First, it will be shown that the HTC distribution over a backward- and forward-facing step post-processed using a 2D model in FEniCSx matches the results obtained using the Oldfield method in regions where the 1D semi-infinite assumption holds. The improved accuracy in the HTC distribution obtained using the FE model will then be demonstrated using virtual experiments for two stylised cases: a flat plate exposed to forced convection with a step change in HTC, and an aerofoil with an HTC distribution representative of a turbine blade.

# References
[1] Oldfield, M. (2008). Impulse response processing of transient heat transfer gauge signals. Journal of Turbomachinery, 130(2).
