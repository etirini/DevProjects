from collections import deque
from re import search

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["thom"] = []
graph["jonny"] = []
graph["peggy"] = []

def search(name):
    search_queue = deque()
    search_queue += graph["you"]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print (person + " is a mango seller")
                return True
            else: 
                search_queue += graph[person]
                searched.append(person)
                print(person)
    return False

def person_is_seller(name):
    return name[-1] == 'm'

search("you")
