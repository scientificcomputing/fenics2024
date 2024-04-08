---
title: 'A Monolithic Approach to Vibro-Acoustic Coupling Across Non-Conformal Mesh Interfaces'
authors:
  - name: Antonio Baiano Svizzero
    affiliations:
      - Undabit
    email: antonio.bs@undabit.com
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

In the frequency domain of vibro-acoustics, the mesh size is primarily dictated by the minimum wavelength of waves in the material. It's common for the wavelengths to vary significantly once the maximum frequency of analysis and the material characteristics are established. If mesh interfaces need to be conformal, the larger mesh (usually the fluid one) needs refinement at the interface, increasing the total number of nodes. In this article, FEniCSx was used to assemble the subsystem matrices, which have been integrated with a special interpolation matrix to accommodate non-conformal meshes. This makes FEniCSx to a level of performance comparable with that of most commercial software, offering a robust and efficient solution for complex vibro-acoustic simulations.
