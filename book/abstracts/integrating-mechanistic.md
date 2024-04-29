---
title: 'Integrating Mechanistic Knowledge into Deep Learning for Improved Cancer Detection'
authors:
  - name: Christoph Sadee
    affiliations:
      - Stanford University
    email: sadee@stanford.edu
  - name: Katherine Hartmann
    affiliations:
      - University of Pennsylvania
  - name:  Alex Dils
    affiliations:
      - Stanford University
  - name: Ianto Xi
    affiliations:
      - University of Pennsylvania
  - name: Francisco Carrillo-Perez
    affiliations:
      - Stanford University
  - name: Ahmet Er Gorkem
    affiliations:
      - Stanford University
  - name: Stefano Testa
    affiliations:
      - Harvard University
  - name: Serena Zhang
    affiliations:
      - Stanford University
  - name: Olivier Gevaert
    affiliations:
      - Stanford University
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Deep learning requires large amounts of data. The ever-growing demand for more data represents a significant bottleneck. Many proposed solutions use AI based synthetic data to augment existing data, however these approaches have marked limitations. Here, we use mechanistic understanding of the human body to integrate physics-based models into a deep-learning model for lung tumor segmentation. We simulate lung deformation according to a natural breathing cycle using a finite element analysis of hyper elasticity with computed tomography (CT) of the chest from the publicly available LOTUS dataset (300 lung CTs) to increase the variation of existing data. This approach extends beyond current methods for data augmentation that are often based on simple spatial transformations (rotation, flipping, translation, and shear). Ultimately this approach serves as a case study of methods to integrate a-priori knowledge with AI.


# References
[1]	H. Sung et al., “Global Cancer Statistics 2020: GLOBOCAN Estimates of Incidence and Mortality Worldwide for 36 Cancers in 185 Countries,” CA. Cancer J. Clin., vol. 71, no. 3, pp. 209–249, 2021, doi: 10.3322/caac.21660.

[2]	H. Xue, Y. Yao, and Y. Teng, “Multi-modal tumor segmentation methods based on deep learning: a narrative review,” Quant. Imaging Med. Surg., vol. 14, no. 1, pp. 1122–1140, Jan. 2024, doi: 10.21037/qims-23-818.

[3]	A. Mansoor et al., “Segmentation and Image Analysis of Abnormal Lungs at CT: Current Approaches, Challenges, and Future Trends,” Radiogr. Rev. Publ. Radiol. Soc. N. Am. Inc, vol. 35, no. 4, pp. 1056–1076, 2015, doi: 10.1148/rg.2015140232.

[4]	Z. Ji et al., “Survey of Hallucination in Natural Language Generation,” ACM Comput. Surv., vol. 55, no. 12, p. 248:1-248:38, Mar. 2023, doi: 10.1145/3571730.

[5]	J. Wang et al., “Evaluation and Analysis of Hallucination in Large Vision-Language Models.” arXiv, Oct. 10, 2023. doi: 10.48550/arXiv.2308.15126.

[6]	A. R. Luca et al., “Impact of quality, type and volume of data used by deep learning models in the analysis of medical images,” Inform. Med. Unlocked, vol. 29, p. 100911, Jan. 2022, doi: 10.1016/j.imu.2022.100911.

[7]	S. M. T. I. Tonmoy et al., “A Comprehensive Survey of Hallucination Mitigation Techniques in Large Language Models.” arXiv, Jan. 08, 2024. doi: 10.48550/arXiv.2401.01313.

[8]	M. Heusel, H. Ramsauer, T. Unterthiner, B. Nessler, and S. Hochreiter, “GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium,” in Advances in Neural Information Processing Systems, Curran Associates, Inc., 2017. Accessed: Mar. 04, 2024. [Online]. Available: https://papers.nips.cc/paper_files/paper/2017/hash/8a1d694707eb0fefe65871369074926d-Abstract.html

[9]	S. Ravuri and O. Vinyals, “Classification Accuracy Score for Conditional Generative Models.” arXiv, Oct. 28, 2019. doi: 10.48550/arXiv.1905.10887.

[10]	S. Göktepe and E. Kuhl, “Electromechanics of the heart: A unified approach to the strongly coupled excitation-contraction problem,” Comput. Mech., vol. 45, pp. 227–243, Nov. 2010, doi: 10.1007/s00466-009-0434-z.

[11]	P. Afshar et al., “Lung-Originated Tumor Segmentation from Computed Tomography Scan (LOTUS) Benchmark.” arXiv, Jan. 02, 2022. Accessed: Mar. 04, 2024. [Online]. Available: http://arxiv.org/abs/2201.00458

[12]	“pydicom/pydicom.” DICOM in Python, Mar. 04, 2024. Accessed: Mar. 04, 2024. [Online]. Available: https://github.com/pydicom/pydicom

[13]	G. Bradski, The Opencv Library, vol. 25. 2000.

[14]	J. Wasserthal et al., “TotalSegmentator: Robust Segmentation of 104 Anatomic Structures in CT Images,” Radiol. Artif. Intell., vol. 5, no. 5, p. e230024, Sep. 2023, doi: 10.1148/ryai.230024.

[15]	A. Al-Mayah, J. Moseley, M. Velec, and K. Brock, “Toward efficient biomechanical-based deformable image registration of lungs for image-guided radiotherapy,” Phys. Med. Biol., vol. 56, no. 15, pp. 4701–4713, Aug. 2011, doi: 10.1088/0031-9155/56/15/005.

[16]	“FEniCS,” FEniCS Project. Accessed: Mar. 08, 2024. [Online]. Available: https://fenicsproject.org/

[17]	“Gmsh: a three-dimensional finite element mesh generator with built-in pre- and post-processing facilities.” Accessed: Mar. 08, 2024. [Online]. Available: https://gmsh.info/
