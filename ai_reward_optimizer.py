import time
import random

class AIRewardOptimizer:
    def __init__(self, base_reward=100, volatility_factor=0.1):
        self.base_reward = base_reward
        self.volatility_factor = volatility_factor

    def get_market_conditions(self):
        staking_volume = random.uniform(5000, 20000) 
        volatility = random.uniform(0.05, 0.3)
        return staking_volume, volatility

    def calculate_dynamic_reward(self, user_stake, staking_duration):
        staking_volume, volatility = self.get_market_conditions()
        duration_multiplier = 1 + (staking_duration / 365.0)
        volatility_adjustment = 1 + (volatility - self.volatility_factor)
        reward = self.base_reward * (user_stake / 1000) * duration_multiplier * volatility_adjustment * (1 + volatility) 
        if user_stake < 0:
            raise ValueError("User stake must be non-negative.") 
        return max(10, reward)

optimizer = AIRewardOptimizer()
user_stake = 1500 
staking_duration = 90 
reward = optimizer.calculate_dynamic_reward(user_stake, staking_duration)
print(f"Optimized Reward: {reward}")
