__author__ = 'MFlores1'
import re


def readDataFromFile(filename):
    """
    filename: .csv file with data in plain text and html format.

    Split data by customer id

    returns a dictionary with customer id as key and text/html data as value
    """
    customer_id_dict = {}
    # Open and read the file
    with open(filename, 'r') as f:
        text = f.read()
    # Read text/html data between customer ids.  Store in tuples
    tuples = re.findall(r'CustomerID:(\d+),(.*?)(?=CustomerID:)', text, re.DOTALL)
    # Copy data from tuples to dictionary


def main():
    filename = "C:/Users/mflores1/dataforpython/property_website_all.csv"
    readDataFromFile(filename)


if __name__ == '__main__':
    main()
