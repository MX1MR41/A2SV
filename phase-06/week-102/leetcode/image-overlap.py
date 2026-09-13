class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        A = []
        B = []
        n = len(img1)
        
        # Step 1: Extract coordinates of all 1s in both images
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    A.append((r, c))
                if img2[r][c] == 1:
                    B.append((r, c))
                    
        # Step 2: Use a hash map to count the occurrences of each translation vector
        overlap_counts = collections.defaultdict(int)
        max_overlap = 0
        
        for r1, c1 in A:
            for r2, c2 in B:
                # The translation needed to align (r1, c1) with (r2, c2)
                translation = (r2 - r1, c2 - c1)
                
                # Count this translation
                overlap_counts[translation] += 1
                
                # Update max overlaps
                max_overlap = max(max_overlap, overlap_counts[translation])
                
        return max_overlap
