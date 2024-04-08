---
title: 'SimCardEMS: A cardiac electro-mechanics solver designed for in silico trials'
authors:
  - name: Cécile Daversin-Catty
    affiliations:
      - Simula Research Laboratory
    email: cecile@simula.no
  - name: Henrik N. Finsberg
    affiliations:
      - Simula Research Laboratory
    email:
  - name: Ilsbeth van Herck
    affiliations:
      - Mimiro AS
    email:
  - name: Jørgen S. Dokken
    affiliations:
      - Simula Research Laboratory
    email:
  - name: Samuel Wall
    affiliations:
      - Simula Research Laboratory
    email:
  - name: Hermenegild Arevalo
    affiliations:
      - Simula Research Laboratory
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The utilization of in silico tools is increasingly essential in advancing the development of novel drugs and devices aimed at combating heart diseases. Nevertheless, the establishment of reliable and efficient models of the cardiovascular system remain challenging, given its strongly coupled multi-physics nature.

We present SimCardEMS, a fully-coupled cardiac electro-mechanics solver that combines electrophysiology and continuum mechanics bidirectionally, based on a collection of open-source FEniCS based software. In contrast to commonly utilized forward-coupled models, our solver incorporates the influence of mechanical changes on the electrical behavior as a feedback within the electrophysiology ordinary differential equations.

We demonstrate the potential of SimCardEMS in predicting drug safety and efficacy through the computation of significant biomarkers targeting both aspects of the cardiac function together with the prediction of the resulting ECG signals.


# References
Finsberg et al., (2023). simcardems: A FEniCS-based cardiac electro-mechanics solver. Journal of Open Source Software, 8(81), 4753, doi:10.21105/joss.04753
