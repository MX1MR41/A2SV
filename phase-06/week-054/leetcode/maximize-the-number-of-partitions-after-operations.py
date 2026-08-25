class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        from functools import cache
      
        @cache
        def dfs(index: int, current_chars: int, can_change: int) -> int:
            """
            Dynamic programming function to find maximum partitions.
          
            Args:
                index: Current position in string
                current_chars: Bitmask representing characters in current partition
                can_change: Flag indicating if we can still change one character (1 = can change, 0 = already used)
          
            Returns:
                Maximum number of partitions from current position
            """
            # Base case: reached end of string
            if index >= n:
                return 1
          
            # Get bitmask for current character
            char_bit = 1 << (ord(s[index]) - ord('a'))
          
            # Add current character to the partition
            next_chars = current_chars | char_bit
          
            # Check if adding current character exceeds k distinct characters
            if next_chars.bit_count() > k:
                # Start new partition with current character
                result = dfs(index + 1, char_bit, can_change) + 1
            else:
                # Continue with current partition
                result = dfs(index + 1, next_chars, can_change)
          
            # If we can still change one character
            if can_change:
                # Try changing current character to each possible letter
                for letter_index in range(26):
                    # Create bitmask for the new character
                    next_chars = current_chars | (1 << letter_index)
                  
                    if next_chars.bit_count() > k:
                        # Start new partition with the changed character
                        result = max(result, dfs(index + 1, 1 << letter_index, 0) + 1)
                    else:
                        # Continue with current partition including changed character
                        result = max(result, dfs(index + 1, next_chars, 0))
          
            return result
      
        # Store string length
        n = len(s)
      
        # Start DFS from index 0, empty partition, with ability to change one character
        return dfs(0, 0, 1)
