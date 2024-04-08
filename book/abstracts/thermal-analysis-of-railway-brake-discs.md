---
title: 'Thermal analysis of railway brake discs'
authors:
  - name: Yanjun Zhang
    affiliations:
      - KTH Royal Institute of Technology
    email: yanjunzh@kth.se
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The paper focuses on the application of FeniCSx for the thermal analysis of railway brake discs. The transient heat transfer equation is solved with multiple Neumann boundary conditions.

Railway brake discs convert the kinetic energy of rail vehicles into thermal energy to achieve braking. This thermal energy reduces the coefficient of friction and induces thermal cracks. It is therefore important to conduct the thermal analysis of the brake discs. Most commercial software is time-consuming and has many constraints, so we use FeniCSx to build a finite element method (FEM) based, three-dimensional (3D) transient thermal model.

Since the brake disc is rotating during braking, multiple Neumann boundary conditions (heat flux) are implemented. We compare the temperatures of the brake discs with different contact areas, which are affected by the wear and thermal expansion of the brake pads. The results are compared with experimental data from a full-scale test rig. The next step is to build the elasticity model of the brake pad, which gives information about wear and deformation in the contact area. Later, the convection heat coefficient can be calculated through the Navier-stokes equation. Then a full thermo-mechanical-fluid model is built up.
