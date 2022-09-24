# Search
<strong>FILES WORKED ON: search.py, searchAgents.py</strong>

This project uses various search algorithms such as breadth first search, A* search, and a few others to help a pacman agent
find particular locations and collect food efficiently. It was developed using Python.

<strong>Commands:</strong>
<ul>
<li><strong>python pacman.py -l mediumMaze -p SearchAgent</strong>
  <ul>
    <li>Depth first search is used to help pacman find a path to a particular location.</li>
  </ul>
</li>
<li><strong>python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs</strong>
  <ul>
    <li>Breadth first search is used to help pacman find the shortest path to a particular location.</li>
  </ul>
</li>
<li><strong>python pacman.py -l mediumDottedMaze -p StayEastSearchAgent</strong>
  <ul>
    <li>Uniform cost search is used to help pacman find a path to a particular location. Paths with food are preferred.</li>
  </ul>
</li>
<li><strong>python pacman.py -l mediumScaryMaze -p StayWestSearchAgent</strong>
  <ul>
    <li>Uniform cost search is used to help pacman find a path to a particular location. Paths without ghosts are preferred.</li>
  </ul>
</li>
<li><strong>python pacman.py -l mediumMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic</strong>
  <ul>
    <li>A* search is used to help pacman find the shortest path to a particular location. The manhattan distance to the goal state is used as a heuristic.</li>
  </ul>
</li>
<li><strong>python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem</strong>
  <ul>
    <li>Uniform cost search is used to find the shortest path to reach all corners.</li>
  </ul>
</li>
<li><strong>python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5</strong>
  <ul>
    <li>A* search is used to find the shortest path to reach all corners. The minimum total manhattan distance to reach all corners is used as a heuristic.</li>
  </ul>
</li>
<li><strong>python pacman.py -l trickySearch -p AStarFoodSearchAgent</strong>
  <ul>
    <li>A* search is used to eat all food in as few steps as possible. The maximum maze distance to a food pellet is used as a heuristic.</li>
  </ul>
</li>
<li><strong>python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5</strong>
  <ul>
    <li>A suboptimal path to eat all food is quickly found by greedily eating the closest food pellet every time.</li>
  </ul>
</li>
</ul>
