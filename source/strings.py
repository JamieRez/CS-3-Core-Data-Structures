#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Of Course there is an empty string in a string
    if pattern == '':
        return True
    # Search Every Char in String
    for index in range(0, len(text)):
        # If we find the first letter of the pattern
        if text[index] == pattern[0]:
            # See if we can get the rest of it
            for patternIndex in range(0, len(pattern)):
                # If the pattern is longer than our remaining string letters
                # Or the we end up finding a fault
                if index + patternIndex > len(text) - 1 or not text[index + patternIndex] == pattern[patternIndex]:
                    # fugetabowtit
                    break
                # otherwise if we made it to the end and it still works
                elif index + patternIndex == index + len(pattern) - 1 and text[index + patternIndex] == pattern[patternIndex]:
                    # Found!!
                    return True
    # All letters have been went through
    return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Of Course there is an empty string in a string
    if pattern == '':
        return 0
    # Search Every Char in String
    for index in range(0, len(text)):
        # If we find the first letter of the pattern
        if text[index] == pattern[0]:
            # See if we can get the rest of it
            for patternIndex in range(0, len(pattern)):
                # If the pattern is longer than our remaining string letters
                # Or the we end up finding a fault
                if index + patternIndex > len(text) - 1 or not text[index + patternIndex] == pattern[patternIndex]:
                    # fugetabowtit
                    break
                # otherwise if we made it to the end and it still works
                elif index + patternIndex == index + len(pattern) - 1 and text[index + patternIndex] == pattern[patternIndex]:
                    # Return that starting index
                    return index
    # All Letters have been searched, not found
    return None

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Store our indices
    indexList = []
    # Of Course there is an empty string in a string
    if pattern == '':
        # Return every index in the string
        return [index for index, char in enumerate(text)]

    # Search Every Char in String
    for textIndex in range(0, len(text)):
        # If we find the first letter of the pattern
        if text[textIndex] == pattern[0]:
            # See if we can get the rest of it
            for patternIndex in range(0, len(pattern)):
                # If the pattern is longer than our remaining string letters
                # Or if we end up finding a fault
                if ((textIndex + patternIndex > len(text) - 1) or
                   (not text[textIndex + patternIndex] == pattern[patternIndex])):
                    # fugetabowtit
                    break
                # otherwise if we made it to the end and it still works
                elif ((textIndex + patternIndex == textIndex + len(pattern) - 1) and
                        (text[textIndex + patternIndex] == pattern[patternIndex])):
                        # Add that starting index to our list!
                        indexList.append(textIndex)

    return indexList

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
