/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function (nums1, m, nums2, n) {
  var bucket = nums1.slice();
  i = 0;
  j = 0;
  for (i, j; i < m && j < n; ) {
    if (bucket[i] <= nums2[j]) {
      nums1[i + j] = bucket[i];
      i++;
    } else {
      nums1[i + j] = nums2[j];
      j++;
    }
  }
  if (i == m) for (j; j < n; j++) nums1[i + j] = nums2[j];
  else for (i; i < m; i++) nums1[i + j] = bucket[i];
};

// We don't need buffer if we go BACKWARDS
var mergeV2 = function (nums1, m, nums2, n) {
  i = m - 1;
  j = n - 1;
  k = m + n - 1;

  while (j >= 0) {
    if (i >= 0 && nums1[i] > nums2[j]) nums1[k--] = nums1[i--];
    else nums1[k--] = nums2[j--];
  }
};
