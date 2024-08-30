# analysis.py
# -----------
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


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    answerNoise = 0.01
    # lower noise to produce more deterministic actions.
    # Any noise larger than 1% prohibits the agent from crossing.
    return answerDiscount, answerNoise

def question3a():
    """
      Prefer the close exit (+1), risking the cliff (-10).
    """
    answerDiscount = 0.2  # small discount factor to prioritize immediate rewards
    answerNoise = 0.01 # agent fails with a larger noise factor.
    answerLivingReward = -1.0 # to encourage the agent to move quickly rather than staying
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b():
    """
      Prefer the close exit (+1), but avoiding the cliff (-10).
    """
    answerDiscount = 0.3  # prioritize immediate rewards less, thus more risk aversion
    answerNoise = 0.3  # any higher noise and agent fails
    answerLivingReward = 0.1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    """
      Prefer the distant exit (+10), risking the cliff (-10).
    """
    answerDiscount = 0.9  # prioritize future rewards more
    answerNoise = 0.01
    answerLivingReward = 0.1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    """
      Prefer the distant exit (+10), avoiding the cliff (-10).
    """
    answerDiscount = 0.9  # prioritize future rewards
    answerNoise = 0.3
    answerLivingReward = 0.1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    """
      Avoid both exits and the cliff (so an episode should never terminate).
    """
    answerDiscount = 1.0  # prioritise future rewaeds
    answerNoise = 0.0  # deterministic actions
    answerLivingReward = 1.0  # allow agent to linger
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question7():
    answerEpsilon = 0.1  # TO DO
    answerLearningRate = 0.5
    # return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'
    return 'NOT POSSIBLE'
if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
