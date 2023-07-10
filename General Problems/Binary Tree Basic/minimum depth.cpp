/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int minDepth(TreeNode* root) {
        queue<pair<TreeNode*,int>> q;
        if(root==nullptr) return 0;
        q.push(make_pair(root,1));
        while (!q.empty()){
            pair<TreeNode*,int> temp=q.front();
            q.pop();
            TreeNode* node=temp.first;
            int level=temp.second;
            if(node->left==nullptr and node->right==nullptr) return level;
            if(node->left) q.push(make_pair(node->left,level+1));
            if(node->right) q.push(make_pair(node->right,level+1));
        }
        return 0;
        
    }
};
