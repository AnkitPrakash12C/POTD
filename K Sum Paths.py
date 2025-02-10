class Solution:
    def solve(self, root, k, curr_sum, count, mp):
        if not root:
            return
        
        curr_sum += root.data
        if curr_sum == k:
            count[0] += 1
        
        if (curr_sum - k) in mp:
            count[0] += mp[curr_sum - k]
        
        mp[curr_sum] += 1
        
        self.solve(root.left, k, curr_sum, count, mp)
        self.solve(root.right, k, curr_sum, count, mp)
        
        mp[curr_sum] -= 1
    
    def sumK(self, root, k):
        mp = defaultdict(int)
        count = [0]
        self.solve(root, k, 0, count, mp)
        return count[0]