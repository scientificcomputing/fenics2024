---
title: 'Implementation in FEniCS of a cellular activity model based on damage theory'
authors:
  - name: Pedro José Diaz Guerrero
    affiliations:
      - Universidad Industrial de Santander
    email: pjdiaz@uis.edu.co
  - name: Javier Navarro Rueda
    affiliations:
      - Pontificia  Universidad Javeriana
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Implementation in FEniCS of a cellular activity model based on damage theory
 
Diaz, P. J.,  Navarro, J.  Suárez, D. R. 
 
Living musculoskeletal tissues, unlike traditional engineering materials, undergo processes of remodeling, repair, or adaptation (Martin et al., 2015). In bone, those processes are given  in response to mechanical loading and/or cellular activity. This ability results in a controlled degradation of material properties in each loading cycle when the patient is in good health, reflecting the occurrence of physical phenomena regulated by biological respons (Oumghar et al., 2020). As such, differences in the degradation of mechanical properties of bone may be associated with various biological responses. For example, mechanical fatigue could lead to eventual fracture due to imbalances between the concentrations of microdamage and the activation of cellular remodeling processes (García-Aznar et al., 2005).
 
This work implements FEniCS into a cellular activity model capable of simulating the coupled effect of the biological remodeling process of bone and the potential occurrence of fractures through growth and repair of microdamage due to mechanical loads. This model takes into account the adaptation of the internal bone structure in terms of bone volume fraction, level of damage, and degree of mineralization.
 
The model is developed based on the geometry derived from anonymized computed tomography (CT) scans, which have been segmented and voxelized to convert Hounsfield Unit values to bone density. A new domain has been constructed and generated, containing bone information of an 86-year-old male patient who has suffered an intratrocanteric fracture. The model aims to explain how the increase and cumulative effect of fatigue, along with events occurring in the process of bone remodeling such as focal bone balance and degree of mineralization, may lead to degradation of mechanical properties under specific dynamic loading conditions.

# References
García-Aznar, J. M., Rueberg, T., & Doblare, M. (2005). A bone remodelling model coupling microdamage growth and repair by 3D BMU-activity. Biomechanics and Modeling in Mechanobiology, 4(2–3), 147–167. doi:10.1007/s10237-005-0067-x

Martin, R. B., Burr, D. B., Sharkey, N. A., & Fyhrie, D. P. (2015). Mechanical Adaptability of the Skeleton. In Skeletal Tissue Mechanics (pp. 275–354). Springer New York. doi:10.1007/978-1-4939-3002-9_6

Ait Oumghar, I., Barkaoui, A., & Chabrand, P. (2020). Toward a Mathematical Modeling of Diseases’ Impact on Bone Remodeling: Technical Review. Frontiers in Bioengineering and Biotechnology, 8. doi:10.3389/fbioe.2020.584198
