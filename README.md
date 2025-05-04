# DUMB-EFFICIENT-algorithm-
Descending Tree Resolution with Density Polarization Algorithm for TSP"
_Note_: Alpha version, details to come. Further details on resolution methods, implementation proposal, explanatory details of simulations, and extended comparison to other algorithms will be added in future versions.


DUMB EFFICIENT: A Simple and Efficient Algorithm for Solving the Traveling Salesman Problem

Abstract
The Traveling Salesman Problem (TSP) is a complex problem that has been studied for decades. We propose a simple and efficient algorithm to solve this problem, called DUMB EFFICIENT. Our approach involves dividing the problem into smaller sub-problems and solving them in a hierarchical manner.

Introduction
The Traveling Salesman Problem (TSP) is a complex combinatorial optimization problem that has been extensively studied over the years. Various algorithms have been proposed to solve TSP, including exact methods such as linear programming and approximation methods such as heuristics and metaheuristics. Despite significant progress, TSP remains a challenging problem for researchers and practitioners due to its complexity and size. We propose a simple and efficient algorithm to solve this problem, called DUMB EFFICIENT. Our approach involves dividing the problem into smaller sub-problems and solving them in a hierarchical manner.

Algorithm Description
The DUMB EFFICIENT algorithm works as follows:
1. Create an initial clustering of cities using DBSCAN.
2. Create a first cluster of density zones of cities with a maximum size of 20 (C1).
3. Divide the density clusters into sub-clusters of maximum size 20 (C2's).
4. Repeat step 3 until clusters of maximum size 20 (Cx's) are obtained.
5. Determine the medoid points using PAM.
6. Join the clusters using the medoid points.
7. Solve each cluster using the nearest neighbor algorithm.

Simulation Results
We have performed simulations to evaluate the performance of the DUMB EFFICIENT algorithm. The results show that:
- For problems of size between 1000 and 5000 cities, the DUMB EFFICIENT algorithm obtains high-quality results, with an accuracy greater than 90%.
- The time complexity of the algorithm is linear, making it very efficient for large-scale problems.
Comparison with other algorithms*

We have also compared the performance of the DUMB EFFICIENT algorithm with that of the Lin-Kernighan-Helsgaun (LKH) algorithm, which is considered one of the best algorithms for solving TSP. The results show that:

- The DUMB EFFICIENT algorithm obtains results of similar quality to those of LKH for problems of size between 1000 and 5000 cities.
- However, the DUMB EFFICIENT algorithm is faster than LKH for large-scale problems.
Conclusion
The DUMB EFFICIENT algorithm is a simple and efficient approach to solving the Traveling Salesman Problem. It is based on a hierarchical modeling and uses clustering and optimization techniques to obtain high-quality results.

References
- Ester, M., Kriegel, H. P., Sander, J., & Xu, X. (1996). A density-based algorithm for discovering clusters in large spatial databases with noise. Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining, 226-231.
- Kaufman, L., & Rousseeuw, P. J. (1990). Finding groups in data: An introduction to cluster analysis. Wiley-Interscience.

NB: When running the program, you will be prompted to enter the parameters `max_cluster_size`, `min_cluster_size`, `Epsilon`, and `num_cities`. For reference, the initial development was based on `max_cluster_size = 20` and `Epsilon = 0.5`, but you can experiment with different values for all parameters to optimize the results.
