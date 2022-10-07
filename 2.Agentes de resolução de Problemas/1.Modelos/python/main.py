from map import Map
map = Map.readData('data.txt')

bfsRes = Map.bfs(map,'Arad', 'Bucharest')
dfsRes = Map.dfs(map,'Arad', 'Bucharest')

bfsRes.fatherPath()
dfsRes.fatherPath()