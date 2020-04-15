# step 1: define the problem in terms of graphs
# what are your nodes? edges (when are two nodes connected)?
# word: ndoe
# hit -> hot
# edge: two words that differ by only 1 letter
# shortest transformation sequence: shortest path <- BFS

# step 2:
# build your graph or define getNeighbors function
# the words list is very large
# add words as nodes - maybe only those of same length as our start_word and end_word
# load edges

def find_ladders(start_word, end_word):
    q = Queue()
    visited = set()

    path = [start_word] # holds start_word to start off with
    q.enqueue(path)

    while q.size() > 0:
        current_path = q.dequeue()

        current_word = current_path[-1]

        if current_word == end_word:
            # then we would return current path
            return current_path

        # else

        if current_word not in visited:
            visited.add(current_word)

            neighbors = getNeighbors(current_word)

            for neighbor in neighbors:
                path_copy = current_path[:]
                path_copy.append(neighbor)
                q.enqueue(path_copy)

# step 3:
# choose and run your algorithm: BFS




## 4/13/2020 lecture
# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:


islands = [[0, 1, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 0, 0]]
island_counter(islands) # returns 4