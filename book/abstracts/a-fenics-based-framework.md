---
title: 'A FEniCS-based framework for modeling cardiac growth and remodeling'
authors:
  - name: Karl Munthe
    affiliations:
      - id: simula
        institution: Simula Research Laboratory
    email: karlfredrik@simula.no
  - name: Henrik Finsberg
    affiliation: simula
  - name: Samuel Wall
    affiliation: simula
  - name: Joakim Sundnes
    affiliation: simula
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Computational models of growth and remodelling have the potential to pro-
vide important understanding of fundamental biological processes, and can also
have direct clinical utility, for instance to predict disease trajectories in pro-
gressive heart disease. Most computational models of soft tissue growth have
been based on the volumetric growth framework of Rodriguez et al. [RHM94],
which splits the overall deformation of the tissue in two parts; a non-elastic
deformation resulting from the growth, and an elastic deformation, ensuring
continuity of the tissue and compatibility with given boundary conditions. The
actual growth is typically driven by either stress or strain, and is described by
a phenomenologically derived constitutive law. A large number of such growth
laws have been proposed, but they have rarely been systematically evaluated or
compared to each other. One notable exception was provided by Witzenburg
and Holmes [WH18], who performed a systematic evaluation of a set of growth
laws for cardiac tissue. The growth models were compared for simplified defor-
mation patterns that enabled collapsing the governing equations into algebraic
relations, eliminating the need to solve partial differential equations with the
finite element method. In the present work we have developed a computational
pipeline for comparing growth model in a more general and flexible setting.
The pipeline is based on a finite element solver implemented in FEniCS, which
solves a generic growth model defined by Cauchy’s equation of motion and the
volumetric growth framework. Any growth model can be combined with any
hyperelastic material law, as well as an arbitrary geometry and boundary condi-
tions. The framework will enable comparing existing and proposed growth laws
in a more realistic setting than what is currently possible. This will illuminate
the respective models relative strengths and weaknesses.

# References
[RHM94] Edward K Rodriguez, Anne Hoger, and Andrew D Mcculloch. STRESS-DEPENDENT FINITE GROWTH IN SOFT ELASTIC TISSUES. 1994.

[WH18] Colleen M. Witzenburg and Jeffrey W. Holmes. “Predicting the time course of ventricular dilation and thickening using a rapid compart- mental model”. In: Journal of Cardiovascular Translational Research 11 (2 Mar. 2018), pp. 109–122. issn: 19375395. doi:10.1007/s12265-018-9793-1.
