## Pandas Interview Questions!
***
1. What is a Pandas DataFrame?
2. What is a Pandas Series?
3. How would you make an empty DataFrame in Python?
4. In Pandas, how would you find the number of unique values in a column?
5. What are some benefits of using Pandas?
6. How would you add a column to a pandas DataFrame?
7. How would you rename a column in a Pandas DataFrame?
8. How would you convert a Pandas DataFrame to a numpy array?
9. How would you save a Pandas DataFrame to a csv file?
10. Define GroupBy in Pandas.

***
  
1: A Pandas DataFrame (a.k.a 'df') is a two-dimensional data structure. It contains both rows and columns, and any arithmetic operations align on both row and column labels. 
It is considered the primary data structure in Pandas.
  
2: A Pandas Series is a one-dimensional ndarray with axis labels (including time series). Series support both integer- and label- based indexing and plenty of functions 
to perfom on the index itself. Series will automatically remove NaNs from data. A key thing to note is that operations between series, such as +, -, /, will perform the function
on it's associated index values. They do not have to be the same length - Series data will sort and unionize these two datasets.
  
3: An empty dataframe made in Python can be done so by the following code.
```python
df = pd.DataFrame()
```

4: To find unique values in a column, use df.info() for a general overview of data types. df.dtypes gives you the referenced type of data (float, int, object),
and df.yourcolumnname.unique() returns the unique values of a column into an object-style array.

5: Pandas benefits include loading, filtering and displaying data all inside of your runtime, as well as the ability to graphically visualize the data into
boxplots, heatmaps, bar graphs, and more, without any need for conversion or changing of format. Essentually it's an advanced Excel that can clean and tidy 
large amounts of data very quickly.

6: Define a list of information that needs to be added, and then give it a new name, and define it as such:
```python
df = pd.DataFrame(data) # defining our current DataFrame of 'data'
newColumn = ['Larry', 'Moe', 'Curly'] # creating the list of names
df['Names'] = newColumn # adding a 'Names' column with the list of newColumn
df # this would allow us to verify the result
```

7: Renaming a column in Pandas is simple with the df.rename or df.columns approach.
```python
# Method 1. Allows you to make a change to only a few column names. 'old_value' : 'new_value'
df = df.rename(columns={'OldName' : 'new_name',
                       'ReplaceMe' : 'replace_me'})
df.head()

# Method 2. You are forced to past a [list] of ALL the data columns, even if you only want to replace one of them.
df.columns = ['new_name', 'replace_me', 'hidden_names', 'forgotten_column']
```
8: Use the .to_numpy() function. Two different methods of approach.
```python
# Method 1.
df.to_numpy()

# Method 2.
df.values
```

9: This will write the object to a comma-separated value (csv) file in a location of our choosing.
```python
df.to_csv(r'C:\Users\yanni\Desktop\export_dataframe.csv', index = False, header=True)
```

10: Groupby allows you to compute statistics per group. *'Split, apply and combine'* is typically
what is thought of when we think about groupby in Python.
**Split** the data depending on the value of a key.
**Apply** a computing function on specified columns.
**Combine** the results of the operation into an output.
```python
# This grabs the max value of the Item_Outlet_Sales column.
df.groupby(['Outlet_Size', 'Outlet_Location_Type'])[['Item_Outlet_Sales']].max()
```