""" Q:1184 = A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops."""


def distanceBetweenBusStops(self, distance, start, destination) -> int:
        if start == destination:
            return 0
        
        if start < destination:
            clockwise_distance = sum(distance[start:destination])
        else:
            clockwise_distance = sum(distance[start:] + distance[:destination])

        total_distance = sum(distance)
        shortest_distance = min(clockwise_distance, total_distance - clockwise_distance)
        return shortest_distance