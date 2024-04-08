---
title: 'Data-parallel based deep learning for the model order reduction of parametrized partial differential equations'
authors:
  - name: Nirav Vasant Shah
    affiliations:
      - University of Cambridge
    email: nvs31@cam.ac.uk
  - name: Chris Richardson
    affiliations:
      - University of Cambridge
    email:
  - name: Garth Wells
    affiliations:
      - University of Cambridge
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Parametrized partial differential equations are used to model problems in engineering. Design of engineering systems is governed by physical parameters such as material properties, boundary conditions and geometric parameters such as shape of the components. In order to rapidly explore the variation in quantity of interest with respect to the physical or geometrical parameters, model order reduction is used as a computationally faster alternative with an “affordable” compromise in accuracy.



Deep learning based model order reduction methods have gained traction in recent years. These methods can be non-intrusive in nature and may not require access to source code used to solve the high-fidelity model. In the case of offline-online two stage procedure, deep learning methods are quicker in the online phase. However, during the offline phase, they suffer from severe computational costs associated with generation of training data and training of artificial neural network. On exascale systems, such approaches require more careful numerical implementation due to heterogeneous mixed CPU/GPU devices.



In this talk, we will focus on problems involving geometric parameters. Further, we will introduce data-parallel distributed training of the artificial neural network in order to address the issue of high offline cost. We will also introduce PyTorch-RBniCSx-FEniCSx based open source package, DLRBniCSx, for deep learning based model order reduction.



Keywords: Geometric parameters, Model order reduction, Artificial neural network, Data-parallelism
