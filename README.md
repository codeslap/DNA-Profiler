This project takes in a database of people with their name and STR counts, and also a text file containing a sample of DNA to match against database of people.

One place where DNA tends to have high genetic diversity is in Short Tandem Repeats (STRs). 

An STR is a short sequence of DNA bases that tends to repeat consecutively numerous times at specific locations inside of a person’s DNA

![image](https://user-images.githubusercontent.com/56369460/186878837-7a7cfbb3-a88b-4867-be04-3666e51bb37a.png)

Using multiple STRs, rather than just one, can improve the accuracy of DNA profiling. 

If the probability that two people have the same number of repeats for a single STR is 5%, and the analyst looks at 10 different STRs, then the probability that two DNA samples match purely by chance is about 1 in 1 quadrillion (assuming all STRs are independent of each other).

To run program, in command-line, type:

python dna.py databases/y.csv sequences/x.txt

Where y is large or small, and x is a number 1-20

Example: 

![image](https://user-images.githubusercontent.com/56369460/186879506-865124e9-2b82-4a30-b71d-e14112b7b9e5.png)

Project is from Harvard's CS50x course, week 6.
