# Engineering Activity 2019-02-14 - Code Golf

## What does "Code Golf" stands for?

### What Wikipedia says?

> Code golf is a type of recreational computer programming competition in which participants strive to achieve the shortest possible source code that implements a certain algorithm. Playing code golf is known as "golf scripting".

> Whilst the term "code golf" was apparently first used in 1999 with Perl, and later popularised through the use of Perl to write a program that performed RSA encryption, similar informal competition was known to have been popular with earlier APL hackers. Today the term has grown to be applied to a wide variety of languages, which has even triggered the creation of dedicated golfing languages.

> The term "code golf" is derived from the similarity of its goal with that of conventional golf, where participants seek to achieve the lowest possible score, rather than the highest, as is the standard in most sports and game scoring systems. While conventional golf players are trying to minimize the number of club strokes needed to complete the course, code golfers are striving to reduce the number of key strokes necessary to write the program.

### Golden Rules
* The shorter the better
* No restrictions on the programming language that you can use, but scripting & syntactic sugar languages will give you a plus :wink:
* Don't worry about optimizations, readibility and maintenability
* The language knowledge & mastery is preferred over the algorithmic skills
* Functional programming FTW!
* Just for fun :wink:, but don't copy & print directly from the `.txt` files :stuck_out_tongue::laughing:

## Cool "Code Golf" references to check

* https://codegolf.stackexchange.com/
* https://code-golf.io/
* https://stackoverflow.com/questions/tagged/code-golf
* https://www.reddit.com/r/codegolf/
* https://www.quora.com/What-is-Code-Golf

## Having some fun with some challenges

### Tests validation

For each of your code solutions, you should compare the generated output against the respective challenge text file. 

You can use the following CLI command to perform the comparison: `diff output-file.txt <(php your-script-file.php);stat -f %z your-script-file.php`

No differences should be spotted by the command above.

### Growing Sequences Challenge

Take the following array of random numbers: `[5, 10, 3, 18, 60, 99, 1000, 5000, 55555, 777777]`.

For each number print the sequence from 1 to the number (inclusive), with one space between each one of these numbers.

Example. For `[3, 4, 2]`, the output should be:
```
1 2 3
1 2 3 4
1 2
```

### Output file
* `sequences.txt`
