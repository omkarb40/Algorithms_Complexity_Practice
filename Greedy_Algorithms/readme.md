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

### Sample Program Input
Initial Distribution
--------------------------------------------------------------------------------
Server     Capacity   Load       Utilization  Tasks
--------------------------------------------------------------------------------
S1         100        45         45.00%      [45]
S2         80         50         62.50%      [50]
S3         120        75         62.50%      [75]
S4         90         30         33.33%      [30]
S5         110        40         36.36%      [40]
S6         70         60         85.71%      [60]

### Sample Program Output
Initial Distribution
--------------------------------------------------------------------------------
Server     Capacity   Load       Utilization  Tasks
--------------------------------------------------------------------------------
S1         100        75         75.00%      [75]
S2         80         60         75.00%      [60]
S3         120        50         41.67%      [50]
S4         90         45         50.00%      [45]
S5         110        40         36.36%      [40]
S6         70         30         42.86%      [30]

Simulating failure of server S3...

Distribution After S3 Failure
--------------------------------------------------------------------------------
Server     Capacity   Load       Utilization  Tasks
--------------------------------------------------------------------------------
S1         100        75         75.00%      [75]
S2         80         60         75.00%      [60]
S4         90         45         50.00%      [45]
S5         110        90         81.82%      [40, 50]
S6         70         30         42.86%      [30]