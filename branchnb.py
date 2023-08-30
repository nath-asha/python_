import numpy as np

def calculate_bound(cost_matrix, assignment):
    total_bound = 0
    assigned_agents = set()
    assigned_tasks = set()

    for agent, task in assignment.items():
        total_bound += cost_matrix[agent, task]
        assigned_agents.add(agent)
        assigned_tasks.add(task)

    unassigned_agents = set(range(len(cost_matrix))) - assigned_agents
    unassigned_tasks = set(range(len(cost_matrix))) - assigned_tasks

    for agent in unassigned_agents:
        min_cost = min(cost_matrix[agent, task] for task in unassigned_tasks)
        total_bound += min_cost

    return total_bound

def branch_and_bound(cost_matrix):
    n = len(cost_matrix)
    best_assignment = {}
    best_cost = float('inf')
    stack = [(0, {})]  # Initialize the stack with the root node

    while stack:
        level, assignment = stack.pop()

        if level == n:
            current_cost = sum(cost_matrix[i, assignment[i]] for i in range(n))
            if current_cost < best_cost:
                best_assignment = assignment.copy()
                best_cost = current_cost
        else:
            for task in range(n):
                if task not in assignment.values():
                    new_assignment = assignment.copy()
                    new_assignment[level] = task
                    bound = calculate_bound(cost_matrix, new_assignment)
                    if bound < best_cost:
                        stack.append((level + 1, new_assignment))

    return best_assignment, best_cost

# Example cost matrix where rows represent agents and columns represent tasks
cost_matrix = np.array([
    [9, 2, 7,8],
    [6, 4, 3,7],
    [5, 8, 1,8],
    [7, 6, 9,4],
])

best_assignment, best_cost = branch_and_bound(cost_matrix)

print("Assigned tasks:")
for agent, task in best_assignment.items():
    print(f"Agent {agent} is assigned to Task {task}")

print("Total cost:", best_cost)