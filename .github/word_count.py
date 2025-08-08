def analyze_text(text):
    """
    Analyze text to count characters (with/without spaces) and words
    """
    lines = text.strip().split('\n')
    
    total_chars_with_spaces = 0
    total_chars_without_spaces = 0
    total_words = 0
    
    print("Line-by-line analysis:")
    print("-" * 50)
    
    for i, line in enumerate(lines, 1):
        chars_with_spaces = len(line)
        chars_without_spaces = len(line.replace(' ', ''))
        words = len(line.split())
        
        total_chars_with_spaces += chars_with_spaces
        total_chars_without_spaces += chars_without_spaces
        total_words += words
        
        print(f"Line {i}: '{line}'")
        print(f"  Characters with spaces: {chars_with_spaces}")
        print(f"  Characters without spaces: {chars_without_spaces}")
        print(f"  Words: {words}")
        print()
    
    print("=" * 50)
    print("TOTALS:")
    print(f"Characters with spaces: {total_chars_with_spaces}")
    print(f"Characters without spaces: {total_chars_without_spaces}")
    print(f"Total words: {total_words}")
    
    return {
        'chars_with_spaces': total_chars_with_spaces,
        'chars_without_spaces': total_chars_without_spaces,
        'words': total_words
    }

# Example usage with the duck haiku
haiku = """Ripples spread outward
Orange webbed feet paddle beneath
Quiet pond at dawn"""

print("Analyzing the duck haiku:")
print("=" * 50)
results = analyze_text(haiku)

# You can also use it with any other text
print("\n" + "="*50)
print("Analyzing a different text:")
print("=" * 50)
sample_text = """The quick brown fox
jumps over the lazy dog"""
analyze_text(sample_text)