---
title: 'How to evaluate wall shear stress?'
authors:
  - name: Jana Brunátová
    affiliations:
      - Charles University
      - University of Groningen
    email: brunatova@karlin.mff.cuni.cz
  - name: Jaroslav Hron
    affiliation: Charles University
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Hemodynamic risk factors such as wall shear stress (WSS) are increasingly being considered in medical decision-making concerning the treatment of cerebral aneurysms. Studying these quantities plays a vital role in improving our understanding of the mechanisms that cause aneurysm growth or rupture, as well as in predicting the risk of rupture. However, there is still a lack of consensus and standardized methods for evaluating hemodynamic quantities within the community. Improving the accuracy of the methods by which these quantities are evaluated could lead to significant differences when compared to commonly used methods, thereby potentially impacting medical decision-making. The aim of this work is to propose and compare several WSS evaluation methods and report the differences among them.

WSS is the most frequently studied hemodynamic quantity; however, its numerical evaluation is not straightforward. We restrict our attention to evaluations based on the finite element method, as our computational code utilises the FEniCS library with a solver from the PETSc library. First, we compute fluid flow (in a rigid impermeable domain) by solving the incompressible Navier–Stokes equations. Subsequently, we evaluate WSS for several choices of finite element spaces, namely DG0, DG1, and CG1. Moreover, we propose a new method for WSS evaluation, formulated as a boundary-flux evaluation problem. All methods are first compared on a Poiseuille flow benchmark with known WSS before being further tested on general 3D geometries. Our results suggest that the proposed boundary-flux evaluation method can improve the accuracy of WSS for suitable choices of finite element spaces, namely the DG0 and CG1. Using a patient-specific geometry, we observed notable differences in WSS depending on the size of elements (particularly near the boundary) and on the choice of finite element spaces. Caution should be exercised when evaluating the WSS numerically.
