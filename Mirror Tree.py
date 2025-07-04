class Solution:
    # Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        # Base case: agar root None hai toh kuch bhi karne ki zarurat nahi
        if root is None:
            return

        # Recursively left and right subtree ka mirror banao
        self.mirror(root.left)
        self.mirror(root.right)

        # Fir root ke left aur right children ko swap kar do
        root.left, root.right = root.right, root.left

        # Tree ka mirror ban gaya, koi return ki zarurat nahi (in-place changes)
