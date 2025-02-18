class Server:
    def __init__(self, name: str, capacity: int):
        """
        Initializing a server with its capacity and task list.
        
        The server keeps track of its current load and maintains a list of assigned tasks.
        """
        self.name = name
        self.capacity = capacity
        self.tasks = []
        self.current_load = 0

    def can_add_task(self, task_load: int) -> bool:
        """
        Verifying if a task can be added without exceeding server capacity.
        Ensuring we never overload a server beyond its specified limits.
        """
        return self.current_load + task_load <= self.capacity

    def add_task(self, task_load: int) -> bool:
        """
        Adding a task to the server if capacity allows.
        Returns True if task was added successfully, False otherwise.
        """
        if self.can_add_task(task_load):
            self.tasks.append(task_load)
            self.current_load += task_load
            return True
        return False

    def get_utilization(self) -> float:
        """
        Calculating server utilization as a percentage.
        This helps in determining the most suitable server for new tasks.
        """
        return (self.current_load / self.capacity) * 100 if self.capacity > 0 else 0


class LoadBalancer:
    def __init__(self):
        """Initialize the load balancer with an empty server dictionary."""
        self.servers = {}

    def add_server(self, name: str, capacity: int):
        """
        Add a new server to the load balancer.
        """
        if capacity <= 0:
            raise ValueError("Server capacity must be positive.")
        if name in self.servers:
            raise ValueError(f"Server {name} already exists.")
        self.servers[name] = Server(name, capacity)

    def find_best_server_for_task(self, task_load: int) -> Server:
        """
        Finding the most suitable server for a task based on current utilization.
        """
        # Filtering servers that can handle the task
        available_servers = [
            server for server in self.servers.values()
            if server.can_add_task(task_load)
        ]
        
        if not available_servers:
            raise ValueError(f"No server can accommodate task of size {task_load}")
        
        # Choosing server with lowest utilization to ensure balanced distribution
        return min(available_servers, key=lambda s: s.get_utilization())

    def distribute_tasks(self, tasks: dict) -> dict:
        """
        Distributeing tasks among servers using an improved greedy approach.
        This version focuses on maintaining balanced load across all servers.
        
        Args:
            tasks: Dictionary mapping task identifiers to their load values
        Returns:
            Current distribution of tasks across all servers
        """
        if not self.servers:
            raise ValueError("No servers available for task distribution.")

        # Input validation
        for task_id, task_load in tasks.items():
            if task_load <= 0:
                raise ValueError(f"Task load must be positive: {task_id}")

        # Sorting tasks by size (largest first) for better distribution
        sorted_tasks = sorted(
            [(task_id, load) for task_id, load in tasks.items()],
            key=lambda x: x[1],
            reverse=True
        )

        # Distributing each task to the server with lowest utilization
        for task_id, task_load in sorted_tasks:
            try:
                best_server = self.find_best_server_for_task(task_load)
                if not best_server.add_task(task_load):
                    raise ValueError(f"Failed to add task {task_id} to selected server")
            except ValueError as e:
                raise ValueError(f"Task distribution failed: {str(e)}")

        return self.get_current_distribution()

    def handle_server_failure(self, failed_server: str) -> dict:
        """
        Handling server failure by redistributing its tasks to remaining servers.
        """
        if failed_server not in self.servers:
            raise ValueError(f"Server {failed_server} not found.")

        # Storing failed server's tasks and remove it from active servers
        failed_tasks = sorted(self.servers[failed_server].tasks, reverse=True)
        failed_capacity = self.servers[failed_server].capacity
        self.servers.pop(failed_server)

        if not self.servers:
            raise ValueError("No remaining servers available for task redistribution.")

        # Creating redistribution tasks dictionary
        redistribution_tasks = {
            f"failed_task_{i}": task_load 
            for i, task_load in enumerate(failed_tasks)
        }

        try:
            # Attempt to redistribute tasks
            return self.distribute_tasks(redistribution_tasks)
        except ValueError as e:
            # Restoring failed server if redistribution fails
            self.servers[failed_server] = Server(failed_server, failed_capacity)
            for task in failed_tasks:
                self.servers[failed_server].add_task(task)
            raise ValueError(f"Failed to redistribute tasks: {str(e)}")

    def get_current_distribution(self) -> dict:
        """
        Get the current distribution of tasks across all servers.
        Returns detailed information about each server's state.
        """
        return {
            name: {
                'capacity': server.capacity,
                'current_load': server.current_load,
                'utilization': server.get_utilization(),
                'tasks': server.tasks
            }
            for name, server in sorted(self.servers.items())
        }


def print_distribution(distribution: dict, title: str = "Current Distribution"):
    """
    Print the current task distribution in a formatted manner.
    """
    print(f"\n{title}")
    print("-" * 80)
    print(f"{'Server':<10} {'Capacity':<10} {'Load':<10} {'Utilization':<12} Tasks")
    print("-" * 80)
    
    for server, info in sorted(distribution.items()):
        print(f"{server:<10} {info['capacity']:<10} {info['current_load']:<10} "
              f"{info['utilization']:.2f}%      {info['tasks']}")


def main():
    """
    Main function to demonstrate the load balancer's functionality
    using the server configuration from the assignment.
    """
    # Initialize load balancer
    lb = LoadBalancer()
    
    # Server configuration from assignment
    servers_data = {
        'S1': {'capacity': 100, 'tasks': 45},
        'S2': {'capacity': 80, 'tasks': 50},
        'S3': {'capacity': 120, 'tasks': 75},
        'S4': {'capacity': 90, 'tasks': 30},
        'S5': {'capacity': 110, 'tasks': 40},
        'S6': {'capacity': 70, 'tasks': 60}
    }
    
    try:
        # Add servers to load balancer
        for name, data in servers_data.items():
            lb.add_server(name, data['capacity'])
        
        # Perform initial task distribution
        initial_tasks = {
            name: data['tasks'] 
            for name, data in servers_data.items()
        }
        initial_distribution = lb.distribute_tasks(initial_tasks)
        print_distribution(initial_distribution, "Initial Distribution")
        
        # Simulate and handle server failure
        print("\nSimulating failure of server S3...")
        new_distribution = lb.handle_server_failure('S3')
        print_distribution(new_distribution, "Distribution After S3 Failure")
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()