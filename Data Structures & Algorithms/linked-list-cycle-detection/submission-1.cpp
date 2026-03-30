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
    bool hasCycle(ListNode* head) {
        // edge case: only one element
        if (head && !head->next) {
            return false;
        }
        
        ListNode* slow = head;
        ListNode* fast = head;

        while (slow && fast) {
            // update pointers
            slow = slow->next;
            fast = fast->next;

            // update fast (check for null)
            fast = fast ? fast->next : nullptr;

            // cycle detected
            if (slow == fast) {
                return true;
            }
        }

        return false;
    }
};
