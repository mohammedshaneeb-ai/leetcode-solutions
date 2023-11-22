""" Q:1184 = A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops."""


def distanceBetweenBusStops(distance, start, destination) -> int:
        if start == destination:
            return 0
        
        if start < destination:
            clockwise_distance = sum(distance[start:destination])
        else:
            clockwise_distance = sum(distance[start:] + distance[:destination])

        total_distance = sum(distance)
        shortest_distance = min(clockwise_distance, total_distance - clockwise_distance)
        return shortest_distance


# Example 1 
distance = [1,2,3,4]
start = 0
destination = 1
# Expected Output: 1


# Example 2
distance = [1,2,3,4]
start = 0
destination = 2
# Expected Output: 3


# Example 3
distance = [1,2,3,4]
start = 0
destination = 3
# Expected Output: 4


print(distanceBetweenBusStops(distance,start,destination))