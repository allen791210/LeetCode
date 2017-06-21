/*Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.*/

//e.g. [-1], []
int maxSubArray(int* nums, int numsSize) {
    int sum=0, max=nums[0];
    for (int i=0; i< numsSize; i++){
        sum += nums[i];
        if (max < sum) max = sum;
        if (sum<0) sum = 0;
    }
    return max;
}