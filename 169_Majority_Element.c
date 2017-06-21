//169. Majority Element

int majorityElement(int* nums, int numsSize) {
    int Maj_idx = 0, count = 1;
    for (int i=1; i<numsSize; i++){
        nums[i]==nums[Maj_idx] ? count++ : count --;
        if (count==0) 
            Maj_idx = i+1;
    }
    //still need to check e.g.[1,2,3] 3 is wrong
    count =0;
    for (int i=0;i<numsSize;i++){
        if (nums[i] == nums[Maj_idx])
            count++;
        if (count > numsSize/2)
            return nums[Maj_idx];
    }
    //return -1;
}