#Dijkstra's Algorithm Implementation

cities=["Atlanta", "Chattanooga", "Macon", "Birmingham", "Montgomery", "Savannah","Augusta", "Greenville", "Knoxville", "Charlotte", "Columbia", "Memphis", "Nashville", "Jackson", "Mobile", "Pensacola", "Jacksonville", "Orlando", "Tampa", "New Orleans"]

graph = [
    [(2,104),(8,140),(7,139),(3,73),(5,154),(4,141)], #Atlanta 1
    [(9,102),(1,104),(4,139),(13,121)], #Chattanooga 2
    [(1,73),(6,155),(19,362)], #Macon 3
    [(13,180),(2,139),(1,141),(5,86),(20,325),(12,217)], #Birmingham 4
    [(4,86),(1,154),(15,170)], #Montgomery 5
    [(11,154),(17,126),(3,155)], #Savannah 6
    [(1,139),(11,67)], #Augusta 7
    [(1,140),(9,169),(10,96)], #Greenville 8
    [(13,167),(2,102),(8,169)], #Knoxville 9
    [(11,87),(8,96)], #Charlotte 10
    [(10,87),(6,154),(7,67)], #Columbia 11
    [(13,197),(4,217),(14,201)], #Memphis 12
    [(9,167),(2,121),(4,180),(12,197)], #Nashville 13
    [(12,201),(20,184)], #Jackson 14
    [(5,170),(16,48),(20,139)], #Mobile 15
    [(17,341),(15,48)], #Pensacola 16
    [(6,126),(18,133),(16,341)], #Jacksonville 17
    [(17,133),(19,78)], #Orlando 18
    [(18,78),(3,362)], #Tampa 19
    [(14,184),(4,325),(15,139)] #New Orleans 20
]


dist=[]
prev=[]
queue=[]

def mindist_vertex(q):
    mindist = 100000000000
    for i in q:
        if dist[i] < mindist:
            mindist = dist[i]
            min = i
    return min

def length(u,v):
    for (i,j) in graph[u]:
        if i==v:
            return j

def Dijkstra(graph, source):
    for i in range(len(graph)):
        dist.append(10000000)
        prev.append(None)
        queue.append(i)
    dist[source-1] = 0

    print(f"initial distances: {dist}")
    print(f"initial prev vertices: {prev}")
    print(f"initial vertex queue: {[x+1 for x in queue]}")
    print()

    while(len(queue)!=0):
        u = mindist_vertex(queue)
        queue.remove(u)
        print(f"current vertex queue: {[x+1 for x in queue]}")
        print(f"Looking at vertex {u+1}'s unsearched neighbors ({cities[u]})")
        for v in [x for x in graph[u] if x[0]-1 in queue]:
            print(f"\tLooking at edge ({u+1}, {v[0]}) with length {length(u,v[0])} ({cities[v[0]-1]})")
            alt = dist[u]+length(u,v[0])
            if alt < dist[v[0]-1]:
                dist[v[0]-1] = alt
                prev[v[0]-1] = u+1
                print(f"\t\t table for vertex {v[0]} updated: new dist={alt} new prev={u+1}")
        print(f"current dist table: {dist}")
        print(f"current prev table: {prev}")
        print()

    return dist, prev

dist_result, prev_result = Dijkstra(graph, 1)
print("Final result of running Dijkstra's algorithm")
print(f"dist table: {dist_result}")
print(f"prev table: {prev_result}")

print("\nCity, Shortest Distance, Previous City")
for i in range(len(cities)):
    print(f"{cities[i]}, {dist_result[i]}, {cities[prev_result[i]-1] if prev_result[i]!=None else None}")