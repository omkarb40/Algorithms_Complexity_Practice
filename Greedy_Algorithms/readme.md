# Server Load Balancing System

### Overview
This implementation provides a sophisticated solution for distributing tasks across multiple servers while maintaining optimal load balance. The system employs a greedy algorithm that considers both server utilization and available capacity when making distribution decisions. A key feature of this implementation is its ability to handle server failures gracefully by redistributing tasks across remaining servers, with support for task splitting when necessary.

### Technical Implementation Details

#### Core Components
The system consists of two main classes that work together to manage load balancing:

The Server class manages individual server operations and maintains server state. Each server tracks its:
- Maximum capacity
- Current load
- List of assigned tasks
- Current utilization percentage
- Available capacity

The LoadBalancer class orchestrates the entire system by:
- Managing multiple servers
- Distributing incoming tasks
- Handling server failures
- Maintaining system-wide load balance
- Providing detailed system state information

### Logic and Features
Task Distribution Algorithm:
The implementation uses an enhanced greedy approach that sorts tasks by size (largest first) and assigns them to servers based on both utilization and available capacity. This ensures efficient use of server resources while maintaining balanced load distribution.

Server Selection Strategy:
When selecting a server for task assignment, the system considers:
- Current server utilization
- Available capacity
- Ability to handle the task without exceeding capacity

Failure Handling:
The system implements a robust failure handling mechanism that:
- Detects server failures
- Collects tasks from the failed server
- Sorts tasks by size for optimal redistribution
- Supports task splitting across multiple servers if necessary
- Includes rollback capabilities if redistribution fails
