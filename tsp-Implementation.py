import matplotlib.pyplot as plt
import numpy             as np


city_coords = [
    (40.7128, -74.0060),  # 0 New York
    (34.0522, -118.2437), # 1 Los Angeles
    (41.8781, -87.6298),  # 2 Chicago
    (44.9778, -93.2650),  # 3 Minneapolis
    (39.7392, -104.9903), # 4 Denver
    (32.7767, -96.7970),  # 5 Dallas
    (47.6062, -122.3321), # 6 Seattle
    (42.3601, -71.0589),  # 7 Boston
    (37.7749, -122.4194), # 8 San Francisco
    (38.6270, -90.1994),  # 9 St. Louis
    (29.7604, -95.3698),  # 10 Houston
    (33.4484, -112.0740), # 11 Phoenix
    (40.7608, -111.8910), # 12 Salt Lake City
]


city_names = [
    "New York",
    "Los Angeles",
    "Chicago",
    "Minneapolis",
    "Denver",
    "Dallas",
    "Seattle",
    "Boston",
    "San Francisco",
    "St. Louis",
    "Houston",
    "Phoenix",
    "Salt Lake City"
]


def create_data_model():
    data = {}

    data["distance_matrix"] = [
        [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
        [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
        [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
        [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
        [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371],
        [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999],
        [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701],
        [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099],
        [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600],
        [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0, 679, 1272, 1162],
        [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, 0, 1017, 1200],
        [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, 0, 504],
        [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, 0],
    ]

    data["depot"] = 0
    return data


def tsp_nearest_neighbor(distance_matrix, start):
    n = len(distance_matrix)
    visited = [False] * n
    visited[start] = True

    route = [start]
    current = start

    for _ in range(n - 1):
        best_dist = float("inf")
        next_city = None

        for city in range(n):
            if not visited[city] and distance_matrix[current][city] < best_dist:
                best_dist = distance_matrix[current][city]
                next_city = city

        visited[next_city] = True
        route.append(next_city)
        current = next_city

    return route


def compute_route_distance(route, matrix):
    total = 0

    for i in range(len(route) - 1):
        total += matrix[route[i]][route[i + 1]]

    total += matrix[route[-1]][route[0]]
    return total


def print_solution(route, distance):
    route_str = " -> ".join(str(c) for c in route)
    route_str += f" -> {route[0]}"

    print(F"Route solution: {route_str}")
    print(f"Route distance: {distance} miles")


def plot_comparison(route, coords):
    coords = np.array(coords)
    xs = coords[:, 1]
    ys = coords[:, 0]

    fig, axes = plt.subplots(1, 2, figsize=(16, 7))

    # Left display
    ax = axes[0]
    ax.scatter(xs, ys, c='red')

    for i, (lat, lon) in enumerate(coords):
        ax.text(
            lon + 0.4,
            lat + 0.4,
            f"[{i}] {city_names[i]}",
            fontsize=9,
            bbox=dict(facecolor="white", alpha=0.6, edgecolor="none")
        )

    ax.set_title("TSP Route Points")
    ax.grid(True)
    ax.set_xticks([])
    ax.set_yticks([])

    # Right display
    ax = axes[1]
    ax.scatter(xs, ys, c='red')

    for i, (lat, lon) in enumerate(coords):
        ax.text(
            lon + 0.4,
            lat + 0.4,
            f"[{i}] {city_names[i]}",
            fontsize=9,
            bbox=dict(facecolor="white", alpha=0.6, edgecolor="none")
        )

    for i in range(len(route)):
        c1 = route[i]
        c2 = route[(i + 1) % len(route)]
        x1, y1 = coords[c1][1], coords[c1][0]
        x2, y2 = coords[c2][1], coords[c2][0]
        ax.plot([x1, x2], [y1, y2])

    ax.set_title("TSP Route Solution")
    ax.grid(True)
    ax.set_xticks([])
    ax.set_yticks([])

    plt.tight_layout()
    plt.show()


def main():
    data = create_data_model()
    matrix = data["distance_matrix"]
    start = data["depot"]

    route = tsp_nearest_neighbor(matrix, start)
    total_distance = compute_route_distance(route, matrix)

    print_solution(route, total_distance)
    plot_comparison(route, city_coords)


if __name__ == "__main__":
    main()
