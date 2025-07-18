import csv

def grocery_calculator(groceries: dict):
    """A function to add up grocery bills.

    Arguments:
        - groceries: a dict which has the names of grocery bill items as its 
        keys, and the cost of the items as its values.

    Returns: a float representing the total cost of the grocery bill.

    Example input: {
        "Baby Spinach 100g bag": 2.78,
        "Hot Chocolate 300g": 3.70,
        "Crackers 250g packet": 2.10,
        "Coffee 500g": 9.00,
        "Carrots 1kg bag": 0.56,
        "Oranges 1kg bag": 3.08
    }

    Example output: 21.22
    """
     
    return sum(groceries.values())  # Return the total cost of the grocery bill
    

def word_counter(word_list: list):
    """A function to count the occurrences of each word in a word list.

    Arguments: 
        - word_list: a list of strings

    Returns: a dictionary containing the number of occurrences of each word in
    word_list.

    Example input: ["apple", "banana", "apple", "cherry", "apple", "banana"]

    Example output: {"apple": 3, "banana": 2, "cherry": 1}
    """

    word_count_dict = {}

    for word in word_list:
        count = word_count_dict.get(word, 0) # get existing word count (default to 0)
        word_count_dict.update({word: count + 1})
    
    return word_count_dict



def create_colour_dict(file_path: str):
    """A function that accesses an indicated csv file of colour values and 
    converts it into a dictionary.
    
    Arguments:
        - file_path: a string representing the location of a .csv file
        
    Returns: a dictionary whose keys are the plain English names of the colours
    described in the .csv file, and whose values are the hex codes of those 
    colours.
    
    Example input: "./data/colours_3_very_simple.csv"
    Example output: {"White": "#FFFFFF", "Black": "#000000", "Red": "#FF0000"}
    """
    colour_dict = {}

    with open(file_path, "r", newline='') as csv_file:
        csv_dictreader = csv.DictReader(csv_file)
        for row in csv_dictreader:
            if row and "English" in row and "HEX" in row:
                colour_name = row["English"].strip()
                hex_code = row["HEX"].strip()
                colour_dict[colour_name] = hex_code

    return colour_dict




