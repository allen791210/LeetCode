//O(N)
int findDuplicate(vector<int>& nums) {
    int slow = 0, fast = 0, t = 0;
    while (true) {
        slow = nums[slow];
        fast = nums[nums[fast]];
        if (slow == fast) break;
    }
    while (true) {
        slow = nums[slow];
        t = nums[t];
        if (slow == t) break;
    }
        return slow;
}

//O(nlogn)
int findDuplicate(int* nums, int numsSize) {
    int left = 1, right = numsSize-1, count = 0;
    int mid;
    while (left < right){
        mid = (left+right)/2;
        
        for (int i=0; i<numsSize; i++)
            if (nums[i] <= mid) count++;
        
        if (count <= mid) left = mid+1;
        else right = mid;
        
        count = 0;
    }
    return left;
}