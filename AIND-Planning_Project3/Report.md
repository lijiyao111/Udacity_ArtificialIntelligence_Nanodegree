# Implement a Planning Search
> My codes in `my_air_cargo_problems.py` and `my_planning_graph.py` passed all unittest in both `test_my_air_cargo_problems.py` and `test_my_planning_graph.py`

Breath first search, Uniform cost search, A-star ignore-preconditions heuristic and A-star level-sum heuristic give optimal planning solution. Sometimes, Greedy best first search also gives optimal solution. Depth first search does not give optimal planning solution.

Since the path cost is 1 from one state to another, Uniform cost search is just Breath first search. Greedy best first search is implemented incorrectly. In `aimacode.search.py`, it is defined as `greedy_best_first_graph_search = best_first_graph_search`, which use a priority queue as frontier. However, the weight for each node is the same. Since elements with the same weight in priority queue does not have fixed order among them, Greedy best first search is neither depth search or breadth search and its solution is not guaranteed to be optimal.   

Among all the search methods, Depth first search takes the shortest time and expand few numbers of nodes. However, it solution is not optimal. Breadth first search takes quite long time and expands the most number of nodes (Uniform cost search is similar to breath first search), but gives optimal solution. 

The A-star search with ignored precondition heuristic and levelsum heuristic give optimal solution. The heuristic search has less expansions than the non-heuristic search. The levelsum heuristic give the least number of expansions and new nodes. However, heuristic also takes time to calculate. The more complicated and more accurate levelsum heuristic takes much much longer to calculate than vanilla breath first search. 

<center> Table 1. - Air Cargo Problem 1. </center>

Search  | Length | Time (s) | Expansions | Goal Tests | New Nodes 
--- | --- | --- | --- | --- | ---
Breadth First| 6 | 0.035 | 43 | 56 |180
Depth First | 20 | 0.016 | 21 | 22 | 84
Uniform Cost | 6 | 0.043 | 55 | 57 | 224
Greedy Best | 6 | 0.006 | 7 | 9 | 28
A-star Ignore | 6 | 0.052 | 41 | 43 | 170
A-star Levelsum | 6 | 1.508 | 11 | 13 | 50

Optimal plan for air cargo problem 1:
```
Load(C1, P1, SFO)
Fly(P1, SFO, JFK)
Unload(C1, P1, JFK)
Load(C2, P2, JFK)
Fly(P2, JFK, SFO)
Unload(C2, P2, SFO)
```

<center> Table 2. - Air Cargo Problem 2. </center>

Search  | Length | Time (s) | Expansions | Goal Tests | New Nodes 
--- | --- | --- | --- | --- | ---
Breadth First| 9 | 13.951 | 3343 | 4609 | 30509
Depth First | 619 | 3.396 | 624 | 625 | 5602
Uniform Cost | 9 | 47.222 | 4852 | 4854 | 44030
Greedy Best | 15 | 7.565 | 990 | 992 | 8910
A-star Ignore | 9 | 15.354 | 1506 | 1508 | 13820
A-star Levelsum | 9 | 157.657 | 86 | 88 | 841

Optimal plan for air cargo problem 2:
```
Load(C1, P1, SFO)
Load(C2, P2, JFK)
Load(C3, P3, ATL)
Fly(P1, SFO, JFK)
Fly(P2, JFK, SFO)
Fly(P3, ATL, SFO)
Unload(C3, P3, SFO)
Unload(C2, P2, SFO)
Unload(C1, P1, JFK)
```

<center> Table 3. - Air Cargo Problem 3. </center>

Search  | Length | Time (s) | Expansions | Goal Tests | New Nodes 
--- | --- | --- | --- | --- | ---
Breadth First| 12 | 96.546 | 14663 | 18098 | 129631
Depth First | 392 | 1.731 | 408 | 409 | 3364
Uniform Cost | 12 | 371.445 | 18235 | 18237 | 159716
Greedy Best | 22 | 101.327 | 5614 | 5616 | 49429
A-star Ignore | 12 | 88.902 | 5118 | 5120 | 45650
A-star Levelsum | 12 | 1002.065 | 403 | 405 | 3708

Optimal plan for air cargo problem 3:
```
Load(C2, P2, JFK)
Fly(P2, JFK, ORD)
Load(C4, P2, ORD)
Fly(P2, ORD, SFO)
Unload(C4, P2, SFO)
Load(C1, P1, SFO)
Fly(P1, SFO, ATL)
Load(C3, P1, ATL)
Fly(P1, ATL, JFK)
Unload(C3, P1, JFK)
Unload(C2, P2, SFO)
Unload(C1, P1, JFK)
```

## Planning Graph

Below is the Planning Graph generated from my code for the "Have Cake and Eat it Too" problem. After checking, this planning graph is correct. And interestingly, the Level A1 is different from the figure in AIMA book in terms of mutex relationship. Probably due to display reason, the textbook figure missed 4 mutual exclusive relations on Level A1:
`Noop_pos(Have(Cake),) vs Noop_pos(Eaten(Cake),)`
`Noop_neg(Have(Cake),) vs Noop_neg(Eaten(Cake),)`
`Eat(Cake,) vs Noop_neg(Have(Cake),)`
`Eat(Cake,) vs Noop_pos(Eaten(Cake),)`

My planning graph:
```
A-star levelsum heuristic

in S_level 0:

*** ~Eaten(Cake)
0 parents
1 children
0 mutex
*** Have(Cake)
0 parents
2 children
0 mutex

in A_level 0:

*** Eat(Cake,)
1 parents
2 children
2 mutex
*** Noop_neg(Eaten(Cake),)
1 parents
1 children
1 mutex
*** Noop_pos(Have(Cake),)
1 parents
1 children
1 mutex

in S_level 1:

*** ~Eaten(Cake)
1 parents
1 children
2 mutex
*** Eaten(Cake)
1 parents
1 children
2 mutex
*** ~Have(Cake)
1 parents
2 children
2 mutex
*** Have(Cake)
1 parents
2 children
2 mutex

in A_level 1:

*** Noop_pos(Have(Cake),)
1 parents
1 children
4 mutex
*** Noop_neg(Have(Cake),)
1 parents
1 children
4 mutex
*** Eat(Cake,)
1 parents
2 children
5 mutex
*** Bake(Cake,)
1 parents
1 children
4 mutex
*** Noop_pos(Eaten(Cake),)
1 parents
1 children
3 mutex
*** Noop_neg(Eaten(Cake),)
1 parents
1 children
4 mutex

in S_level 2:

*** ~Eaten(Cake)
1 parents
0 children
2 mutex
*** Eaten(Cake)
2 parents
0 children
1 mutex
*** ~Have(Cake)
2 parents
0 children
2 mutex
*** Have(Cake)
2 parents
0 children
1 mutex
```