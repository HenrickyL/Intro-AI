from asyncio import sleep
import sys
from time import time
from typing import Callable
from map import Map
from node import Node

map = Map.readData('data.txt')
origins =['Neamt','Eforie','Lugoj','Arad','Vaslui','Oradea','Iasi','Timisoara']
destiny = 'Bucharest'
distanceMap = Map.readDistanceMap('bucharest_dist.json')

solutions : dict[str,(Node, float)]= {}
functions = [
  ['bfs',lambda o,d : Map.bfs(map,o,d)],
  ['ucs',lambda o,d : Map.ucs(map,o,d)],
  ['dfs',lambda o,d : Map.dfs(map,o,d)],
  ['gcs',lambda o,d : Map.gcs(map,o,d,distanceMap)],
  ['A*',lambda o,d : Map.aStar(map,o,d,distanceMap)],
]

def runSearch(algorithm: Callable[[str,str],Node], origins: list[str],target: str):
  for origin in origins:
    res = algorithm(origin,target)


def runAllAlgorithm():
  for name,func in functions:
    runSearch(func, origins,destiny)
