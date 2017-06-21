int removeDuplicates(int* nums, int numsSize) {
    int count = 1;
    if (numsSize<2) return numsSize; //Empty array
    
    for (int i=1; i<numsSize; i++)
        if (nums[i] != nums[i-1]) nums[count++] = nums[i]; 
    return count;
}