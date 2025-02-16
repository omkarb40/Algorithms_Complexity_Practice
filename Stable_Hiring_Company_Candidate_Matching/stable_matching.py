#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    company_prefs = []

    for _ in range(n):
        company_prefs.append(list(map(int, input().rstrip().split())))

    candidate_prefs = []

    for _ in range(n):
        candidate_prefs.append(list(map(int, input().rstrip().split())))

    # Write your code here
    candidate_match = [-1] * n
    next_proposal_index = [0] * n
    free_companies = list(range(n))
    
    while free_companies:
        company = free_companies[0]
        candidate = company_prefs[company][next_proposal_index[company]]
        next_proposal_index[company] += 1
        
        if candidate_match[candidate] == -1:
            candidate_match[candidate] = company
            free_companies.pop(0)
        else:
            current_company = candidate_match[candidate]
            current_rank = candidate_prefs[candidate].index(current_company)
            new_rank = candidate_prefs[candidate].index(company)
            
            if new_rank < current_rank:
                candidate_match[candidate] = company
                free_companies.pop(0)
                free_companies.append(current_company)
    
    for candidate in range(n):
        print(candidate, candidate_match[candidate])