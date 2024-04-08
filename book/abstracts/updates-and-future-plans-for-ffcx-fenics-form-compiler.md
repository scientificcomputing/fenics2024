---
title: 'Updates and future plans for ffcx FEniCS Form Compiler'
authors:
  - name: Chris Richardson
    affiliations:
      - University of Cambridge
    email: cnr12@cam.ac.uk
  - name: Igor Baratta
    affiliations:
      - NVIDIA
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The FEniCS form compiler, ffcx, converts symbolic language (ufl) into code that can be compiled on a CPU, currently in "C". As hardware and software requirements change over time, ffcx needs to be updated to meet the new challenges that arise. As part of this, we have changed the internal language representation to be more agnostic of the output, so we can output in other languages, such as Python, C++, or even Rust perhaps. GPUs also present a challenge for software engineers: can we output suitable kernels, perhaps in smaller chunks to process finite element kernels more efficiently? How can we effectively use shared memory on these devices? We will try to answer some of these questions in this presentation.
