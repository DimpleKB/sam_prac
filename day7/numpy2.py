
# import numpy as np

# array1 = np.array([[1, 2], [3, 4]]) 
# array2 = np.array([[1, 2], [3, 4]]) 

# print(array1 == array2) # Does element wise comparison and returns truth value for every comparison which is again stored in the respective sized np array

# comparison = (array1 == array2)
# equal_arrays = comparison.all() # Here all the truth values of the inferred np array is taken and if all are True then it returns True, else False.

# print(equal_arrays)

   


# import numpy as np

# # Problem1: Finding indices where spendings are greater than 100

# # Explanation: Using np.where() to find indices where the condition is met

# week_spendings = np.array([50, 120, 30, 40, 200, 90, 300])
# high_spend = np.where(week_spendings > 100)
# print(high_spend) # Output: Indices where the values are greater than 100




# import numpy as np
# week_spendings = np.array([50, 120, 30, 40, 200, 90, 300])
# highest_spending = max(week_spendings)
# print(highest_spending)



# import numpy as np
# week_spendings = np.array([50, 120, 30, 40, 200, 90, 300])
# index = 1
# big_spending = week_spendings[0]
# big_spending=max(week_spendings)
# index = np.argmax(week_spendings)
# days = {1:'mon', 2:'tue', 3:'wed', 4:'thus', 5:'fri', 6:'sat', 7:'sun'}
# print(big_spending, days[index+1])

# '''
# for i in range(len(week_spendings)):
# 	if week_spendings[i] > big_spending:
# 		big_spending = week_spendings[i]
# 		index = i
#         '''



# # Replacing values less than 50 with 0 in an array

# # Explanation: Using np.where() to replace values meeting the condition
# import numpy as np
# expenses = np.array([20, 60, 5, 80, 45, 90])
# modified_expenses = np.where(expenses < 50, 0, expenses)
# print(modified_expenses)  # Output: [ 0 60  0 80  0 90]




# #Generating random floating-point numbers between 0 and 1

# # Explanation: Using np.random.rand() to create a random array of given shape
# import numpy as np
# random_data = np.random.rand(3, 4) # Creates a 3x4 array with random values
# print(random_data)




# import random

# user_number = int(input('Enter a number of your choice between [0 and 9]: '))
# system_number = random.randint(0,10)
# if system_number == user_number:
# 	print('CrorePati')
# else:
# 	print('RoadPati')



# import pandas as pd

# def read_excel_file():
#     #Define the path to the Excel file
#     file_path = './students.xlsx'

#     # Read the Excel file into a pandas DataFrame
#     df = pd.read_excel(file_path)

# 	# Display the first few rows of the DataFrame
#     print(df.count())
#     print(df.head())
#     print(df.tail())

# def read_excel_file1():
#     file_path = './students.xlsx'
#     df = pd.read_excel(file_path)
#     for index, row in df.iterrows():
#         print(row[0], '  ', row[1])

# def read_excel_file2():
#     file_path = './students.xlsx'
#     df = pd.read_excel(file_path)
#     for index,row in df.iterrows():
#        print(row[1][0], row[1][1])

# read_excel_file()



# #Difference between np.arange() and np.linspace()

# # Explanation: np.arange() generates values with a fixed step, while np.linspace() generates a set number of equally spaced values
# import numpy as np
# sequence_arange = np.arange(1, 10, 3)  # Generates values from 1 to 10 with a step of 3
# sequence_linspace = np.linspace(0, 100, 5)  # Generates 5 equally spaced values between 0 and 100
# print("Using arange:", sequence_arange)
# print("Using linspace:", sequence_linspace)



# import numpy as np
# # Output of np.arange(1, 10, 3)

# # Explanation: np.arange() generates numbers starting at 1, stopping before 10, with step size 3

# sequence = np.arange(1, 10, 3)
# print(sequence)  # Output: [ 1  4  7]



# # Generating 23 equally spaced values between 0 and 100

# # Explanation: Using np.linspace() to generate specified number of values in a range
# import numpy as np
# values = np.linspace(0, 100, 23)
# print("Generated values:", values)
# print("Total count:", len(values))




# # Creating a DataFrame

# # Explanation: Using pandas to create a DataFrame from a dictionary

# import pandas as pd
# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 30, 35],
#         'Salary': [50000, 60000, 70000]}
# df = pd.DataFrame(data)
# print(df)




# # Reading a CSV file and checking for missing values

# # Explanation: Using pd.read_csv() to load data and checking for missing values using isnull()
# import pandas as pd
# df = pd.read_csv('learning\my_folder\sam_prac\day7\data.csv')  # Reads the CSV file
# df.head()  # Displays the first 5 rows
# print(df.isnull().sum())  # Counts missing values in each column




# # Filtering rows where Salary > 50000

# # Explanation: Using boolean indexing to filter rows based on Salary column

# import pandas as pd
# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 30, 35],
#         'Salary': [50000, 60000, 70000]}
# df = pd.DataFrame(data)
# # print(df)
# high_salary = df[df['Salary'] > 50000]  # Filters rows based on Salary
# print(high_salary)





# Sorting data by Salary in descending order

# Explanation: Using sort_values() to arrange rows based on Salary

# import pandas as pd
# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 30, 35],
#         'Salary': [50000, 60000, 70000]}
# df = pd.DataFrame(data)
# # print(df)
# df_sorted = df.sort_values(by='Salary', ascending=False)
# print(df_sorted)




# Grouping data by Age and calculating mean Salary

# Explanation: Using groupby() to aggregate data and compute mean salary
# import pandas as pd
# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 30, 35],
#         'Salary': [50000, 60000, 70000]}
# df = pd.DataFrame(data)
# grouped = df.groupby('Age')['Salary'].mean() 
# # Groups by Age and calculates mean salary
# print(grouped)

# # select avg(salary) as Avg_Salary from employees group by age;





# Creating a DataFrame from a dictionary

# Explanation: Creating a DataFrame using a dictionary with multiple columns
# import pandas as pd
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'Los Angeles', 'Chicago']
# }
# df = pd.DataFrame(data)  # Converts dictionary into a DataFrame
# print(df)




# Selecting a single column from a DataFrame

# Explanation: Accessing specific columns from the DataFrame
# import pandas as pd
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'Los Angeles', 'Chicago']
# }
# df = pd.DataFrame(data)  # Converts dictionary into a DataFrame
# # print(df)
# print(df['Name'])  # Access column using dictionary-style indexing
# print(df.Age)      # Access column using dot notation






# import numpy as  np
# np_array_data = np.array([[1, 2, 3, 4, 5,], [0, 2, 4, 6, 8], [1, 3, 5, 7, 9], [2, 3, 5, 7, 11], [11, 13, 17, 19, 23]], int)

# print(np_array_data[:, 3])
# print(np_array_data[1:4, 3])
# print(np_array_data[:, 2:3])
# print(np_array_data[1:, 1:4])



# Filtering rows in Pandas based on a condition

# Explanation: Using boolean indexing to filter rows where Age > 25
# import pandas as pd
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'Los Angeles', 'Chicago']
# }
# df = pd.DataFrame(data)  # Converts dictionary into a DataFrame
# # print(df)
# filtered_df = df[df['Age'] > 25]  # Selects rows where Age > 25
# print(filtered_df)



# Grouping data in a DataFrame and applying aggregate functions

# Explanation: Using groupby() and agg() to perform multiple aggregations on grouped data
# import pandas as pd
# data = {
#     'Department': ['IT', 'HR', 'IT', 'HR', 'IT'],
#     'Salary': [60000, 55000, 70000, 58000, 75000]
# }

# df = pd.DataFrame(data)

# # Grouping by Department and calculating mean, sum, and max salary
# grouped_df = df.groupby('Department').agg({'Salary': ['mean', 'sum', 'max']})  
# print(grouped_df)

# select department, avg(salary) as avg_salary from employees groupby dept having dept in['teaching', 'non-teaching']




# LINE PLOT
# Problem Statement: Visualizing a sine wave using a line plot.
# Question: How does a sine wave behave over a continuous range of values?

# import matplotlib.pyplot as plt
# import numpy as np
# # import seaborn as sns
# # import pandas as pd
# # from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

# x = np.linspace(0, 10, 100)  # Generating 100 points between 0 and 10
# y = np.sin(x)  # Sine function

# plt.plot(x, y, label="Sine Wave")  # Plot sine wave
# plt.xlabel("X-axis")  # Label for x-axis
# plt.ylabel("Y-axis")  # Label for y-axis
# plt.title("Line Plot")  # Title of the plot
# plt.legend()  # Display legend
# plt.show()  # Show the plot





# SCATTER PLOT
# Problem Statement: Understanding the correlation between two variables.
# Question: What pattern can we observe in the scatter plot of randomly generated values?

# import matplotlib.pyplot as plt
# import numpy as np
# # import seaborn as sns
# # import pandas as pd
# # from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

# x = np.random.rand(50)
# y = np.random.rand(50)

# plt.scatter(x, y, color='red', marker='o')
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Scatter Plot")
# plt.show()



# BAR PLOT
# Problem Statement: Comparing categorical data using a bar chart.
# Question: Which category has the highest value in the given dataset?


# import matplotlib.pyplot as plt
# import numpy as np
# # import seaborn as sns
# # import pandas as pd
# # from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

# categories = ['A', 'B', 'C', 'D']
# values = [10, 20, 15, 25]

# plt.bar(categories, values, color=['blue', 'green', 'red', 'purple'])
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.title("Bar Chart")
# plt.show()




# import numpy as np

# my_array = np.zeros((8, 8), dtype = int)
# #my_array[1::2, ::2] = 8
# #Starting from row-index-1 and there after, for all alternatives rows, and for all columns from index 0 and there after alternative columns, replace the cells with value 8
# my_array[::2, 1::2] = 1
# # Odd indexed-rows Even Indexed-Columns
# print(my_array)


# import numpy as np

# # nan is not a number

# print(0 * np.nan)
# print(np.nan == np.nan)
# print(np.inf > np.nan)
# print(np.nan - np.nan)
# print(np.nan in set([np.nan]))
# print(0.3 == 3 * 0.1)


# list1 = [2, 3, 5]

# string = ' '.join(map(str, list1)) # convert a list of items of tyep other than str into a string
# print(string)
# print(type(string))

# list2 = ['23', '55', '67']
# string = ' '.join(list2) 
# print(string)
# print(type(string))



# # Create a checkerboard 8x8 matrix using the tile function 
# import numpy as np

# #my_matrix = np.array([[0,1],[1,0]])
# #print(my_matrix)

# chess_board = np.tile( np.array([[1, 0],[0, 1]]), (4,4))
# # chess_board = np.tile( np.array([['*', ' '],[' ', '*']]), (4,4))
# #print('\n', chess_board)

# list1 = []
# for array in chess_board:
#     list1 = list(array)
#     string = ' '.join(map(str, list1))
#     print(string)



# # Normalize a 5x5 random matrix
# import numpy as np

# my_array = np.random.random((5,5))
# #print(my_array)

# values = my_array - np.mean (my_array)
# print('\n', values)

# values = np.std (my_array)
# print('\n', values)

# my_array = (my_array - np.mean (my_array)) / (np.std (my_array))
# print(my_array)





# HORIZONTAL BAR PLOT
# Problem Statement: Displaying categorical data with long labels in a horizontal format.
# Question: Which category has the highest value in the horizontal bar chart?


# import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns
# import pandas as pd
# from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

# categories = ['A', 'B', 'C', 'D']
# values = [10, 20, 15, 25]

# plt.barh(categories, values, color='orange')
# plt.xlabel("Values")
# plt.ylabel("Categories")
# plt.title("Horizontal Bar Chart")
# plt.show()




# HISTOGRAM
# Problem Statement: Analyzing the frequency distribution of normally distributed data.
# Question: How is the data distributed across different bins?


# import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns
# import pandas as pd
# from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

# data = np.random.randn(1000)

# plt.hist(data, bins=30, color='green', edgecolor='black')
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.title("Histogram")
# plt.show()




# LINE PLOT
# Problem Statement: Visualizing a sine wave using a line plot.
# Question: How does a sine wave behave over a continuous range of values?

# import matplotlib.pyplot as plt
# import numpy as np

# # Generate 100 points between 0 and 10
# x = np.linspace(0, 10, 100)  
# # Compute sine function values
# y = np.sin(x)  

# # Plot sine wave
# plt.plot(x, y, label="Sine Wave")  
# plt.xlabel("X-axis")  # Label for x-axis
# plt.ylabel("Y-axis")  # Label for y-axis
# plt.title("Line Plot")  # Title of the plot
# plt.legend()  # Display legend
# plt.show()  # Show the plot



# # SCATTER PLOT
# # Problem Statement: Understanding the correlation between two variables.
# # Question: What pattern can we observe in the scatter plot of randomly generated values?
# import numpy as np
# import matplotlib.pyplot as plt
# # Generate 50 random values for x and y
# x = np.random.rand(50)
# y = np.random.rand(50)

# # Create scatter plot
# plt.scatter(x, y, color='red', marker='o')
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Scatter Plot")
# plt.show()




# # PIE CHART
# # Problem Statement: Representing the market share of different brands.
# # Question: Which brand has the largest market share?
# import matplotlib.pyplot as plt
# # Define sizes and labels for pie chart
# sizes = [30, 20, 25, 25]
# labels = ['A', 'B', 'C', 'D']
# colors = ['blue', 'red', 'green', 'purple']

# # Create pie chart
# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
# plt.title("Pie Chart")
# plt.show()




# BOX PLOT
# Problem Statement: Displaying data distribution and outliers using a box plot.
# Question: Which category has the highest spread in the dataset?
# import numpy as np
# import matplotlib.pyplot as plt
# # Generate random data for 4 categories
# data = [np.random.randn(100) for _ in range(4)]

# # Create box plot
# plt.boxplot(data, patch_artist=True)
# plt.xlabel("Category")
# plt.ylabel("Values")
# plt.title("Box Plot")
# plt.show()




# VIOLIN PLOT
# Problem Statement: Comparing multiple distributions using a violin plot.
# Question: How does the density of data differ across categories?
# import matplotlib.pyplot as plt
# import numpy as np
# # Create violin plot
# data = [np.random.randn(100) for _ in range(4)]
# plt.violinplot(data)
# plt.xlabel("Category")
# plt.ylabel("Values")
# plt.title("Violin Plot")
# plt.show()


# 3D SCATTER PLOT
# Problem Statement: Visualizing relationships between three variables in a 3D space.
# Question: How are the three random variables distributed in the 3D space?

# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# import numpy as np
# # Generate 50 random values for x, y, and z
# x = np.random.rand(50)
# y = np.random.rand(50)
# z = np.random.rand(50)

# # Create 3D figure and axis
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Create 3D scatter plot
# ax.scatter(x, y, z, color='red')
# ax.set_xlabel("X-axis")
# ax.set_ylabel("Y-axis")
# ax.set_zlabel("Z-axis")
# ax.set_title("3D Scatter Plot")
# plt.show()




# HEATMAP
# Problem Statement: Understanding data distribution using a heatmap.
# Question: What areas in the matrix have the highest intensity values?

# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np
# data = np.random.rand(10,10)  # Generate a 10x10 matrix of random values

# # Create heatmap
# plt.imshow(data, cmap='coolwarm', interpolation='nearest')
# plt.colorbar()
# plt.title("Heatmap")
# plt.show()


# SEABORN PAIR PLOT
# Problem Statement: Analyzing relationships between multiple stock market variables.
# Question: How do different variables relate to each other in the dataset?
# import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# data_dict = {
#     "total_bill": np.random.uniform(5, 50, 100),
#     "tip": np.random.uniform(1, 10, 100),
#     "sex": np.random.choice(["Male", "Female"], 100),
#     "smoker": np.random.choice(["Yes", "No"], 100),
#     "day": np.random.choice(["Thur", "Fri", "Sat", "Sun"], 100),
#     "time": np.random.choice(["Lunch", "Dinner"], 100),
#     "size": np.random.randint(1, 6, 100)
# }

# # Convert dictionary to DataFrame
# data_df = pd.DataFrame(data_dict)

# # Create pair plot using seaborn
# sns.pairplot(data_df, hue="sex")
# plt.title("Pair Plot")
# plt.show()



