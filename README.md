# Tumor-Growth-Simulation

This project is a simulation for the evolution of a tumor based on it's `genetic code` using `reinforcement learning`. Tumors are abnormal masses of cells that develop on an organ or a specific tissue, require a blood supply to grow (in anatomical terms: angionesis) and can have a variable grow.

For this simulation, the `TumorEnv` class is used to initialize the tumor, the environment and the behavior (I also implemented the possibility to run many other simulations in parallel in the `runParallelSimulation() -> Simulation.py`). Each generated tumor will have it's own randomized genetic code and based on the pattern it can influence: density, growth rate, asymetry, heterogeneity (diversity) and the tissue type (it can have only one type: red - muscular type, blue - castilage-like, orange - organ tissue). The behavior is: new cells are added only near the existing ones, `blood vessels` are generated every new 10 cells, the tumor grows on an organ, `reinforcement learning` is used to explore different growth strategies. An example of a tumor:

![alt text](tumor.png)

The organ will be generated just as a sphere:

![alt text](organ.png)

Reinforcement Learning principles used: 
- the `RL agent` is the tumor
- the `RL environment` is defined in `TumorEnv`
- the available actions are: `normal growth` (balanced cell expansion), `rapid expansion` (aggressive tumor growth), `reduced growth` (cells multiply at a slower rate)
- `the reward` is proportional to the number of cells which motivates the tumor to grow.

The mathematical model is as follows:

1. Definitions and notation

The tumor is represented as a set of `spherical cells` of radius $r_i$ in a 3D space with the position $C_i = (x_i, y_i, z_i)$ and the whole structure at time step $t$ is a set $T(t) = \{ (C_1, r_1), (C_2, r_2),...,(C_n, r_n) \} $, where $n$ is the number of cells at time $t$.
The genetic traits: $density (d)$ influences how closely cells are packed, $growth rate (g)$ determines how fast new cells are added, $assymetry (a)$ controls random deviations in growth, $heterogeneity (h)$ determines variations in cell sizes.
RL components: $state S_t$ represents the tumor at time $t$ as $S_t = T(t)$, $action A_t$ from where the agent chooses an action: $A \in

NEED TO FINISH

![til](ezgif.com-video-to-gif-converter.gif)

Bibliographical references:
- Byrne, H. M. (2010). Dissecting cancer through mathematics: from the cell to the animal model. Nature Reviews Cancer, 10(3), 221-230
- Araujo, R. P., & McElwain, D. L. (2004). A history of the study of solid tumour growth: The contribution of mathematical modelling. Bulletin of Mathematical Biology, 66(5), 1039-1091
- Folkman, J. (1971). Tumor angiogenesis: therapeutic implications. New England Journal of Medicine, 285(21), 1182-1186
- Hanahan, D., & Weinberg, R. A. (2011). Hallmarks of cancer: the next generation. Cell, 144(5), 646-674
- Sutton, R. S., & Barto, A. G. (2018). Reinforcement Learning: An Introduction (2nd Edition). MIT Press
- Silver, D., et al. (2017). Mastering the game of Go without human knowledge. Nature, 550(7676), 354-359
- Esteva, A., et al. (2017). Dermatologist-level classification of skin cancer with deep neural networks. Nature, 542(7639), 115-118
- Ciresan, D. C., et al. (2012). Deep neural networks segment neuronal membranes in electron microscopy images. Advances in Neural Information Processing Systems (NeurIPS), 2852-2860
- Tracqui, P. (2009). Biophysical models of tumour growth. Reports on Progress in Physics, 72(5), 056701
- Altrock, P. M., Liu, L. L., & Michor, F. (2015). The mathematics of cancer: integrating quantitative models. Nature Reviews Cancer, 15(12), 730-745
