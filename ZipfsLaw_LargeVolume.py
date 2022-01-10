# This program prompts the user for a text file, and produces the total word count,
# the word counts of the 10 most frequent words inside the program and a graph.

# Importing string for list of punctuation
import string

# Importing os to consume all .txt files in the same directory
import os
location = os.getcwd() # get current directory location

# Importing matplotlib for plotting purposes
import matplotlib.pyplot as plt

# Import time for timing function
from time import perf_counter

# Helpful Global Variables
words = dict() # Dictionary with word counts
wordcounts = list() # List containing tuples representing word count pairs
wordcount = 0 # used for total word count
start_time = perf_counter() # Starting time

def consume_files():
    ''' Finding and opening the text files in the directory and analyzing them'''
    
    for file in os.listdir(location):
        if file.endswith(".txt"):
            file = open(file, encoding="utf-8")
            calculate_wordcounts(file)
    print_final_values()
    

def calculate_wordcounts(file):
    ''' Count the words in the text files '''
    global words, wordcount # get global variables
    # Iterating through lines to count words
    for line in file:
        line = line.rstrip() # get rid of whitespace
        line = line.translate(line.maketrans("","", string.punctuation)) # get rid of standard punctuation
        line = line.lower().split() # make line lowercase, split into a list of words
        for word in line:
            filtered_word = "".join(filter(str.isalpha, word)) # word containing only letters
            words[filtered_word] = words.get(filtered_word,0) + 1 # add/modify words dictionary
            wordcount +=1 # increase wordcount

def plot_zipf():
    ''' Plotting the graph visualizing Zipf's law with the collected data, also prints time elapsed '''
    global wordcounts # get global variables
    rank = 0 # Counter representing rank
    ranks = [] # list of ranks in increasing order
    frequencies = [] # list or frequencies in decreasing order
    expected_frequencies = [] # expected list of frequencies based on Zipf's law

    for val, key in wordcounts:
        rank += 1 # increase rank
        ranks.append(rank) # add rank to ranks
        frequencies.append(val) # add frequency to frequencies
        if rank == 1:
            first_freq = val # frequency of most common word
            expected_frequencies.append(first_freq) # add expected frequency to expected_frequencies
        else:
            expected_frequencies.append(first_freq/rank) # expected frequency of word based off of zipf's law

    # Plotting results
    plt.plot(ranks, frequencies, label = "Acual result") # Plot actual result
    plt.plot(ranks, expected_frequencies, label = "Expected result") # Plot expected result
    plt.xscale("log") # Scale x axis with log 10
    plt.yscale("log") # Scale y axis with log 10
    plt.xlabel("Ranking") # Label x axis
    plt.ylabel("Frequency") # Label y axis
    plt.title("The Frequency of Words versus their Relative Ranking") # Plot title
    plt.legend() # Show legend
    end_time = perf_counter()
    print("Time taken: " + str(end_time - start_time))
    plt.show() # Display plot

def print_final_values():
    ''' Returning the final results after analyzing data: word count, most common words, graph '''

    # Sort the dictionary by value
    for key, val in list(words.items()):
        wordcounts.append((val, key))
    wordcounts.sort(reverse=True) # sort in decreasing order of frequency

    print("\nTotal word count: "+ str(wordcount)) # Print total word count of consumed files
    print("\nTotal unique words: "+ str(len(wordcounts))) # Print total unique words
    # Print 10 most common words from consumed files
    print("\nThe 10 most common words are:")
    for key, val in wordcounts[:10]:
        print(val, key)
    
    plot_zipf() # plot values to visualize zipf's law

consume_files() # Running consume_files()

