import math
import statistics

class County:
    def __init__(self, name, values):
        self.name = name
        self.values = values
    def distance(self, othervals):
        dist = 0
        for i in range(len(self.values)):
            dist += abs(float(self.values[i])-float(othervals.centroid[i]))
        return dist

class Cluster:
    def __init__(self):
        self.centroid = []
        self.contents = []
    def updateCentroid(self):
        clusterMeans = []
        for item in self.contents:
            items = [ float(i) for i in item.values ]
            itemMean = statistics.mean(items)
            clusterMeans.append(itemMean)
        return statistics.mean(clusterMeans)
    def names(self):
        names = ""
        for c in self.contents:
            names += c.name + "; "
        return names
    def clear(self):
        self.contents = []

def readData(filename):
    counties = []
    with open(filename, 'r') as f:
        data = f.readlines()[1:]
        for line in data:
            data = line.split(';')
            cleanData = [ float(c.strip()) for c in data[1:] ]
            county = County(data[0], cleanData[1:])
            counties.append(county)
    return counties

def initClusters(counties, num):
    clusters = []
    for i in range(num):
        newcluster = Cluster()
        newcluster.centroid = counties[i].values
        clusters.append(newcluster)
    return clusters

def placeCounties(counties, clusters):
    for county in counties:
        closestCluster = None
        closestDistance = float('inf')
        for cluster in clusters:
            distance = county.distance(cluster)
            if distance < closestDistance:
                closestDistance = distance
                closestCluster = cluster
        closestCluster.contents.append(county)


def updateCentroids(clusters):
    for c in clusters:
        c.updateCentroid()

def clearClusters(clusters):
    for c in clusters:
        c.clear()

def writeOutput(clusters, filename):
    with open(filename, 'w') as f:
        for i, cluster in enumerate(clusters):
            f.write('Cluster ' + str(i) + '\n')
            f.write('size: ' + str(len(cluster.contents)) + '\n')
            values = []
            for v in cluster.centroid:
                values.append(v)
            f.write(str(values) + '\n')
            countiesString = ''
            for c in cluster.contents:
                countiesString += c.name + '; '
            f.write(countiesString + '\n')
            f.write('\n')
    #your code here

def kmeans(infile, outfile, k, cycles):
    counties = readData(infile)
    clusters = initClusters(counties, k)
    for i in range(cycles):
        clearClusters(clusters)
        placeCounties(counties, clusters)
        updateCentroids(clusters)
    writeOutput(clusters, outfile)

kmeans("normalized_counties.txt", "output.txt", 30, 2)
