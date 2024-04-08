---
title: 'Towards identification of material parameters of fibre-reinforced polymers through digital volume correlation and micro-mechanical simulations with FEniCSx.'
authors:
  - name: Edgar Rios
    affiliations:
      - KU Leuven
    email: edgar.rios@kuleuven.be
  - name: Christian Breite
    affiliations:
      - KU Leuven
    email:
  - name: Mahoor Mehdikhani
    affiliations:
      - KU Leuven
    email:
  - name: Yentl Swolfs and Martin Diehl
    affiliations:
      - KU Leuven
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Fibre-reinforced polymers (FRP) have a good balance between strength, toughness, weight, corrosion resistance, formability and price. They are used in vehicles, wind turbines, buildings and other applications¹. Currently, their weight-saving advantage is partly mitigated by a lack of confidence in the prediction of their mechanical behaviour². This can be improved with the use of virtual testing frameworks, which would facilitate simulations of hierarchical FRP architectures at different scale-lengths. However, such frameworks rely on the understanding of the materials’ micromechanics³. Thus, the goal here is to improve the accuracy of the models by advancing characterisation.

The required identification of constitutive parameters in this process⁴ is frequently based on inverse simulations using experimental results to construct an objective function. The progress in image analysis now allows such a function to be linked to full fields of deformation from digital volume correlation (DVC) of micro- and nano X-ray tomography. This information can then be used to adjust the parameters of micro-mechanical models by computer-based simulations⁵,⁶. Ultimately, a full field of deformation from DVC and finite element analysis would be compared to determine in-situ parameters of micro-mechanical models of FRP.

To study the feasibility of the approach, optimisation based on genetic algorithms and gradient-descent is applied on synthetic FRP microstructures to find the parameters of a softening model⁸ for the polymer matrix. The in-house modelling of the constitutive behaviour is based on the NewFrac, dolfinx_materials and fenics-constitutive projects⁸–¹⁰. FEniCSx 0.8.x¹¹–¹³ is used to generate the target deformation, and SciPy provides the optimisation framework that drives FEniCSx simulations to seek for the optimal parameters. The results show that the combination of full-field DVC and simulations provides a mean for parameter identification of in-situ properties of FRP.

# References
1.	B. Harris. Fatigue in composites. 2003. isbn: 9781855736085.

2.	C. Breite. “Aligning Fibre Break Models for Composites with the Observable Micro-Scale Material Behaviour”. 2021.

3.	S. Huang et al. “Characterization of interfacial properties between fibre and polymer matrix in composite materials - A critical review”. J. Mater. Res. Technol. 2021 https://doi.org/10.1016/j.jmrt.2021.05.076.

4.	J. Chevalier. “Micromechanics of an epoxy matrix for fiber reinforced composites: experiments and physics-based modelling”. 2018.

5.	A. Buljac et al. “Digital Volume Correlation: Review of Progress and Challenges”. Exp. Mech. 2018. https://doi.org/10.1007/s11340-018-0390-7.

6.	B. P. Croom et al. “Damage mechanisms in elastomeric foam composites: Multiscale X-ray computed tomography and finite element analyses”. Compos. Sci. Technol. 2019. https://doi.org/10.1016/j.compscitech.2018.11.025.

7.	T. Titscher, J. Oliver, and J. F. Unger. “Implicit-explicit integration of gradient-enhanced damage models”. J. Eng. Mech. 2019. https://doi.org/10.1061/(ASCE)EM.1943-7889.0001608.

8.	J. Bleyer. dolfinx_materials. Ver: 8cef2944. Laboratoire Navier, Ecole des Ponts ParisTech, 2024. https://github.com/bleyerj/dolfinx_materials.

9.	J. Hale, C. Maurini, and A. Latyshev. Computational fracture mechanics examples with FEniCSx. Ver: de88e30. 2020. https://gitlab. com/newfrac/newfrac-fenicsx-training.

10.	J. Bleyer. Numerical tours of Computational Mechanics with FEniCSx. Ver: v0.1. 2024. https://doi.org/10.5281/zenodo.10470942.

11.	M. S. Alnaes et al. “Unified Form Language: A domain-specific language for weak formulations of partial differential equations”. ACM Trans. on Math. Softw. 2014. https://doi.org/10.1145/2566630.

12.	M. W. Scroggs et al. “Basix: a runtime finite element basis evaluation library”. J. Open Source Softw. 2022. https://doi.org/10.21105/joss.03982.

13.	M. W. Scroggs et al. “Construction of arbitrary order finite element degreeof-freedom maps on polygonal and polyhedral cell meshes”. ACM Trans. on Math. Softw. 2022. https://doi.org/10.1145/3524456.
