# numbers = [1, 2, 3]

# new_list = [n + 1 for n in numbers]

# print(new_list)




# name = "August"

# new_list = [letter for letter in name]

# print(new_list)



# rng_list = [num * 2 for num in range(1, 5) if 5 == 5]

# print(rng_list)



# names = ["August hej", "Emma hej", "Sixten", "Chrille"]


# short_names = [name for name in names if len(name) < 12]
# print(short_names)

# long_names = [name.capitalize() for name in names if len(name) < 18]
# print(long_names)


# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(num) for num in list_of_strings]
# result = [num for num in numbers if num % 2 == 0]
# print(result)



# with open("file1.txt") as file1:
#   list1 = file1.readlines()
    
# with open("file2.txt") as file2:
#   list2 = file2.readlines()
    
# result = [int(num) for num in list1 if num in list2]
 
# print(result)


# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Freddie"]



# student_score = {student:random.randint(1,100) for student in names}

# print(student_score)

# passed_students = {student:score for (student, score) in student_score.items() if score >= 60}

# print(passed_students)



# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}

# print(result)


# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

# print(weather_f)




# student_dict = {
#   "student": ["Angela", "James", "Lily"],
#   "score": [56, 76, 98]
# }



# for (key, value) in student_dict.items():
#   print(value)
  
  
# import pandas 

# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)


# # for (key, value) in student_data_frame.items():
# #   print(value)

# for(index, row) in student_data_frame.iterrows():
#   if row.student == "Angela":
#     print(row.score)


student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

data = pandas.read_csv("nato.csv")


phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dictionary)
word = input("Enter word: ").upper()


output_list = [phonetic_dictionary[letter] for letter in word]

print(output_list)


 # # for (key, value) in student_data_frame.items():
# #   print(value)

# for(index, row) in student_data_frame.iterrows():
#   if row.student == "Angela":
#     print(row.score)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}

# print(result)