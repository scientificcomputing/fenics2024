---
title: 'Expressing general constitutive models using algorithmic automatic differentiation in DOLFINx'
authors:
  - name: Andrey Latyshev
    affiliations:
      - University of Luxembourg
    email: latyshev.andrey.a@gmail.com
  - name: Jérémy Bleyer
    affiliations:
      - Ecole des Ponts ParisTech
    email:
  - name: Jack S. Hale
    affiliations:
      - Sorbonne Université
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The Unified Form Language (UFL) (Alnaes et al., 2013) is a widely-used package for writing variational forms of partial differential equations. However, many notable solid mechanics problems cannot be naturally expressed in UFL e.g. complex plasticity and neural network constitutive models. This limitation has slowed the adoption of FEniCS in the solid mechanics community. In this talk we show a framework (Latyshev & Hale, 2024) for DOLFINx (Baratta et al., 2023) that enables the inclusion of arbitrary constitutive models using any third-party package that supports ndarray-like objects (e.g. JAX (Frostig et al., 2018), Numba (Lam et al., 2015) and others). We achieve this by leveraging three recent developments: the ExternalOperator extension of UFL (Bouziani & Ham, 2021), the new data-centric design in DOLFINx, and its automatic code generation for UFL Expressions. A key outcome of this work is the support for algorithmic automatic differentiation techniques in DOLFINx, demonstrated by implementing a non-associative plasticity model of Mohr-Coulomb type using forward-mode automatic differentiation in the JAX library.

# References
Alnæs, M. S., Logg, A., Ølgaard, K. B., Rognes, M. E., & Wells, G. N. (2014). Unified form language: A domain-specific language for weak formulations of partial differential equations. ACM Transactions on Mathematical Software, 40(2), 9:1-9:37. doi:10.1145/2566630

Baratta, I. A., Dean, J. P., Dokken, J. S., Habera, M., Hale, J. S., Richardson, C. N., Rognes, M. E., Scroggs, M. W., Sime, N., & Wells, G. N. (2023). DOLFINx: The next generation FEniCS problem solving environment. Zenodo. doi:10.5281/zenodo.10447666

Bouziani, N., & Ham, D. A. (2021). Escaping the abstraction: A foreign function interface for the Unified Form Language [UFL] (arXiv:2111.00945). arXiv. doi:10.48550/arXiv.2111.00945

Frostig, R., Johnson, M. J., & Leary, C. (2018). Compiling machine learning programs via high-level tracing. Systems for Machine Learning, 4(9). https://mlsys.org/Conferences/doc/2018/146.pdf

Lam, S. K., Pitrou, A., & Seibert, S. (2015). Numba: A LLVM-based Python JIT compiler. Proceedings of the Second Workshop on the LLVM Compiler Infrastructure in HPC, 1–6. doi:10.1145/2833157.2833162

Latyshev, A., & Hale, J. S. (2024). dolfinx-external-operator: V.0.0.1 (v0.0.1) [Computer software]. Zenodo. doi:10.5281/zenodo.10907418
