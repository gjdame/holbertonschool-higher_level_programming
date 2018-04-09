#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast != NULL && slow != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
