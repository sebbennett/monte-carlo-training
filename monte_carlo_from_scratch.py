import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



class FinancialStock:
    
    def generate_stock_value(self, method='random_uniform', limits:tuple=(100,1000)):
        if method == 'random_uniform':
            self.value = round(np.random.uniform(limits[0], limits[1]),2)
            self.starting_value = self.value
        elif method == 'gaussian':
            self.value = round(np.random.normal(limits[0], limits[1]),2)
            self.starting_value = self.value
        else:
            raise ValueError(f'Method {method} is not known')
            
    def check_stock_value(self):
        print(f"Stock value of this stock is {self.value}")
        return self.value
    
    def generate_stock_price_changes(self):
        p = np.random.uniform(0,1)
        multiplier = np.random.normal(1, 0.2)
        print(f"Multiplier = {multiplier}")
        self.value *= multiplier

        
if __name__=='__main__':
    fs = FinancialStock()
    fs.generate_stock_value()
    print(f"{fs.starting_value}")
    
    output = []
    for _ in range(10000):
        fs.generate_stock_value('gaussian',limits=(17, 2.8))
        output.append(fs.value)

    plt.hist(output)
