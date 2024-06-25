/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
const maxDepth = (root) => {
  let dep = 0;
  let maxdep = 0;
  let ptr = root;
  let crossArr = [];

  while (ptr) {
    dep++;
    if (ptr.right && ptr.left) {
      crossArr.push({
        ptr,
        dep,
      });
      ptr = ptr.right;
    } else if (ptr.right) ptr = ptr.right;
    else if (ptr.left) ptr = ptr.left;
    else if (crossArr.length) {
      if (dep > maxdep) maxdep = dep;
      const cross = crossArr.pop();
      ptr = cross.ptr.left;
      dep = cross.dep;
    } else {
      if (dep > maxdep) return dep;
      return maxdep;
    }
  }
  return maxdep;
};

// Stop hating recursion.. ^^
const maxDepthV2 = (root) => {
  if (!root) return 0;
  let left = maxDepthV2(root.left);
  let right = maxDepthV2(root.right);
  return Math.max(left, right) + 1;
};
