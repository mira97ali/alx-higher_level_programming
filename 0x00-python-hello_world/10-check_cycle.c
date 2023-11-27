#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head
 * Return: 0 if there is no cycle, 1 if there is one
 */

int check_cycle(listint_t *list)
{
	listint_t *previous, *current;

	if (list == NULL || list->next == NULL)
		return (0);

	previous = list;
	current = list->next;

	while (current != NULL && current->next != NULL)
	{
		if (previous == current)
			return (1);

		previous = previous->next;
		current = current->next->next;
	}

	return (0);
}
