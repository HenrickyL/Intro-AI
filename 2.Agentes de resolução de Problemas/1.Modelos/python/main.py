from map import Map
map = Map.readData('data.txt')
ini ='Arad'
fin = 'Bucharest'
bfsRes = Map.bfs(map,ini, fin)
print('-----------------')
dfsRes = Map.dfs(map,ini, fin)
print('-----------------')
ucsRes = Map.ucs(map,ini, fin)
print('-----------------')

distanceMap = Map.readDistanceMap('bucharest_dist.json')

gcs = Map.gcs(map, ini, fin, distanceMap)
print('-----------------')
aStar = Map.aStar(map, ini, fin, distanceMap)
print('-----------------')

bfsRes.fatherPath()
dfsRes.fatherPath()
ucsRes.fatherPath()
gcs.fatherPath()
aStar.fatherPath()