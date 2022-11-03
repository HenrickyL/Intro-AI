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

def runSearch(algorithm, origin,target, solutions):
    res = algorithm(origin,target)
    solutions['Origem'].append(origin)
    solutions['Solução'].append(res.fatherPath())
    solutions['Custo'].append(res.cost)




def runAllAlgorithm():
  result = {
  }
  for name,func in algorithms.items():
    solutions = {
      'Origem': [],
      'Solução': [],
      'Custo': []
      }
    for origin in origins:
      runSearch(func, origin,destiny,solutions)
    result[name] = solutions
  return result

res = runAllAlgorithm()

import pandas as pd

with open('searchLab.tex','a') as file:
  for key,value in res.items():
    file.write(f'{key}\n')
    pd.DataFrame(res[key]).style.hide(axis='index').to_latex(file, encoding='utf-8')
    file.write(f'{key}\n')