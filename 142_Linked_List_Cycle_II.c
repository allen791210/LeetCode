/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *detectCycle(struct ListNode *head) {
    struct ListNode *fast = head;
    struct ListNode *slow = head;
    if (head == NULL) return NULL;
    while (fast->next != NULL && fast->next->next!=NULL){
        fast = fast->next->next;
        slow = slow->next;
        if (slow == fast){
            slow = head;
            while(slow != fast){
                slow = slow -> next;
                fast = fast -> next;
            }
            return slow;
        }
    }
    return NULL;
}
