# Favorite Singers Counter

A Python solution to find the number of favorite singers in a playlist. A favorite singer is defined as one who has the maximum number of songs in the playlist.

## Problem Description

Bob has a playlist of N songs, where each song has a singer associated with it (denoted by an integer). A favorite singer is one whose songs appear the most times in the playlist. The task is to count how many favorite singers Bob has.

### Input Format
- First line: An integer N, denoting the number of songs in Bob's playlist
- Second line: N space-separated integers, where the i-th integer denotes the singer of the i-th song

### Output Format
- A single integer representing the number of favorite singers

### Constraints
- 1 ≤ N ≤ 2 * 10^5
- 1 ≤ a[i] ≤ 10^15 (where a[i] represents the singer ID of the i-th song)

## Example

### Sample Input
```
5
1 1 2 2 4
```

### Sample Output
```
2
```

### Explanation
In this example:
- Singer 1 appears 2 times
- Singer 2 appears 2 times
- Singer 4 appears 1 time
- Both singers 1 and 2 have the maximum number of songs (2 songs each)
- Therefore, there are 2 favorite singers

## Implementation Details

The solution uses a Python dictionary to count the occurrences of each singer and then counts how many singers have the maximum number of appearances. The implementation ensures efficient handling of the given constraints and uses 64-bit data types as required.

## Usage

1. Make sure you have Python installed on your system
2. Run the program:
   ```bash
   python favorite_singers.py
   ```
3. Enter the input as specified in the input format
4. The program will output the number of favorite singers

## Time and Space Complexity

- Time Complexity: O(N), where N is the number of songs
- Space Complexity: O(K), where K is the number of unique singers

## Technical Requirements
- Python 3.x
- No additional libraries required
- Requires handling of 64-bit integers (built into Python)

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
