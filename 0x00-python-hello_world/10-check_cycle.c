#include "lists.h"
/**
 * check_cycle - checks for a loop in a linked list
 * @list - pointer to a linked list
 *
 * Return: 1 if loop exists, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);

	while (fast != NULL && slow != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
