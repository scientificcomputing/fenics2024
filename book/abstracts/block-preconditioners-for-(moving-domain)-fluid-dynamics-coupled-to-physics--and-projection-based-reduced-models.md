---
title: 'Block Preconditioners for (Moving Domain) Fluid Dynamics Coupled to Physics- and Projection-based Reduced Models'
authors:
  - name: Marc Hirschvogel
    affiliations:
      - id: mox
        institution: MOX, Dipartimento di Matematica, Politecnico di Milano
        city: Milan
        country: Italy
    email: marc.hirschvogel@ambit.net
  - name: Maximilian Balmus
    affiliations:
      - id: tric
        institution: TRIC-DT, The Alan Turing Institute, National Heart and Lung Institute, Imperial College London
        city: London
        country: UK
  - name: Mia Bonini
    affiliation: michbio
  - name: David Nordsletten
    affiliations:
      - id: michbio
        institution: Department of Biomedical Engineering, University of Michigan
        city: Ann Arbor
        country: USA
      - id: michcar
        institution: Department of Cardiac Surgery, University of Michigan
        city: Ann Arbor
        country: USA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Models of patient-specific cardiovascular fluid flow play a central role in many biomedical engineering applications, and modeling the adaptive interplay between blood and vessel walls is highly relevant but remains challenging. To efficiently construct models of the (3-dimensional, 3D) region of interest, be it the heart cavities or the aorta, model reduction techniques are commonly applied to adjacent portions of the vascular system whose detailed spatial representation may not be decisive for modeling their influence. These encompass lumped-parameter flow models (0-dimensional, 0D) that account for the up- or downstream vascular system pressures, or wall models (reduced-dimensional, RD) that mimic the active and elastic behavior, circumventing the need to perform full fluid-solid interaction (FSI) simulations.The coupling of distributed (3D) and reduced (0D/RD) models, however, can pose additional challenges to solvers, especially when 3D and 0D/RD are strongly interlinked and necessitate a monolithic solution scheme in order to be solved stably. We leverage a recently proposed 3D-RD-0D model of cardiac hemodynamics, denoted as fluid-reduced-solid interaction (FrSI), where elastic vessel wall features are included by means of a physics- and projection-based model reduction approach. For this purpose, we develop a 3x3 block preconditioning strategy that allows to split Navier-Stokes into bulk and RD vessel wall degrees of freedom, enabling any reduced models to be treated with a direct solve due to their comparatively small dimension. Operators associated to bulk velocity and the approximate Schur complement are addressed by applying an algebraic multigrid preconditioner.The solver is demonstrated for a large-scale model of patient-specific FrSI in the left heart as well as rigid-wall CFD in arteries coupled to 0D models, demonstrating superiority compared to 2x2 block approaches where 0D variables are merged to the fluid pressure space.
