#!/usr/bin/env python3
# Jeff Bohn
# 9/5/2024
# Week_3_Lab_2 
# Chapter 6 - Lists & Tuples
# main.py

import validation

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")


def get_scores():
    scores = []

    while True:
        score = validation.validate(input("Enter test score: "))
        if score != "x" :
            scores.append(score)
        else:
            return scores


def process_scores(scores):

    count = int(len(scores))
    total = sum(scores)
    average = total / count
    scores.sort()
      
    if (count % 2) == 0:
        # even - take the average of the 2 middle numbers
        a = int(count / 2)
        b = int((count / 2) - 1)
        median_score = (scores[a] + scores[b]) / 2
    else:
        # odd - same number of scores below it as above it
        a = int((count / 2))
        median_score = scores[a] 
               
    # format and display the result
    print()
    print("Score total:       ", total)
    print("Number of Scores:  ", count)
    print("Average Score:     ", round(average, 2))
    print("Low Score:         ", min(scores))
    print("High Score:        ", max(scores))
    print("Median Score:      ", median_score)


def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("\nBye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
