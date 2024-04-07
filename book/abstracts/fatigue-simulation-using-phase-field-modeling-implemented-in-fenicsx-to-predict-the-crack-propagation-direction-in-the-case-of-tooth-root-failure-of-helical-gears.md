---
title: 'Fatigue simulation using phase-field modeling implemented in FEniCSx to predict the crack propagation direction in the case of tooth root failure of helical gears'
authors:
  - name: Daniel Martini
    affiliations:
      - German Aerospace Center (DLR)
    email: daniel.martini@dlr.de
  - name: Lisa Reischmann
    affiliations:
      - German Aerospace Center (DLR)
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The concept of geared turbofans has proven to significantly increase the efficiency of aero engines. The idea of this concept is to decouple fan and low pressure turbine by a planetary gearbox. To show airworthiness of such a planetary gearbox, the containment of failing gears has to be ensured, which is only possible, when bursting of high energy parts is avoided. Bursting of planetary gears may occur, when gear tooth root cracks propagate towards the shaft. Consequently, the crack path of fatigue cracks at the tooth root needs to be predicted correctly. In this talk, we present an approach to predict crack paths originating from gear tooth roots, which is implemented in FEniCSx and which is based on phase-field modeling of fatigue. To reduce the computational costs and speed up the numerical simulations, the phase-field model is just applied to a sector-shaped sub-model, which is driven by a global gear model. Furthermore, a cycle jump technique is incorporated to extrapolate history variables related to phase-field modeling of fatigue. Additionally, the mechanical loading of gears, that is centrifugal and gear line loads need to be applied within the FEniCSx-framework. Furthermore, initial numerical simulations are shown which illustrate possible influences on the crack propagation direction.
