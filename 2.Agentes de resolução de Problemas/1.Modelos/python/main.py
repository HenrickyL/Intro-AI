from map import Map
map = Map.readData('data.txt')

res = Map.bds(map,'Arad', 'Bucharest')

print(res)