/** Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
	 
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct TreeNode* mergeTrees(struct TreeNode* t1, struct TreeNode* t2) {
    if (!t1) return t2;
    if (!t2) return t1;
    
    struct TreeNode* Newnode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    Newnode -> val = t1->val + t2->val;
    Newnode -> left = mergeTrees(t1->left, t2->left);
    Newnode -> right = mergeTrees(t1->right, t2->right);
    return Newnode;
}


