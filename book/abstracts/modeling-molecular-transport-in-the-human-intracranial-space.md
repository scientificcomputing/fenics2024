---
title: 'Modeling molecular transport in the human intracranial space'
authors:
  - name: Rami Masri
    affiliations:
      - Simula
    email: miroslav@simula.no
  - name: Miroslav Kuchta
    affiliations:
      - Simula
    email:
  - name: Marius Causemann
    affiliations:
      - Simula
    email:
  - name: Marie Rognes
    affiliations:
      - Simula
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Molecular transport in perivascular spaces (PVSs) plays an important role in clearance
and delivery in the human brain. Previous studies indicate rapid movement of molecules
in the subarachnoid space (SAS) and PVSs surrounding pial arteries, however, the exact
mechanisms are not fully understood. Moreover, computational investigations of the phenomena
in terms of fully resolved $3d$-$3d$ models are prohibitively expensive due to the complex
geometry of the PVSs. To address these challenges, we introduce a $3d$-$1d$ model [1, 2]
of the convective and diffusive transport in the PVS and the parenchyma. We discuss approximation
properties of the reduced-order model and describe the finite element discretization of the
resulting coupled system. Our implementation isolates the mixed-dimensional coupling and
leverages existing FEniCS functionality for the remaining parts. Using recent imaging data
of the human pial vasculature we finally showcase capabilities of the model/solver by studying
brain clearance on the whole organ scale.


# References
[1] Masri, R., Kuchta, M., & Riviere, B. (2023). Discontinuous Galerkin methods for 3D-1D systems. arXiv preprint arXiv:2312.16565.

[2] Masri, R., Zeinhofer, M., Kuchta, M., & Rognes, M. E. (2023). The modelling error in multi-dimensional time-dependent solute transport models. arXiv preprint arXiv:2303.17999.
