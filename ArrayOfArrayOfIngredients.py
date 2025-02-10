import csv

# Function to read ingredient lists from a CSV file
def read_ingredient_lists(file_path, separator="hawk tuah"):
    master_list = []
    current_list = []
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            ingredient = row[0].strip()
            if ingredient == separator:
                if current_list:
                    master_list.append(current_list)
                    current_list = []
            else:
                current_list.append(ingredient)
        # Append the last list if there are remaining ingredients
        if current_list:
            master_list.append(current_list)
    return master_list


#csv_file_path = "RecipeUrlsTextFRs.csv"  # Replace with your CSV file path
#ingredient_master_list = read_ingredient_lists(csv_file_path)
#print("Master Ingredient List:")
#for ingredients in ingredient_master_list:
 #   print(ingredients)
