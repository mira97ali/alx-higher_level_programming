#include "lists.h"
#include <stdbool.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: true if palindrome, otherwise it's false
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev, *temp;

	if (*head == NULL || (*head)->next == NULL)
		return (true);

	slow = *head;
	fast = *head;
	prev = NULL;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}

	if (fast)
		slow = slow->next;

	while (prev && slow)
	{
		if (prev->n != slow->n)
			return (false);
		prev = prev->next;
		slow = slow->next;
	}

	return (true);
}
