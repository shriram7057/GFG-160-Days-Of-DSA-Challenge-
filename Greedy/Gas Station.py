class Solution:
    def startStation(self, gas, cost):
        total_gas = 0
        total_cost = 0
        tank = 0
        start_index = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]

            if tank < 0:
                start_index = i + 1
                tank = 0

        if total_gas < total_cost:
            return -1
        return start_index
