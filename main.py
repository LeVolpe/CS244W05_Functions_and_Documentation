import numpy as np

"""
This is worksheet 6 by Daniel Bursztynski

"""

Year = 0
DFTemp = 1
DFRain = 2
JATemp = 3
JARain = 4
JDTemp = 5
JDRain = 6

"""
read_data reads data from specified file
"""

def read_data(filename):
    a = np.loadtxt(filename, dtype=float, skiprows=1)
    return a

"""
find_offset returns the index of a specified year
"""
def find_offset(data, year):
    idx = 0

    for line in data:
        if line[0] == year:
            return idx
        else:
            idx = idx + 1

"""
get_years returns and array of data between specified years
"""
def get_years(data, sYear, eYear):
    start = find_offset(data, sYear)
    end = find_offset(data, eYear) + 1
    return(data[int(start):int(end), :])

"""
mean_temps returns the mean of a specified data such as the temperature in February
"""
def mean_temps(array, data01, data02):
    return np.mean(array[:, data01]), np.mean(array[:, data02])

"""
compare compares to data sets
"""
def compare(data01, data02):
    print(data01)
    print(data02)

    print('Diff:', data01[0] - data02[0])
    print('Diff:', data01[1] - data02[1])

"""
main is the main functions that run everything in a particular order
"""
def main():
    file = read_data('raintemp.csv')

    print(compare(mean_temps(get_years(file, 1845, 1900), DFTemp, JATemp),
                  mean_temps(get_years(file, 1970, 2011), DFTemp, JATemp)))


main()

