---
title: "DOLFINx and FFCx on Amazon’s Graviton3"
authors:
  - name: Michal Habera
    affiliations:
      - Rafinex Sarl
    email: mail@jackhale.co.uk
  - name: Jack S. Hale
    affiliations:
      - University of Luxembourg
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

We discuss performance results from executing the FEniCS Project finite element software on Amazon Web Services (AWS) systems with ARM64-based Graviton3(e) processors (Habera and Hale, 2023). We show both weak scaling tests across nodes and explore the auto-vectorisation capabilities of the latest clang and GCC compilers on FFCx generated kernels.

# References
Habera, M., Hale, J. S., 2023. The FEniCS Project on AWS Graviton3. Preprint. https://hdl.handle.net/10993/55560
