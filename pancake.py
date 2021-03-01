from simpleai.search import *
from random import shuffle
from datetime import datetime

class PancakeProblem(SearchProblem):
    def __init__(self, initial_state):
        self.initial_state = tuple(initial_state)
        self.goalState = tuple(sorted(initial_state))
        self.size = len(initial_state)

    def actions(self, state):
        possible_actions = []
        for i in range(2,self.size+1):
            possible_actions.append(i)
        return possible_actions

    def result(self, state, action):
        firstPie = state[:action]
        secondPie = state[action:self.size]
        resultState = tuple(reversed(firstPie)) + tuple(secondPie)
        return resultState

    def is_goal(self, state):
        return state == self.goalState

    def heuristic(self, state):
        max_out_of_place = 0
        for i in range(len(self.goalState)):
            if self.goalState[i] != state[i]:
                if max_out_of_place < int(self.goalState[i]):
                    max_out_of_place = int(self.goalState[i])
        return max_out_of_place

    def cost(self, state, action, state2):
        firstPie = state[:action]
        return len(firstPie)


def UCS(problem):
    before = datetime.now()
    search = uniform_cost(problem)
    after = datetime.now()
    print("*** Uniform Cost Search ***")
    print("Actions: ",search.action_representation())
    print("Path: ",search.path())
    print("Path Cost: ", search.cost)
    print("Time: ",(after - before).total_seconds())
    print("*"*30)
def BFS(problem):
    before = datetime.now()
    search = breadth_first(problem)
    after = datetime.now()
    print("*** Breadth First Search ***")
    print("Actions: ", search.action_representation())
    print("Path: ", search.path())
    print("Path Cost: ",search.cost)
    print("Time: ", (after - before).total_seconds())
    print("*" * 30)
def DFS(problem):
    before = datetime.now()
    search = depth_first(problem, graph_search=True)
    after = datetime.now()
    print("*** Depth First Search ***")
    print("Actions: ",search.action_representation())
    print("Path: ",search.path())
    print("Path Cost: ", search.cost)
    print("Time: ", (after - before).total_seconds())
    print("*" * 30)
def DLS(problem):
    before = datetime.now()
    search = limited_depth_first(problem, depth_limit=10, graph_search=True)
    after = datetime.now()
    print("*** Depth Limited Search ***")
#    print("Actions: ",search.action_representation())
    print("Path: ",search.path())
    print("Path Cost: ", search.cost)
    print("Time: ", (after - before).total_seconds())
    print("*" * 30)
def IDS(problem):
    before = datetime.now()
    search = iterative_limited_depth_first(problem)
    after = datetime.now()
    print("*** Iterative DLS Search ***")
    print("Actions: ",search.action_representation())
    print("Path: ",search.path())
    print("Path Cost: ", search.cost)
    print("Time: ", (after - before).total_seconds())
    print("*" * 30)
def GBFS(problem):
    before = datetime.now()
    search = greedy(problem,lambda node: node.state)
    after = datetime.now()
    print("*** Greedy Best First Search ***")
    print("Actions: ", search.action_representation())
    print("Path: ", search.path())
    print("Path Cost: ", search.cost)
    print("Time: ", (after - before).total_seconds())
    print("*" * 30)
def Astar(problem, viewer=my_viewer):
    before = datetime.now()
    search = astar(problem)
    after = datetime.now()
    print("*** AStar Search ***")
    print("Actions: ",search.action_representation())
    print("Path: ",search.path())
    print("Path Cost: ", search.cost)
    print("Time: ", (after - before).total_seconds())
    print("-" * 18)
def AllAlgorithms(problem):
    print(("*" * 22) + "\n* Uniformed Searches *\n" + ("*" * 22))
    BFS(problem)
    UCS(problem)
    DFS(problem)
    DLS(problem)
    IDS(problem)
    print(("*" * 22) + "\n* Informed Searches  *\n" + ("*" * 22))
    GBFS(problem)
    Astar(problem)

pancakeNumber = int(input("Enter number of pancakes: ")) - 1
isOrder = input("Do you want to enter ordering? yes(y), no(n)")
initial_state = []
goalState = []

if(isOrder == "n"):
    for i in range(pancakeNumber + 1):
        initial_state.append(i)
    shuffle(initial_state)
    print(initial_state)
else:
    print(f"Enter top to bottom ordering between [0, {pancakeNumber}]")
    for i in range(pancakeNumber + 1):
        userOrder = input()
        initial_state.append(userOrder)
    print(initial_state)

pancake_problem = PancakeProblem(initial_state)

while True:
        print("Which searching algorithm do you want to calculate?")
        algorithm = int(input("1 - All algorithms\n"
              "2 - Breadth First Search\n"
              "3 - Uniform Cost Search\n"
              "4 - Depth First Search\n"
              "5 - Depth Limited Search\n"
              "6 - Iterative DLS Search\n"
              "7 - Greedy Best First Search\n"
              "8 - Astar Search\n"))
        if algorithm == 1:
            AllAlgorithms(pancake_problem)
        elif algorithm == 2:
            BFS(pancake_problem)
        elif algorithm == 3:
            UCS(pancake_problem)
        elif algorithm == 4:
            DFS(pancake_problem)
        elif algorithm == 5:
            DLS(pancake_problem)
        elif algorithm == 6:
            IDS(pancake_problem)
        elif algorithm == 7:
            GBFS(pancake_problem)
        elif algorithm == 8:
            Astar(pancake_problem)
        else:
            print("Invalid input")
            continue
        if input("Want to calculate with different algorithm? [y]/[n]") =="n":
            break
