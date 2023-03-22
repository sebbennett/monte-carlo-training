import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



class FinancialStock:
    
    def generate_stock_value(self, method='random_uniform', limits:tuple=(100,1000)):
        if method == 'random_uniform':
            self.value = round(np.random.uniform(limits[0], limits[1]),2)
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



def update_line(hl, new_data):
    hl.set_xdata(np.append(hl.get_xdata(), new_data))
    hl.set_ydata(np.append(hl.get_ydata(), new_data))
    plt.draw()
        
if __name__=='__main__':
    pass
    # %matplotlib notebook
    
    
    fig, ax = plt.subplots()
    line, = ax.plot([]) 
    hl, = plt.plot([], [])
    
    def animate(frame_num):
        x = frame_num
        my_stock.generate_stock_price_changes()
        y = my_stock.value
        line.set_data((x, y))
        return line
    
    anim = FuncAnimation(fig, animate, frames=100, interval=20)
    plt.show()