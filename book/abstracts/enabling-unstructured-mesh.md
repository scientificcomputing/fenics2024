---
title: 'Enabling unstructured-mesh computation on massively tiled AI processors: An example of accelerating in silico cardiac simulation'
authors:
  - name: Luk Burchard
    affiliations:
      - Simula Research Laboratoy
    email: langguth@simula.no
  - name: Kristian Gregorius Hustad
    affiliations:
      - Simula Research Laboratoy
    email:
  - name: Johannes Langguth
    affiliations:
      - Simula Research Laboratoy
    email:
  - name: Xing Cai
    affiliations:
      - Simula Research Laboratoy
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

A new trend in processor architecture design is the packaging of thousands of small processor cores into a single device, where there is no device-level shared memory but each core has its own local memory. Thus, both the work and data of an application code need to be carefully distributed among the small cores, also termed as tiles. In this paper, we investigate how numerical computations that involve unstructured meshes can be efficiently parallelized and executed on a massively tiled architecture. Graphcore IPUs are chosen as the target hardware platform, to which we port an existing monodomain solver that simulates cardiac electrophysiology over realistic 3D irregular heart geometries. There are two computational kernels in this simulator, where a 3D diffusion equation is discretized over an unstructured mesh and numerically approximated by repeatedly executing sparse matrix-vector multiplications (SpMVs), whereas an individual system of ordinary differential equations (ODEs) is explicitly integrated per mesh cell. We demonstrate how a new style of programming that uses Poplar/C++ can be used to port these commonly encountered computational tasks to Graphcore IPUs. In particular, we describe a per-tile data structure that is adapted to facilitate the inter-tile data exchange needed for parallelizing the SpMVs. We also study the achievable performance of the ODE solver that heavily depends on special mathematical functions, as well as their accuracy on Graphcore IPUs. Moreover, topics related to using multiple IPUs and performance analysis are addressed. In addition to demonstrating an impressive level of performance that can be achieved by IPUs for monodomain simulation, we also provide a discussion on the generic theme of parallelizing and executing unstructured-mesh multiphysics computations on massively tiled hardware, and discuss the implications for future scientific computing.
