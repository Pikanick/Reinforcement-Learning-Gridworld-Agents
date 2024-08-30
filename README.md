# Reinforcement Learning Agents for Gridworld

## Overview
This repository contains Python implementations of reinforcement learning algorithms used to solve decision-making problems in the Gridworld environment. The project explores different methods, such as Value Iteration and Q-Learning, to optimize policies for both known and unknown Markov Decision Processes (MDPs). These algorithms are fundamental in developing intelligent agents that can learn and adapt to complex environments.

## Table of Contents
- [Introduction](#introduction)
- [Implemented Algorithms](#implemented-algorithms)
- [Files and Structure](#files-and-structure)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Introduction
In this project, we implement and compare different reinforcement learning algorithms to solve the Gridworld problem. The goal is to develop agents that can make optimal decisions under uncertainty by maximizing cumulative rewards.

## Implemented Algorithms
1. **Value Iteration**: A dynamic programming approach that computes the optimal policy by iteratively improving the value function.
2. **Q-Learning**: A model-free reinforcement learning algorithm that learns the optimal policy by interacting with the environment.
3. **Prioritized Sweeping Value Iteration**: An optimized version of value iteration that prioritizes updates based on the magnitude of their potential impact on the policy.

## Files and Structure
- `valueIterationAgents.py`: Contains the implementation of the Value Iteration agent.
- `qlearningAgents.py`: Contains the implementation of the Q-Learning agent.
- `analysis.py`: Includes the analysis of different scenarios and configurations for reinforcement learning in Gridworld.
- `mdp.py`: Defines the structure and methods for general Markov Decision Processes (MDPs).
- `learningAgents.py`: Defines base classes for reinforcement learning agents.
- `gridworld.py`: The Gridworld environment implementation.
- `util.py`: Utility functions and data structures used by the agents.

For example, to test the Q-Learning agent, run:
```bash
python gridworld.py -a q -k 5
 ```
Refer to the comments in the individual files for detailed usage of specific agents or tasks.

## Results
The agents were tested on various Gridworld layouts, and their performance was evaluated based on their ability to learn and execute optimal policies. The results demonstrate the effectiveness of each algorithm in different scenarios, with particular emphasis on the trade-offs between exploration and exploitation in Q-Learning.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
