import random


def distance(p1,p2):
    x=p1[0]-p2[0]
    y=p1[1]-p2[1]
    return ( x**2 + y**2)**(0.5)

class Cluster():
    def __init__(self,center):
        self.points=[]
        self.center=center
    
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
    def exist_point(self,p_new):
        for p in self.points:
            if p[0]==p_new[0] and p[1]==p_new[1]:
                return True
        return False

    def add_point(self,p):
        self.points.append(p)
    def recenter(self):
        x=0
        y=0
        for p in self.points:
            x+=p[0]
            y+=p[1]
        x/=len(self.points)
        y/=len(self.points)
        self.center=(x,y)
    def del_point(self,p):
        self.points.remove(p)

    def __str__(self):
        return str(self.points)


def create_points(num_points):
    points=[]
    for _ in range(num_points):
        x = random.random()*10
        y = random.random()*10
        points.append( (x,y) )
    return points



def main(num_points,num_cent):
    points=create_points(num_points)  # creating dump data
    centroids=create_points(num_cent) # creating centroids
    
    clusters=[ Cluster(c) for c in centroids ]
    change_points=True
    while change_points:
        change_points=False
        for p in points:
            distances=[]
            for c in clusters:
                distances.append(distance(p,c.center))
            min_distance=min(distances)
            index_cl=distances.index(min_distance)
            if not clusters[index_cl].exist_point(p):
                for c in clusters:
                    if c.exist_point(p):
                        c.del_point(p)
                change_points=True
                clusters[index_cl].add_point(p)
        
        for c in clusters:
            c.recenter()
        print("centroide:",c.center,"points:",c.points)
        print()
    

if __name__ == "__main__":
    num_points=int(input("Numero de puntos: "))
    num_cent=int(input("Numero de centroides: "))
    main(num_points,num_cent)


