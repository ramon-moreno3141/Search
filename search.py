# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    closed = set() #A set of states or coordinates
    fringe = util.Stack() #A stack of nodes. A node is a tuple with the state(coordinate) and list of actions: [s, w, e, etc.]
    fringe.push( (problem.getStartState(), []) )

    while not fringe.isEmpty():
        node = fringe.pop()
        curr_state = node[0]
        listOfActions = node[1]

        if problem.isGoalState(curr_state): return listOfActions
        if curr_state not in closed:
            closed.add(curr_state)
            for child_node in problem.getSuccessors(curr_state):
                copyOfActions = list(listOfActions)
                copyOfActions.append(child_node[1])
                fringe.push( (child_node[0], copyOfActions) )

    return None

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    closed = set() #A set of states or coordinates
    fringe = util.Queue() #A stack of nodes. A node is a tuple with the state(coordinate) and list of actions: [s, w, e, etc.]
    fringe.push( (problem.getStartState(), []) )

    while not fringe.isEmpty():
        node = fringe.pop()
        curr_state = node[0]
        listOfActions = node[1]

        if problem.isGoalState(curr_state): return listOfActions
        if curr_state not in closed:
            closed.add(curr_state)
            for child_node in problem.getSuccessors(curr_state):
                copyOfActions = list(listOfActions)
                copyOfActions.append(child_node[1])
                fringe.push( (child_node[0], copyOfActions) )

    return None
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    closed = set() #A set of states or coordinates
    fringe = util.PriorityQueue() #A stack of nodes. A node is a tuple with the state(coordinate) and list of actions: [s, w, e, etc.]
    fringe.push((problem.getStartState(), [], 0),  0)

    while not fringe.isEmpty():
        node = fringe.pop()
        curr_state = node[0]
        listOfActions = node[1]
        cost_to_come = node[2]

        if problem.isGoalState(curr_state): return listOfActions
        if curr_state not in closed:
            closed.add(curr_state)
            for child_node in problem.getSuccessors(curr_state):
                copyOfActions = list(listOfActions)
                copyOfActions.append(child_node[1])
                child_cost_to_come = cost_to_come + child_node[2]
                fringe.push((child_node[0], copyOfActions, child_cost_to_come), child_cost_to_come )

    return None
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    closed = set() #A set of states or coordinates
    fringe = util.PriorityQueue() #A stack of nodes. A node is a tuple with the state(coordinate) and list of actions: [s, w, e, etc.]

    start_state = problem.getStartState()
    fringe.push((start_state, [], 0),  0 + heuristic(start_state, problem))

    while not fringe.isEmpty():
        node = fringe.pop()
        curr_state = node[0]
        listOfActions = node[1]
        cost_to_come = node[2]

        if problem.isGoalState(curr_state): return listOfActions
        if curr_state not in closed:
            closed.add(curr_state)
            for child_node in problem.getSuccessors(curr_state):
                copyOfActions = list(listOfActions)
                copyOfActions.append(child_node[1])
                child_cost_to_come = cost_to_come + child_node[2]
                child_state = child_node[0]
                fringe.push((child_state, copyOfActions, child_cost_to_come), child_cost_to_come + heuristic(child_state, problem))

    return None
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
