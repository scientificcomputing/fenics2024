---
title: 'Automated optimisation of Stellarator configurations '
authors:
  - name: Massimiliano Leoni
    affiliations:
      - Proxima Fusion
    email: mleoni@proximafusion.com
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Stellarators are (momentarily) a futuristic approach to fusion power plants that must confine a 100 million degree plasma, while confining high energy particles, extracting heat, ensuring tritium self-sufficiency, refueling the core and - worth mentioning - making that clean energy dream last for more than a nanosecond. These extremely complex machines require careful design taking decades xor a fully automated pipeline that can iterate through several designs in an optimization loop. And at Proxima Fusion we ain't gonna wait decades.

In this presentation I'll discuss part of our integrated optimization pipeline which relies on, you guessed it, FEniCS-X for the simulation of thermal diffusion in the first wall, a crucial component of the design process.
