#include "lists.h"
/**
 *
 *
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *runner = *head;
	listint_t *new = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if ((*head)->n > number || (*head) == NULL)
	{
		new->next = *head;
		*head = new;
		return(new);
	}

	runner = runner->next;

	while(runner->next != NULL)
	{
		if (runner->next->n >= number)
		{
			new->next = runner->next;
			runner->next = new;
			return(new);
		}
		runner = runner->next;
	}

	new->next = NULL;
	runner->next = new;
	return(new);
}
