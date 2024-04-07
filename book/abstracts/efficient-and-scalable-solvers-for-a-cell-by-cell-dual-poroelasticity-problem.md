---
title: 'Efficient and scalable solvers for a cell-by-cell dual-poroelasticity problem'
authors:
  - name: Marius Causemann
    affiliations:
      - Simula Research Laboratory
    email: mariusca@simula.no
  - name: Miroslav Kutcha
    affiliations:
      - Simula Research Laboratory
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Understanding the intricate interplay of mechanical forces and fluid dynamics at the cel-
lular scale is crucial for unravelling the complexities of brain function. Notably, cellular
swelling and volume regulation modulate brain states [1], while mechanical forces play a
pivotal role in structural plasticity and learning [2]. Recent advances in high-resolution
electron microscopy reconstructions of the mammalian brain pave the way for detailed
numerical investigations into these physiological processes in detailed cellular geometries.

Addressing the computational challenges posed by the high geometrical complexity of
entangled brain cells, we propose efficient and scalable solvers for cell-by-cell models of
cellular mechanics and fluid flow in cerebral tissue. Employing a dual-poroelasticity ap-
proach, we represent both the intracellular and extracellular spaces as poroelastic media.
The elastic solid models the cytoskeleton and the extracellular matrix, respectively, while
the fluid network represents intra- and extracellular fluid. The permeable cell mem-
brane separates both domains and allows hydrostatic and osmotic pressure-driven fluid
exchange, resulting in a Robin-type interface condition.

Motivated by conservation of mass on a discrete level we consider two different 3-field
formulations of the model using the total-pressure and flux as additional unknowns.
For each formulation, we introduce parameter-robust norm-equivalent preconditioners.
Demonstrating the efficiency and scalability of our FEniCS and Firedrake based solvers, we present numerical results showcasing cellular swelling on large-scale 3D reconstructions of the rat visual cortex.

# References
[1] Rasmussen, R., O’Donnell, J., Ding, F., & Nedergaard, M. (2020). Interstitial ions: A key regulator of state-dependent neural activity?. Progress in neurobiology, 193, 101802.

[2] Quintana, M. B., & Rangamani, P. (2023). Mechanical forces promote actin-mediated structural plasticity. Biophysical Journal, 122(3), 418a.
