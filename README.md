# eco-dqn
[![Generic badge](https://img.shields.io/badge/arXiv-1909.04063-<COLOR>.svg)](https://arxiv.org/abs/1909.04063)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](./LICENSE)

---

Implementation of ECO-DQN as reported in ["Exploratory Combinatorial Optimization with Reinforcement Learning"](https://arxiv.org/abs/1909.04063).

---

## Requirements

Beyond standard packages found in most Python distributions (e.g. numpy, matplotlib etc), this project requires:

- pytorch
- networkx
- numba
- pandas

Alternatively, the included [``environment.yml``](environment.yml) file will produce a working environment called ``spin-solver``.

    >>> git clone --recursive https://github.com/tomdbar/eco-dqn
    >>> cd eco-dqn
    >>> conda env create -f environment.yml (<-- optional)
    >>> source active spin-solver (<-- optional)

## Running experiments

*Scripts to reproduce the agents trained in the paper can be found in the [``experiments``](experiments) folder.  It is straightforward to modify these to use different training/testing data or parameters.*

##### Reproducing ECO-DQN agents and tests

We train agents on two different types of graph called Erdos-Renyi (ER) and Barabasi-Albert (BA).  For each graph type we train the agents on 20, 40, 60, 100, 200 and 500 vertex graphs. *Note the code typically refers to a ***vertex*** as a ***spin***.*

Training these agents can be reproduced by running the corresponding scripts. *Replace ER_20spin below with the appropriate folder for different agents.*

    >>> cd eco-dqn
    >>> python -m experiments.ER_20spin.train.train_eco


The creates a directory ``ER_20spin/eco/network`` to store following.
- The network parameters at various points over training and of the fully trained agent.
- The test scores over training, as a .pkl file and plotted.
- The loss over training, as a .pkl file and plotted.

Agents are then typically tested on graphs of the same type of the same or greater size.  To test an agent, presuming the training script has already been run, simply use:

    >>> cd eco-dqn
    >>> python -m experiments.ER_20spin.test.test_eco
 
*Edit these scripts to only test on a subset of possible graph sizes if desired.*
    
This creates a directory ``ER_20spin/eco/data`` to store following for every graph size tested on.
- The averaged results, summarized in a pandas dataframe and saved to ``results_xxx.pkl``.
- The raw results on each graph, summarized in a pandas dataframe and saved to ``results_xxx_raw.pkl``.
- The full history of every test episode, saved to ``results_xxx_histories.pkl``.

Alternativley, the agent can be trained and tested with a single script.

    >>> cd eco-dqn
    >>> python -m experiments.ER_20spin.train_and_test_eco
    
##### Testing pre-trained agents

A script to test pre-trained agents on different graph sets is provided in [``experiments/pre_trained_agent/test_eco.py``](experiments/pretrained_agent/test_eco.py). Simply edit the ``network_save_loc`` and ``graph_save_loc`` parameters to point at the desired agent and test_graphs.  Moreover, the pretrained agents as produced for the paper can be found in [``experiments/pre_trained_agent/networks/eco/``](experiments/pre_trained_agent/networks/eco).
    
##### Reproducing S2V-DQN agents and tests
    
S2V-DQN is a framework origionally proposed by [Khalil *et al*](https://arxiv.org/abs/1704.01665) which we reimplemented to use the same network architecure as ECO-DQN.  As such, for every training and test script above, the equivalent S2V-DQN script can be ran by replacing ``*_eco --> *_s2v``.

*Please note this is our implementation of S2V-DQN, however the original repository is provided by Hanjun Dai [here](https://github.com/Hanjun-Dai/graph_comb_opt).*
    
## Repository contents

##### [**_graphs**](_graphs)

Contains the graph instances used in the paper.  This is split into three catagories:
- [``benchmarks``](_graphs/benchmarks): The known benchmarks tested on in the paper.  Specifically G1-G10 (800 vertices) and G22-G32 (2000 vertices) from the GSet, along with the "Physics" (125 vertex) dataset.
- [``testing``](_graphs/testing): Sets of 50 graphs for each graph type and size.  These are the graphs against which the agents are tested during training.
- [``validation``](_graphs/validation):  Sets of 100 graphs for each graph type and size.  These are the graphs on which the performances of trained agents are tested.

Within each of these sub-folders, the ``opts/`` folder contains the "optimum" solutions/values (best known for the benchmarking graphs, and the best found by any of our optimization methods as described in the supplemental material of the paper for testing and validation graphs).

The graph sets themselves are .pkl files that un-pickle to be list graphs.  Ultimately, the code wants these as a list of numpy arrays, however the ``load_graph_set(...)`` function in [``experiments/utils.py``](experiments/utils.py) will also convert lists of either networkx graphs or scipy sparse matrices into the correct form (these are more memory efficient ways of storing large graphs).  If you wish to point the code at custom sets of graphs, they should match one of these formats and be appropriately stored in a .pkl file.

##### [experiments](experiments)

Described above.

##### [**src**](src)

Contains source code for ECO-DQN.  This consists of three directories which, at a very high level are:
- [``agents``](src/agents): Contains the [DQN](src/agents/dqn) agent trained, along with classes to solve graphs using either a trained agent or a greedy heuristic.
- [``envs``](src/envs): Contains the environment for tacking combinatorial optimisation over a graph in an RL-framework.
- [``networks``](src/networks): Contains the Q-network used for ECO-DQN.  This is a form of Message Passing Neural Network (MPNN) as first introduced by [Gilmer *et al*](https://arxiv.org/abs/1704.01212).

## Reference

If you find this work or the associated paper useful, it can be cited as below.

    @article{barrett2019exploratory,
      title={Exploratory Combinatorial Optimization with Reinforcement Learning},
      author={Barrett, Thomas D and Clements, William R and Foerster, Jakob N and Lvovsky, AI},
      journal={arXiv preprint arXiv:1909.04063},
      year={2019}
    }
