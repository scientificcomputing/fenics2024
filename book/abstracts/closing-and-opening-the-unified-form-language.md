---
title: 'Closing and opening the Unified Form Language'
authors:
  - name: David A. Ham
    affiliations:
      - Imperial College London
    email: David.Ham@Imperial.ac.uk
  - name: Nacime Bouziani
    affiliations:
      - Imperial College London
    email:
  - name: India Marsden
    affiliations:
      - University of Oxford
    email:
  - name: Reuben W. Nixon-Hill
    affiliations:
      - Imperial College London
    email:
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The Unified Form Language underpins the user interfaces and code generation frameworks of Firedrake, FEniCS and some other finite element tools. The interface and capabilities of the language were mostly stable for many years after the publication of Alnæs et al (2014). However, a number of significant extensions to the language have been merged over the last year or so. These change the language in two distinct, but related, ways.

The first set of extensions, centred on dual spaces and cofunctions, attempt to close the language. In other words, operations, such as finite element assembly, which take UFL as an input should also produce UFL as outputs. Doing so enables composability: the ability of users to assemble complex calculations from the core UFL building blocks. The direct consequence of this is that operators that act on assembled objects, such as preconditioners, become much more cleanly representable in UFL.

The converse idea to that of closure is that operators which act on UFL objects and return UFL objects should themselves be representable as UFL objects. Due to the mathematical properties of the adjoint, this functionality strongly depends on cofunctions and dual spaces. The most fundamental such operator interpolation into a finite element space, which is now available as a UFL operator. The adjoint to this operation enables point forcing to be directly represented in UFL. Taking this further, UFL now contains a foreign function interface that enables users to include any differentiable operation between finite element spaces in the UFL language. This in particular facilitates including neural networks as operators inside a UFL form.

In this presentation I will outline these recent extensions to UFL, and provide the mathematical background to their definitions.

# References
Martin S. Alnæs, Anders Logg, Kristian B. Ølgaard, Marie E. Rognes, and Garth N. Wells. 2014. Unified form language: A domain-specific language for weak formulations of partial differential equations. ACM Trans. Math. Softw. 40, 2, Article 9 (February 2014), 37 pages. doi:10.1145/2566630
