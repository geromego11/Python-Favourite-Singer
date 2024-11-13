def count_favorite_singers():
    # Read the number of songs
    N = int(input())
    
    # Read the singers array
    singers = list(map(int, input().split()))
    
    # Dictionary to store the count of each singer's songs
    singer_counts = {}
    
    # Count occurrences of each singer
    for singer in singers:
        singer_counts[singer] = singer_counts.get(singer, 0) + 1
    
    # Find the maximum number of songs by any singer
    max_songs = max(singer_counts.values())
    
    # Count how many singers have the maximum number of songs
    favorite_singers = sum(1 for count in singer_counts.values() if count == max_songs)
    
    return favorite_singers

# Process input and print output
print(count_favorite_singers())
