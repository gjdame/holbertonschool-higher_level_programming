#include "lists.h"
/**
 *
 *
 *
 *
 */
int is_palindrome(listint_t **head)
{
	const listint_t *current;
	int len;
	int i, j;
	int *arr;

	if (*head == NULL)
		return(1);
	current = *head;
	len = 0;
	while (current != NULL)
	{
		current = current->next;
		len++;
	}

	if (len == 1)
		return(1);

	arr = malloc(sizeof(int) * len);
	if (arr == NULL)
		return(1);

	current = *head;
	i = 0;
	while(current != NULL)
	{
		arr[i] = current->n;
		i++;
		current = current->next;
	}

	j = 0;
	while(i >= (len / 2))
	{
		if (arr[i] != arr[j])
			return(1);
		i--;
		j++;
	}
	return (0);
}
