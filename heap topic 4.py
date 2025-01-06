import heapq

# Example usage of Min-Heap
orders = [(3, "Order 3"), (1, "Order 1"), (2, "Order 2")]

heapq.heapify(orders)
print("Heapified Orders:")
print(orders)

# Adding a new order
heapq.heappush(orders, (4, "Order 4"))
print("After Adding Order 4:")
print(orders)

# Extracting the highest-priority order
highest_priority = heapq.heappop(orders)
print("Highest Priority Order:")
print(highest_priority)
