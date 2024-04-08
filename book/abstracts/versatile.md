---
title: 'Versatile large scale level set topology optimization using FEniCSx'
authors:
  - name: Murtaza Bookwala
    affiliations:
      - University of California San Diego
    email: mbookwala@ucsd.edu
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Topology optimization has emerged as a powerful method to design structures and systems with optimal material distribution, particularly in engineering applications. However, this comes at the expense of complexity and computational cost, as TO needs multiple iterations involving forward analysis, sensitivity calculations, and design updates. This iterative process also needs to be scalable, particularly to address practical, large-scale engineering problems. Existing large-scale topology optimization implementations often lack versatility, either constrained by specific physical phenomena or lacking modularity. To address these limitations, a novel framework for modular large-scale topology optimization, utilizing the level set method is introduced. This framework is structured with distinct modules dedicated to analysis, optimization, and level set method, thus enabling a versatile and adaptable approach. Leveraging FEniCSx for finite element analysis ensures physics-agnostic capabilities, broadening the applicability of the framework across various engineering domains. Most of the computation is distributed using MPI and hence, the code is massively parallelizable. Furthermore, strategies are proposed to optimize memory usage and reduce computational time, enhancing the efficiency of the optimization process.
Traditionally, topology optimization represents void regions with low-density elements to avoid re-meshing of the domain. However, in scenarios with low target volume fractions, this method can lead to increased matrix conditioning numbers and prolonged solve times. An alternative approach is presented, focusing on integrating and solving the bilinear form solely within the active domain. This targeted approach is akin to element removal and improves code efficiency by minimizing unnecessary computations in inactive regions. The framework offers a comprehensive solution to the challenges of large scale TO and enables effective engineering design processes.
