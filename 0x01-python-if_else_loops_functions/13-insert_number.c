#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a new node at in a sorted list
 * @head: pointer to pointer to the head of the list
 * @number: the integer that will be included in the new node
 * Return: NULL if it fails or the address of the new element
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_value;
	listint_t *current_value;
	listint_t *previous_value;

	current_value = *head;
	previous_value = NULL;

	new_value = malloc(sizeof(listint_t));
	if (new_value == NULL)
		return (NULL);

	new_value->n = number;
	new_value->next = NULL;

	if (*head == NULL)
	{
		*head = new_value;
		return (new_value);
	}

	while (current_value != NULL && current_value->n < number)
	{
		previous_value = current_value;
		current_value = current_value->next;
	}

	if (previous_value == NULL)
	{
		new_value->next = *head;
		*head = new_value;
	}
	else
	{
		previous_value->next = new_value;
		new_value->next = current_value;
	}

	return (new_value);
}
