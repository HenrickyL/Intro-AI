import sys
from map import Map

map = Map.readData('data.txt')
origins =['Neamt','Eforie','Lugoj','Arad','Vaslui','Oradea','Iasi','Timisoara']
destiny = 'Bucharest'
distanceMap = Map.readDistanceMap('bucharest_dist.json')
algorithms = {
  'bfs':lambda o,d : Map.bfs(map,o,d),
  'ucs':lambda o,d : Map.ucs(map,o,d),
  'dfs':lambda o,d : Map.dfs(map,o,d),
  'gcs':lambda o,d : Map.gcs(map,o,d,distanceMap),
  'A*':lambda o,d : Map.aStar(map,o,d,distanceMap),
}
def runSearch(algorithm, origin,target):
  algorithms[algorithm](origin,target)


if __name__ == '__main__':
  _,algorithm, origin = sys.argv
  runSearch(algorithm, origin,destiny)