import numpy as np
import os
import matplotlib.pyplot as plt

def get_neighborhood(cell, occ_map_shape):
  '''
  @params 
    cell - cell coordinates
    occ_map_shape - shape of the occupancy map

  returns
    - list of neighbor coordinate tuples
  '''

  result = []

  for i in [-1, 0, 1]:
    for j in [-1, 0, 1]:
        x = cell[0] + i
        y = cell[1] + j

        if (x < 0) or (x >= occ_map_shape[0]):
            continue
        if (y < 0) or (y >= occ_map_shape[1]):
            continue
        if i == j == 0: 
            continue
        
        result.append((x, y))
    
  return result

def get_edge_cost(parent, child, occ_map):
  '''
  Cost for moving from parent to child.
  @params
    parent, child - cell coordinates
    occ_map - occupancy grid

  returns -
    edge_cost
  '''
  cost = 0
  
  prob = occ_map[child]
  cost = np.linalg.norm(np.array(parent) - np.array(child))
  cost += 10 * prob
  if prob>=0.5:
      cost = np.inf
  return cost

def get_heuristic(cell, goal, n = 1):
  '''
  Heuristically estimated cost
  @params -
    cell, goal - cell coordinates
  returns
    cost
  '''
  heuristic = 0
  heuristic = np.linalg.norm(cell-goal)*n
  return heuristic

def plot_map(occ_map, start, goal):
  plt.imshow(occ_map.T,cmap=plt.cm.binary, interpolation='none', origin='upper')
  plt.plot([start[0]], [start[1]], 'rs')
  plt.plot([goal[0]], [goal[1]], 'gs')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.grid(b=True)

def plot_expanded(expanded, start, goal):
  if np.array_equal(expanded, start) or np.array_equal(expanded, goal):
    return
  plt.plot([expanded[0]], [expanded[1]], 'ys')
  plt.pause(1e-100)

def plot_path(path, goal):
  if np.array_equal(path, goal):
    return
  plt.plot([path[0]], [path[1]], 'bs')
  plt.pause(1e-100)

def plot_costs(cost):
  plt.figure()
  plt.imshow(cost.T, cmap=plt.cm.gray, interpolation='none', origin='upper')
  plt.xlabel('x')
  plt.ylabel('y')

def path_planning(occ_map, start, goal, n_H):
 
  plot_map(occ_map, start, goal)
  costs = np.ones(occ_map.shape) * np.inf
  closed_flags = np.zeros(occ_map.shape)
  
  predecessors = -np.ones(occ_map.shape + (2,), dtype=np.int)

  # heuristic for A*
  heuristic = np.zeros(occ_map.shape)
  for x in range(occ_map.shape[0]):
    for y in range(occ_map.shape[1]):
      heuristic[x, y] = get_heuristic([x, y], goal, n_H)

  parent = start
  costs[start[0], start[1]] = 0

  while not np.array_equal(parent, goal):
    
    open_costs = np.where(closed_flags==1, np.inf, costs) + heuristic

    x, y = np.unravel_index(open_costs.argmin(), open_costs.shape)
   
    if open_costs[x, y] == np.inf:
      break
    
    parent = np.array([x, y])
    closed_flags[x, y] = 1
    
    neighbours = get_neighborhood(parent, occ_map.shape)
    for child in neighbours:
      child_cost = costs[x, y] + get_edge_cost(parent, child, occ_map)
      if child_cost < costs[child]:
          costs[child] = child_cost
          predecessors[child] = parent
    
    # Covered cells
    plot_expanded(parent, start, goal)
  
  # rewind the path from goal to start (at start predecessor is [-1,-1])
  if np.array_equal(parent, goal):
    path_length = 0
    while predecessors[parent[0], parent[1]][0] >= 0:
      plot_path(parent, goal)
      predecessor = predecessors[parent[0], parent[1]]
      path_length += np.linalg.norm(parent - predecessor)
      parent = predecessor

    print (f"Explored {np.count_nonzero(closed_flags)} cells.")
    print ("Path cost = ", costs[goal[0], goal[1]])
    print ("Path length = ", path_length)
  else:
    print ("No valid path found.")
  plt.waitforbuttonpress()

def path(start, goal, n_H = 2):
  # load the occupancy map
  occ_map = np.loadtxt('map.txt')
  path_planning(occ_map.T, start, goal, n_H)
  os.remove('map.txt')