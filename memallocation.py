def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    block_copy = blocks[:]

    for i, p in enumerate(processes):
        for j, b in enumerate(block_copy):
            if b >= p:
                allocation[i] = j
                block_copy[j] -= p
                break
    print("\nFIRST FIT ALLOCATION:")
    for i, a in enumerate(allocation):
        if a != -1:
            print(f"Process {i+1} (size {processes[i]}) -> Block {a+1}")
        else:
            print(f"Process {i+1} (size {processes[i]}) -> Not allocated")

def best_fit(blocks, processes):
    allocation = [-1] * len(processes)
    block_copy = blocks[:]

    for i, p in enumerate(processes):
        best_index = -1
        for j, b in enumerate(block_copy):
            if b >= p:
                if best_index == -1 or block_copy[j] < block_copy[best_index]:
                    best_index = j
        if best_index != -1:
            allocation[i] = best_index
            block_copy[best_index] -= p
    print("\nBEST FIT ALLOCATION:")
    for i, a in enumerate(allocation):
        if a != -1:
            print(f"Process {i+1} (size {processes[i]}) -> Block {a+1}")
        else:
            print(f"Process {i+1} (size {processes[i]}) -> Not allocated")

def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)
    block_copy = blocks[:]

    for i, p in enumerate(processes):
        worst_index = -1
        for j, b in enumerate(block_copy):
            if b >= p:
                if worst_index == -1 or block_copy[j] > block_copy[worst_index]:
                    worst_index = j
        if worst_index != -1:
            allocation[i] = worst_index
            block_copy[worst_index] -= p
    print("\nWORST FIT ALLOCATION:")
    for i, a in enumerate(allocation):
        if a != -1:
            print(f"Process {i+1} (size {processes[i]}) -> Block {a+1}")
        else:
            print(f"Process {i+1} (size {processes[i]}) -> Not allocated")

# Input data
blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426, 420]

# Run all strategies
first_fit(blocks, processes)
best_fit(blocks, processes)
worst_fit(blocks, processes)