#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *moon, *cake;

	if (list == NULL || list->next == NULL)
		return (0);

	moon = list->next;
	cake = list->next->next;

	while (moon && cake && cake->next)
	{
		if (moon == cake)
			return (1);
		moon = moon->next;
		cake = cake->next->next;
	}

	return (0);
}
