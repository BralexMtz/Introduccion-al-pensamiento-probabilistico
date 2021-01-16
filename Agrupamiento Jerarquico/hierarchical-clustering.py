import random


def distance(p1,p2):
    x=p1[0]-p2[0]
    y=p1[1]-p2[1]
    return ( x**2 + y**2)**(0.5)

class Cluster():
    def __init__(self,point):
        self.points=[]
        self.points.append(point)
    
    def __get_all_distances(self,o_cluster):
        distancias=[]
        for p in self.points:
            for o_p in o_cluster.points:
                distancias.append(distance(p,o_p))
        return distancias

    def get_distance(self,cluster,method):
        all_distances=self.__get_all_distances(cluster)
        if method == 1: # Single linkage
            return min(all_distances)
        if method == 2: # Complete linkage
            return max(all_distances)
        if method == 3: # Average linkage
            return sum(all_distances)/len(all_distances) # is the same get average of distances than average of coordenates, and then get distance?
    def add_cluster(self,cluster):
        for p in cluster.points:
            self.points.append(p)
    def __str__(self):
        return str(self.points)
def create_points(num_points):
    points=[]
    for _ in range(num_points):
        x = random.random()*10
        y = random.random()*10
        points.append( (x,y) )
    return points

def find_cluster(clusters,method):
    print("\n"+"-"*15)
    for c in clusters:
        print(c,end="    ")
    
    distance = 1000000000
    couple = (0,0)
    if len(clusters)==1:
        return clusters[0]
    for i in range(len(clusters)):
        for j in range(len(clusters)):
            distance_result = clusters[i].get_distance(clusters[j], method)
            if (distance_result < distance) and i != j:
                distance = distance_result
                couple = (i,j)
    clusters[couple[0] ].add_cluster(clusters[couple[1]])
    clusters.pop(couple[1])
    return find_cluster(clusters,method)

def main(distance_method,num_points):
    points=create_points(num_points)
    clusters=[ Cluster(p) for p in points ]
    
    find_cluster(clusters,distance_method)
    print()

if __name__ == "__main__":
    print("Elige el método de distancia")
    distance_method=int(input(" 1. Single linkage \n 2. Complete linkage \n 3. Average linkage\n > "))
    num_points=int(input("Numero de puntos: "))
    main(distance_method,num_points)


