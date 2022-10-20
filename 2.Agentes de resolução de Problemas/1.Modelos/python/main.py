from map import Map
map = Map.readData('data.txt')
ini ='Lugoj'
fin = 'Pitesti'
bfsRes = Map.bfs(map,ini, fin)
print('-----------------')
dfsRes = Map.dfs(map,ini, fin)
print('-----------------')
ucsRes = Map.ucs(map,ini, fin)
print('-----------------')

bfsRes.fatherPath()
dfsRes.fatherPath()
ucsRes.fatherPath()