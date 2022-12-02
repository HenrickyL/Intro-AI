from map import Map
map = Map.readData('data.txt')
ini ='Oradea'
fin = 'Bucharest'
bfsRes = Map.bfs(map,ini, fin)
print('-----------------')
dfsRes = Map.dfs(map,ini, fin)
print('-----------------')
ucsRes = Map.ucs(map,ini, fin)
print('-----------------')

distanceMap = Map.readDistanceMap('bucharest_dist.json')

gcsRes = Map.gcs(map, ini, fin, distanceMap)
print('-----------------')
aStarRes = Map.aStar(map, ini, fin, distanceMap)
print('-----------------')

print(f"bfs: {bfsRes.cost} - "+bfsRes.fatherPath())
print(f"dfs: {dfsRes.cost} - "+dfsRes.fatherPath())
print(f"ucs: {ucsRes.cost} - "+ucsRes.fatherPath())
print(f"gcs: {gcsRes.cost} - "+gcsRes.fatherPath())
print(f"A*:  {aStarRes.cost} - "+aStarRes.fatherPath())