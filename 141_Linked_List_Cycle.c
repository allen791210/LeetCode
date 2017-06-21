/*
bool detect_cycle(Node* head){
  Node *fast = head;
  Node *slow = head;
  //Check head
  if (head==NULL || head->nextptr==NULL)
    return false;
  
  while(fast->nextptr!=NULL && fast->nextptr->nextptr!=NULL){
    fast = fast->nextptr->nextptr;
    slow = slow->nextptr;
    if (fast == slow) return true;
  }
  return false;
}
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    struct ListNode *fast = head;
    struct ListNode *slow = head;
    if (head == NULL) return false;
    while (fast->next != NULL && fast->next->next!=NULL){
        fast = fast->next->next;
        slow = slow->next;
        if (slow == fast) return true;
    }
    return false;
}