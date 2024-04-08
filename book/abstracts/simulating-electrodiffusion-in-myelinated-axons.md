---
title: 'Simulating electrodiffusion in myelinated axons'
authors:
  - name: Alessandro Gatti
    affiliations:
      - id: uio
        institution: Department of Informatics, University of Oslo
        country: Norway
    email: alessandrog@simula.no
  - name: Pietro Benedusi
    affiliations:
      - id: euler
        institution:  Euler Institute, Università della Svizzera italiana
        country: Switzerland
  - name: Simone Pezzuto
    affiliations:
      - id: trento
        institution: Department of Mathematics, University of Trento
        country: Italy
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

In the context of computational neuroscience, we study the propagation of electrical signals in myelinated axons. In particular, using 3D simulations in realistic geometries, we address how demyelinating diseases, which cause damage to myelin sheaths such as retraction or thinning, affect the speed of nerve impulses.

In the context of computational electrophysiology, the EMI (Extra-Membrane-Intra) framework can be used to simulate excitable tissues at the cellular scale, with an explicit representation of membrane geometries. EMI problems are composed of two differential problems describing the evolution of extracellular and intracellular potentials, coupled at the cellular membrane via Robin-type conditions. To include membrane currents, we consider a Hodgkin-Huxley model in the Ranvier nodes of the axon. Moreover, since ion concentration gradients are crucial in membrane dynamics, we also consider the Kirchhoff-Nernst-Planck (KNP-EMI) model, a system of time-dependent nonlinear PDEs, extending the EMI model by including electrodiffusion of ions.

We numerically solve the EMI and KNP-EMI equations using the finite element method and tailored iterative solution strategies, allowing to handle large realistic 3D geometries.
Simulations confirm the theory that myelination enhances the speed of action potential propagation. In addition, a study of ephaptic coupling is presented by comparing myelinated and unmyelinated axon bundles. The results demonstrate that ephaptic coupling is feasible in both scenarios, with myelination accelerating the propagation of subsequent action potentials.
