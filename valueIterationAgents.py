# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
import queue

# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util
from queue import PriorityQueue

from learningAgents import ValueEstimationAgent
import collections

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.runValueIteration()

    def getGreedyUpdate(self, state):
        """computes a one step-ahead value update and return it"""
        if self.mdp.isTerminal(state):
            return self.values[state]
        actions = self.mdp.getPossibleActions(state)
        vals = util.Counter()
        for action in actions:
            vals[action] = self.computeQValueFromValues(state, action)
        return max(vals.values())

    def runValueIteration(self):
        # Write value iteration code here

        for i in range(self.iterations):
            new_values = self.values.copy()
            for state in self.mdp.getStates():
                if self.mdp.isTerminal(state):
                    new_values[state] = 0
                else:
                    actions = self.mdp.getPossibleActions(state)
                    new_values[state] = max([self.computeQValueFromValues(state, action) for action in actions])
            self.values = new_values


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):  # calculate Q value for given state-action pair
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """

        q_value = 0

        # Iterate over all possible next states and their transition probabilities
        for next_state, prob in self.mdp.getTransitionStatesAndProbs(state, action):
            # Get the reward for this transition
            reward = self.mdp.getReward(state, action, next_state)
            # Get the value of the next state
            next_value = self.values[next_state]
            # Compute the expected value
            q_value += prob * (reward + self.discount * next_value)  #Bellman update

        return q_value


    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        # Check if the state is terminal
        if self.mdp.isTerminal(state):
            return None  # No action

        # Initialize variables to keep track of the best action and highest Q-value
        best_action = None
        highest_q_val = float('-inf')

        # Iterate over all possible actions from the state
        for action in self.mdp.getPossibleActions(state):
            # Compute the Q-value for this action
            q_value = self.computeQValueFromValues(state, action)

            # Update best action if this Q-value is higher than the current highest
            if q_value > highest_q_val:
                highest_q_val = q_value
                best_action = action

        return best_action


    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)


class PrioritizedSweepingValueIterationAgent(ValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A PrioritizedSweepingValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs prioritized sweeping value iteration
        for a given number of iterations using the supplied parameters.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100, theta = 1e-5):
        """
          Your prioritized sweeping value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy.
        """
        self.theta = theta
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()  # A Counter is a dict with default 0
        self.runValueIteration()


    def runValueIteration(self):
        # Compute predecessors of all states
        predecessors = {}
        for state in self.mdp.getStates():
            predecessors[state] = set()
        for state in self.mdp.getStates():
            # For each non - terminal state s, do: (note: to make the autograder work for this question, you
            # must iterate over states in the order returned by self.mdp.getStates())
            if not self.mdp.isTerminal(state):
                for action in self.mdp.getPossibleActions(state):
                    for next_state, prob in self.mdp.getTransitionStatesAndProbs(state, action):
                        if prob > 0:
                            predecessors[next_state].add(state)

        # Setup priority queue for all states based on their highest diff in greedy update
        # util.raiseNotDefined()

        # Initialize an empty priority queue.
        priority_queue = util.PriorityQueue()

        for state in self.mdp.getStates():
            if not self.mdp.isTerminal(state):
                max_q_value = max(self.computeQValueFromValues(state, action)
                                  for action in self.mdp.getPossibleActions(state))
                # Find the absolute value of the difference between the current value of s in self.values and the highest Q - value
                # across all possible actions from s (this represents what the value should be);
                # call this number diff.Do NOT update self.values[s] in this step.
                diff = abs(self.values[state] - max_q_value)
                # Push s into the priority queue with priority - diff(note that this is negative).
                # We use a negative because the priority queue is a min heap, but we want to prioritize updating states
                # that have a higher error.
                priority_queue.update(state, -diff)

        # run priority sweeping value iteration:
        # util.raiseNotDefined()

        # For iteration in 0, 1, ..., self.iterations - 1, do:
        for _ in range(self.iterations):
            if priority_queue.isEmpty():  # If the priority queue is empty, then terminate.
                break

            state = priority_queue.pop()  # Pop a state s off the priority queue.

            # Update the value of s( if it is not a terminal state) in self.values.
            if not self.mdp.isTerminal(state):
                self.values[state] = max(self.computeQValueFromValues(state, action)
                                         for action in self.mdp.getPossibleActions(state))

            #   For each predecessor p of s, do:
            for p in predecessors[state]:
                max_q_value = max(self.computeQValueFromValues(p, action)   # python generator
                                  for action in self.mdp.getPossibleActions(p))
                # Find the absolute value of the difference between the current value of p in self.values and the highest Q - value
                # across all possible actions from p (this represents what the value should be); call this number diff.
                # Do NOT update self.values[p] in this step.
                diff = abs(self.values[p] - max_q_value)

                # If diff > theta, push p into the priority queue with priority - diff(note that this is negative),
                # as long as it does not already exist in the priority queue with equal or lower priority.
                # As before, we use a negative because the priority queue is a min heap, but we want to prioritize
                # updating states that have a higher error
                if diff > self.theta:
                    priority_queue.update(p, -diff)


class AsynchronousValueIterationAgent:
    print("Not part of this assignment.")
    pass
