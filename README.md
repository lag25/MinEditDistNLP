# Minimum Editing Distance Calculator

This Python script calculates the minimum editing distance (MED) between two strings and describes the edit steps required to transform one string into another.

# Working and History of Minimum Editing Distance Algorithm

## Working of Minimum Editing Distance Algorithm

The Minimum Editing Distance (MED) algorithm, also known as Levenshtein distance, is a dynamic programming algorithm used to measure the similarity between two strings. It calculates the minimum number of operations required to transform one string into another, where the allowed operations are insertion, deletion, and substitution of characters.

The algorithm typically involves creating a matrix where each cell represents the minimum edit distance between substrings of the input strings. By iteratively filling in the matrix, the algorithm efficiently computes the minimum edit distance.

## History

The concept of Minimum Editing Distance was introduced by the Soviet mathematician Vladimir Levenshtein in 1965. It was initially developed to aid in the study of information theory and coding theory. Over time, it found applications in various fields, including natural language processing, bioinformatics, spell checking, and data deduplication.
For more information about the Minimum Edit Distance algorithm, you can refer to its [Wikipedia page](https://en.wikipedia.org/wiki/Levenshtein_distance#:~:text=Informally%2C%20the%20Levenshtein%20distance%20between,considered%20this%20distance%20in%201965.)

### Natural Language Processing:
- Spell checking: MED is used to suggest corrections for misspelled words by finding the closest matching words in a dictionary.
- Text correction: It helps in correcting grammar and punctuation errors in textual data.

### Bioinformatics:
- DNA sequencing: MED is used to compare DNA sequences and identify mutations, insertions, and deletions.
- Protein sequence alignment: It helps in aligning protein sequences to identify similarities and differences.

### Data Deduplication:
- MED is used to identify duplicate records in databases or datasets by measuring the similarity between records.

### Fuzzy String Matching:
- In information retrieval systems, MED is used for fuzzy string matching to find approximate matches for search queries.

### Version Control Systems:
- MED is used in version control systems like Git to calculate the difference between different versions of files.

The Minimum Editing Distance algorithm has wide-ranging applications in various domains, making it a fundamental tool in computational linguistics, bioinformatics, and data analysis.



## Description

The Minimum Editing Distance (MED) is a measure of the similarity between two strings in terms of the minimum number of operations required to transform one string into the other. The allowed operations are insertion, deletion, and substitution of characters.

This script provides a class `MinEditDist` with methods to calculate the MED between two strings and describe the edit steps needed to transform one string into another.

## Usage

1. **Minimum Editing Distance Calculation:**
    ```python
    med_instance = MinEditDist()
    s1 = "kitten"
    s2 = "sitting"
    med_result = med_instance.MED(s1, s2)
    print(f"Minimum Edit Distance: {med_result}")
    ```

2. **Description of Edit Steps:**
    ```python
    edit_steps = med_instance.describe_edit_steps(s1, s2)
    ```

    This method prints the edit steps required to transform string `s1` into string `s2`.

## Example

Consider the following example:
```python
s1 = "kitten"
s2 = "sitting"
med_result = med_instance.MED(s1, s2)
print(f"Minimum Edit Distance: {med_result}")
edit_steps = med_instance.describe_edit_steps(s1, s2)
```
This will output

```python
Minimum Edit Distance: 3
1. Substitute 'e' at position 5 with 'i'
2. Match 't' at position 4
3. Insert 'g' at position 3
```
