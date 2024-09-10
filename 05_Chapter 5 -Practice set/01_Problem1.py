# Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up! 

hindi_to_english = {
    'नमस्ते': 'Hello',
    'धन्यवाद': 'Thank you',
    'सपना': 'Dream',
    'प्यार': 'Love',
    'खुशी': 'Happiness',
    'खाना': 'Food',
    'पानी': 'Water',
    'सूरज': 'Sun',
    'चाँद': 'Moon',
    'मित्र': 'Friend',
    'घर': 'Home',
    'सड़क': 'Street',
    'सपना': 'Dream',
    'शिक्षा': 'Education',
    'स्वास्थ्य': 'Health'
}

word = input("enter the word to get the meaning : ")

print(hindi_to_english[word])