class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        births = [x[0] for x in logs]
        deaths = [x[1] for x in logs]
        first_birth = min(births)
        last_death = max(deaths)
        years_pop = [0]*(last_death - first_birth + 1)
        for year in births:
            years_pop[year-first_birth] += 1
        for year in deaths:
            years_pop[year-first_birth] -= 1
        max_pop_year = first_birth
        pop = years_pop[0]
        for idx in range(last_death - first_birth + 1):
            if idx > 0:
                years_pop[idx] += years_pop[idx-1]
            if years_pop[idx] > pop:
                pop = years_pop[idx]
                max_pop_year = first_birth + idx 
        return max_pop_year