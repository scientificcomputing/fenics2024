---
title: 'Leveraging DOLFINx data-oriented design for GPU implementation'
authors:
  - name: Adeeb Arif Kor
    affiliations:
      - University of Cambridge
    email: adeebkor@gmail.com
  - name: Igor Baratta
    affiliations:
      - University of Cambridge
    email:
  - name: Garth N. Wells
    affiliations:
      - University of Cambridge
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The data-oriented design choice adopted by DOLFINx offers several advantages. One such benefit is the ease of implementing kernels that can run on both CPU and GPU architectures. In this presentation, we discuss our efforts in implementing the mass and stiffness kernel on the GPU. Utilizing the Numba CUDA interface, we demonstrate how the data-oriented design simplifies the implementation process for GPU acceleration. Furthermore, we present performance results to illustrate the efficiency of our implementation, despite its simplicity. Specifically, using a benchmark problem in transcranial ultrasound simulation, we showcase comparable performance achieved on a modest GPU architecture compared to a single node on an HPC architecture.
