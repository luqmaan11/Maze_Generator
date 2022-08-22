# Maze_Generator

A maze can be generated using a predetermined grid or arrangement of cells, 
which can be looked at as a connected graph. Each node of the graph 
represents a cell in the maze and the edges represent wall sites. Then, using the 
maze generating algorithm, a subgraph can be generated that represents a 
challenging route between 2 nodes.

### Algorithm

Randomized Prim’s Algorithm consists of the following steps:
1. Start with a grid full of walls
2. Pick a cell, mark it as part of the maze. Add the walls of the cell to the 
walls of the list
3. While there are walls in the list:
 1. Pick a random wall from the list. If only one of the two cells that the 
wall divides are visited, then:
 a) Make the wall a passage and mark the unvisited cell as part of 
the maze
 b) Add the neighboring walls of the cell to the wall list.
 2. Remove the wall from the list
 
 ### Steps to Run:
 - Install prerequisites: Django,colorama
 - Open the Project in Pycharm after dowloading and extracting the files
 - Type in console: "python manage.py runserver"
 
 
 ### Screenshots
 
 **Homepage:**
 
![image](https://user-images.githubusercontent.com/69753061/186014572-c8b6a28d-5483-4dd3-b7d3-2cee66d46032.png)

![image](https://user-images.githubusercontent.com/69753061/186014591-c79a0c49-80da-42f3-b287-029e5af15993.png)

![image](https://user-images.githubusercontent.com/69753061/186014614-2c0769bb-3df0-4e38-9122-9b3febf53492.png)

**Input Dimensions:**

![image](https://user-images.githubusercontent.com/69753061/186014623-89fdcab8-4972-42f0-b57b-180727ff3af9.png)

**Output:**

![image](https://user-images.githubusercontent.com/69753061/186014652-6695537b-55e3-46d7-80ce-fca13a7fa8fd.png)
