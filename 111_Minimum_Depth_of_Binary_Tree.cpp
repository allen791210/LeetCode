/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 //Recursive Solution
class Solution {
public:
    int minDepth(TreeNode* root) {
        if(root == NULL) return 0;
        else if(root->right==NULL && root->left==NULL) return 1;
        else if(root->right==NULL) return minDepth(root->left)+1;
        else if(root->left==NULL) return minDepth(root->right)+1;
        return min(minDepth(root->right), minDepth(root->left))+1;
    }
};

//BFS
class Solution {
public:
    int minDepth(TreeNode* root) {
        if (root==NULL) return 0;
        
        queue<TreeNode> q;
        q.push(root);
        int left_level_cnt = 1, right_level_cnt = 1;
        TreeNode* temp;
        
        while (!q.empty()){
            qi = q.front();
            q.pop();
                
            if (qi->left==NULL && qi->right==NULL) return max(left_level_cnt, right_level_cnt);
            
            if (qi->left != NULL){
                temp = qi->left;
                q.push(temp);
                left_level_cnt +=1;    
            }
            
            if (qi->right != NULL){
                temp = qi->right;
                q.push(temp);
                right_level_cnt +=1;
            }
        }
        return 0;
    }
    
};