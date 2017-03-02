# Udacity Artificial Intelligence Nanodegree
> In general, this class is similar to UC Berkeley's [Intro to AI class](http://ai.berkeley.edu/home.html);
>  Read this famous book on AI: [Artificial Intelligence: A Modern Approach](http://aima.cs.berkeley.edu/)

## Term 1
### Project 1, Sudoku -- Finished
Tricks to reduce possible states in the problem by implement Elimination, Naked Twins. Then Depth-first-search with backtracking to find the solution.

### Project 2, Isolation Game Playing -- Finished
Depth-limited search and iterative deepening search, with Minimax Decision and Alpha-beta pruning. Also provide heuristics to estimate the score of the leaf node.

### Lab 1, Pacman game playing, Search -- Finished
> From UC Berkeley [Intro To AI Class](http://ai.berkeley.edu/home.html)
> [Class project 1 on Search](http://ai.berkeley.edu/search.html)

Various kinds of graph search to reach the goal (destination, multiple destinations, and eat all the food). Design proper heuristic for A-star search.

As requested, I cannot post my solution to this Pacman search project to the public online. If you are stuck with this project, you can email me at jiyao.lee at gmail.com. 

Below is unittest from the Autograder:
```
-------------------------------------------------------------------------------
CS 188 Local Submission Autograder
Version 1.3.1
-------------------------------------------------------------------------------
Setting up environment.................................................... DONE
Downloading autograder.................................................... DONE
Extracting autograder..................................................... DONE
Preparing student files................................................... DONE
Running tests (this may take a while):
  Question q1...................... 3/3 
  Question q2...................... 3/3 
  Question q3...................... 3/3 
  Question q4...................... 3/3 
  Question q5...................... 3/3 
  Question q6...................... 3/3 
  Question q7...................... 4/4 
  Question q8...................... 3/3 
Generating submission token............................................... DONE
-------------------------------------------------------------------------------
Final score: 25/25
```



### Project 3, Search and Planning -- Finished
Solve deterministic logistics planning problems for an Air Cargo transport system using a planning search agent. Depth first graph search, Breath first graph search, Uniform cost search and A-star search with two heuristics. In the planning problem, heuristic does not have physical meaning such as euclidean distance or Manhattan distance to the destination in the navigation problem. The heuristic implemented in this problem is solution to a relaxed problem (number of unsatisfied goals) and planning graph. 
