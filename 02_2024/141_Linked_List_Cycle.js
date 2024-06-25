/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
const hasCycle = (head) => {
  let ptr;
  ptr = head;

  if (!head) return false;
  while (ptr) {
    if (!ptr.next) return false;
    else if (ptr.next == ptr) return true;
    const temp = ptr.next;
    ptr.next = ptr;
    ptr = temp;
  }
};

// Floyd’s Cycle-Finding Algorithm, "tortoise and the hare algorithm"
const hasCycleV2 = (head) => {
  let fast = head;
  while (fast && fast.next) {
    head = head.next;
    fast = fast.next.next;
    if (head === fast) return true;
  }
  return false;
};
