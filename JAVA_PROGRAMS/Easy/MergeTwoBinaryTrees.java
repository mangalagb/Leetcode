package Easy;

//You are given two binary trees root1 and root2.
//
//Imagine that when you put one of them to cover the other,
// some nodes of the two trees are overlapped while the others
// are not. You need to merge the two trees into a new binary tree.
// The merge rule is that if two nodes overlap, then sum node values
// up as the new value of the merged node. Otherwise, the NOT null
// node will be used as the node of the new tree.
//
//Return the merged tree.
//
//Note: The merging process must start from the root nodes of both trees.

public class MergeTwoBinaryTrees {

     // Definition for a binary tree node.
      public class TreeNode {
          int val;
          TreeNode left;
          TreeNode right;
          TreeNode() {}
          TreeNode(int val) { this.val = val; }
          TreeNode(int val, TreeNode left, TreeNode right) {
              this.val = val;
              this.left = left;
              this.right = right;
          }
      }

    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null) {
            return null;
        }


        TreeNode newNode = new TreeNode(0);
        if (root1 != null && root2 != null) {
            newNode.val = root1.val + root2.val;

            //Recurse
            newNode.left = this.mergeTrees(root1.left, root2.left);
            newNode.right = this.mergeTrees(root1.right, root2.right);

        } else if (root1 != null) {
            newNode.val = root1.val;

            //Recurse
            newNode.left = this.mergeTrees(root1.left, null);
            newNode.right = this.mergeTrees(root1.right, null);

        }else {
            newNode.val = root2.val;

            //Recurse
            newNode.left = this.mergeTrees(null, root2.left);
            newNode.right = this.mergeTrees(null, root2.right);
        }
        return newNode;
    }

    public TreeNode makeTree1() {
        TreeNode root1 = new TreeNode(1);
        TreeNode node1 = new TreeNode(3);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(5);
        root1.left = node1;
        root1.right = node2;
        node1.left = node3;
        return root1;
    }

    public TreeNode makeTree2() {
        TreeNode root2 = new TreeNode(2);
        TreeNode node4 = new TreeNode(1);
        TreeNode node5 = new TreeNode(3);
        TreeNode node6 = new TreeNode(4);
        TreeNode node7 = new TreeNode(7);
        root2.left = node4;
        root2.right = node5;
        node4.right = node6;
        node5.right = node7;
        return root2;
    }


    public static void main(String[] args){
          MergeTwoBinaryTrees solution = new MergeTwoBinaryTrees();

          TreeNode root1 = solution.makeTree1();
          TreeNode root2 = solution.makeTree2();
          TreeNode result = solution.mergeTrees(root1, root2);
          System.out.println("result");
    }
}
