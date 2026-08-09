def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    assignments = []

    for point in points:
        min_distance = float('inf')
        best_centroid = -1

        for j, centroid in enumerate(centroids):
            # Squared Euclidean distance
            distance = sum(
                (point[d] - centroid[d]) ** 2
                for d in range(len(point))
            )

            if distance < min_distance:
                min_distance = distance
                best_centroid = j

        assignments.append(best_centroid)

    return assignments