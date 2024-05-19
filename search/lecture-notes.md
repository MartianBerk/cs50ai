# Search - Lecture 1

### Terms:
- <b>agent</b>: entity that perceives its environment and acts upon it.
- <b>state</b>: configuration of the agent and it's environment.
- <b>initial state</b>: where agent begins.
- <b>actions</b>: choices that can be made in a state.
    ACTIONS(s) returns the set of actions that can be executed in state s.
- <b>transition model</b>: a description of what state we get from performing any applicable actions on a state.
    RESULT(s, a) returns the state resulting from performing action a in state s.
- <b>state space</b>: set of all the states reachable from the initial by any sequence of actions. Here, imagine the game of 15 puzzle and therefore all the possible moves and the outcome from each in sequence.
- <b>goal test</b>: way to determine if a given state is a goal state.
- <b>path cost</b>: numerical cost of a given path.

### Notes
A search problem is looking for the optimal solution to go from a initial state to goal state by performing actions.

A node is a data structure that keeps track of a state, a parent node (the node that generated this node), an action (applied to parent to get to node) and a path cost (from initial state to node).

<b>Approach:</b> 

We start from a given state and explore from there. Once we explore, more options will become apparent. A "frontier" will be a data structure that contains all the states.
The frontier will start with the intial state.

<b>Algorithm</b>

Repeat:
- If the frontier is empty, then no solution.
- Remove a node from the frontier.
- If that node happpens to be a goal, return the solution.
- Otherwise, expand the node, add resulting nodes to the frontier. Those are the next nodes the agent can get to.

<b>Example:</b>

Find a path from A - E.
<br />
A branches from B.
<br />
```
A -> B -> C -> E
     | -> D -> F
```

Frontier will hold A to start.
Next, remove A from the frontier. Is this node the goal? No. So we expand and add the resulting nodes to the frontier. So, now B will be in the frontier.

Frontier holds B.
Now we're considering B. Repeating the process.

Frontier now holds C and D.
Now we remove C, arbitrarily picked. Now add E to the frontier.

Frontier now holds E and D.
Remove E, it's the goal.
COMPLETE.

What can go wrong here?
Imagine A and B is bi-directional.
<br />
A -> B -> A.
<br />
What happens now? Can get to A, C and D all in the frontier. If you randomly pick A, you're in a loop. We can deal with this by tracking what we already explored. No need to go back to another state and add it to the frontier.

<b>Revised approach:</b>

Start with a frontier that contains the initial state.
Start with an empty explorted set.

Repeat:
- If the frontier is empty, then no solution.
- Remove a node from the frontier.
- If that node happpens to be a goal, return the solution.
- <b>Add the node to the explored set.</b>
- Otherwise, expand the node, add resulting nodes to the frontier. Those are the next nodes the agent can get to. Only do this if not already in the frontier <b>or in the explored set</b>.

How do we structure a frontier? How do we add and remove a node, therefore what order do we do things in? It can be a:
- <b>STACK:</b> last-in first-out data type. We always pop the last node from the frontier to examine. In the above example, we would go as deep as we can in the search tree to then back up and go back down another route if needed. This is depth-first search. A search algorith that always expands the deepest node in the frontier.
- <b>QUEUE:</b> first-in first-out data type, breadth-first search. Always expands the shallowest node in the frontier.

Depth first search will find the goal eventually given a finite set of states. But it might not necessarily find the best path.

Breadth first search will check all nodes that are one away (immediately next to initial state). Then it will pick those 2 away, and then three away, etc. Looking deeper and deeper along both paths simultaneously. It will find the most optimal path though. It will also have to explore a lot of states. A lot of wasted time.

<b>Intelligent Search</b>

On a large maze, breadth first search will often have to examine the entire maze. How can it do this more intelligently?
At the first decision point, a human would kind of know the direction to head in. A computer can assume this based on coordinates. The algorithm can and should do this. Uninformed search vs informed search.

- <b>Uninfoirmed search:</b> Uses no problem-specific knowledge to solve the problem.
- <b>Informed search:</b> Uses problem-specific knowledge to find solutions more efficiently. An example of this, if you're in a node thats geographically closer to the goal then that's better.

<b>Greedy best-first search</b> will expand the node that is closest to the goal, estimated by a heuristic function <i>h(n)</i>. An example of this is Manhattan Distance. How many squares vertically and horizontally from two points will it take to get to the goal, ignoring walls? Because it's ignoring the walls, or relaxing the problem, the hueristic is just an estimate. As a result of this, we can make an informed decision on the better route to take.

Would you always use this? Well, you'd need a good hueristic. Also, will it always find the optimal path? Not necessarily... It depends on the maze, in these examples. If the path is a bit convuluted, then you might want to consider how many steps it will take to get to a higher number. This algorithm would be A* search. Don't just consider the hueristic, but also the cost to reach each node.

<b>A* Search:</b> Expands node with the lowest value of <i>g(n) + h(n)</i>.

- <i>g(n)</i> = cost to reach the node.
- <i>h(n)</i> = estimated cost to goal.

A* is optimal if <i>h(n)</i> is admissible, it never over-estimates the true cost, either gets it right or under-estimates. And, <i>h(n)</i> is consistent, for every node <i>n</i> and successor <i>n'</i> with step cost <i>c</i>: <i>h(n) <= h(n') + c</i>. This is where the problem often comes, choosing a good hueristic. There are other search algorithms for other use cases.

<b>Adversarial Search:</b>

What about adversarial search? Two agents competing. Could imagine a game, like tic-tac-toe. The problem is similar in spirit, with actions, states, etc. But we just now have an opponent. One algorithm here is called Minimax.

<b>Minimax:</b> Can take each of the possible ways a tic-tac-toe game can unfold and assign that a value. Could be -1, 0 and 1 for lose, draw and win respectively. The X player can be the max player and the O player can be the min player. X wants to maximise the score, while O wants to minimize the score. We reduce the notion of winning and losing mathematically to maximize or minimize the score.

- <b>MAX(X)</b> aims to maximise the score
- <b>MIN(O)</b> aims to minimize the score

<b>Functions:</b>
<br />
<br />
<b>S0:</b> initial state
<br />
<b>Player(s):</b> returns which player to move in state <i>s</i>. Which players turn is it.
<br />
<b>Actions(s):</b> return the legal moves in state <i>s</i>.
<br />
<b>Result(s, a):</b> returns the state after action <i>a</i> taken in state <i>s</i>.
<br />
<b>Terminal(s):</b> checks if state is in a terminal state, is the game over? Multiple goals: someone wins or draw equals terminal state.
<br />
<b>Utility(s):</b> final numerical value for terminal state <i>s</i>.

Initial state is empty game board. (2-D array)
<br />
Player(s): Whos turn it is.
<br />
Actions(s): All possible actions in that state, just like in other algorithms above.
<br />
Result(s, a): Apply the move to the state and return the new state.
<br />
Terminal(s): Is the game over?
<br />
Utility(s): Win = 1, lose = -1, draw = 0.

Minimax is a recursive alogithm, when it finds the next state of a move, it needs to decide what the opponent would do. So, if you're trying to minimize, then your opponent is trying to maximize. Follow this recursion back and forth until you hit the terminal state.

Given a state <i>s</i>:
<br />
Max player picks an action <i>a</i> in Actions(s) that produces highest value of <b>MIN-VALUE(RESULT(s, a))</b>.
Min player picks an action a in Actions(s) that produces the smallest value of <b>MAX-VALUE(RESULT(s, a))</b>.

Function MAX-VALUE(s): 
<br />
Is the game over? 
<br />
If Terminal(s) return Utility(s). 
Else, v = negative infinity. Initial value. 
<br />
For a in actions(s): v = MAX(v, MIN-VALUE(Result(s, a))).
<br />
Return v. 
<br />
What we're doing here is for each value we're finding the max of v and MIN-VALUE, what the opponent is doing.
<br />
MIN-VALUE(s): Direct opposite. v is inifity and the loop logic checks against MIN(v, MAX-VALUE(Result(s, a))).

This alogirthm can get long for more complex games. What optimizations do we have? Maybe you don't have to do all the calculations available to figure out. If you're the max player and you see a value, say 4. If on the next action you see a 3 before you complete that path, you can stop there as you know there is no other number that can be higher than it; the min player would not pick it. Save some time this way. You're keeping track a bit more, but it can help save some time. This kind of optimisation is called <b>Alpha-Beta Pruning</b>. 

Think about Chess, which is a far more complex game. Introduce <b>Depth-Limited Minimax</b>. Tic-Tac-Toe was depth-unlimited as it's so simple. The idea here is you stop after, say, 10 moves deep. You still need to assign a score here, even if it's not in terminal state. So we add one addition feature, called an <b>evaluation function</b>. This will estimate the expected Utility of the game from a given state. How good the evaluation function is will determine how good the AI is. These kinds of functions are key. For example, in chess a simple one might think about how many pieces are left with a numerical assigned for each piece to sway the decision somehow.