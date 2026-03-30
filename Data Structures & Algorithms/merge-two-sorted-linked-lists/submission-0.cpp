/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:

    /**

    1 -> 2 -> 3
        l1 

    4 -> 5 -> 6 -> 7
    l2 

    -1 -> 1 -> 2
     d    t
                  
    */

    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* dummy = new ListNode(-999);
        ListNode* tail = dummy;

        // building result
        ListNode* l1 = list1;
        ListNode* l2 = list2;
        while (l1 && l2) {
            if (l1->val <= l2->val) {
                tail->next = l1;
                l1 = l1->next;
            } 
            else {
                tail->next = l2;
                l2 = l2->next;
            }   

            tail = tail->next;
        }

        // handle extra nodes
        if (l1) {
            tail->next = l1;
        } else if (l2) {
            tail->next = l2;
        }
        
        return dummy->next;
    }
};
