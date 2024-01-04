#!/usr/bin/env python
# coding: utf-8

# In[26]:


import numpy as np

class MinEditDist:
    def MED(self, s1, s2):
        m = len(s1)
        n = len(s2)
        self.arr = np.zeros((m+1, n+1), dtype=np.int8)
        
        for i in range(m+1):
            self.arr[i][0] = i
        for j in range(n+1):
            self.arr[0][j] = j

        for x in range(1, m+1):
            for y in range(1, n+1):
                if s1[x-1] == s2[y-1]:
                    self.arr[x][y] = self.arr[x-1][y-1]
                else:
                    self.arr[x][y] = min(self.arr[x-1][y-1], self.arr[x][y-1], self.arr[x-1][y]) + 1

        return self.arr[m][n]

    def describe_edit_steps(self, s1, s2):
        x, y = len(s1), len(s2)
        steps = []

        while x > 0 or y > 0:
            current_cost = self.arr[x][y]

            if x > 0 and y > 0 and s1[x-1] == s2[y-1]:
                steps.append(f"Match '{s1[x-1]}' at position {x}")
                x -= 1
                y -= 1
            elif x > 0 and y > 0 and self.arr[x-1][y-1] <= self.arr[x][y-1] and self.arr[x-1][y-1] <= self.arr[x-1][y]:
                steps.append(f"Substitute '{s1[x-1]}' at position {x} with '{s2[y-1]}'")
                x -= 1
                y -= 1
            elif y > 0 and (x == 0 or self.arr[x][y-1] <= self.arr[x-1][y-1] and self.arr[x][y-1] <= self.arr[x-1][y]):
                steps.append(f"Insert '{s2[y-1]}' at position {x+1}")
                y -= 1
            else:
                steps.append(f"Delete '{s1[x-1]}' at position {x}")
                x -= 1
                
        for num,step in enumerate(steps[::-1]):
            print(f"{num+1}. {step}")
            

# Example usage:
med_instance = MinEditDist()
s1 = "kitten"
s2 = "sitting"
med_result = med_instance.MED(s1, s2)
print(f"Minimum Edit Distance: {med_result}")
edit_steps = med_instance.describe_edit_steps(s1, s2)


# In[ ]:




