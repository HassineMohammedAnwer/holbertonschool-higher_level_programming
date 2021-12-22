#include "lists.h"

/**
 * check_cycle - checks for a cycle
 * @list: list
 *
 * Return: 1 on succes 0 on failure
 */
int check_cycle(listint_t *list)
{
	listint_t *snd = list;
	listint_t *frst = list;

	if (!list)
		return (0);

	while (snd && frst && frst->next)
	{
		snd = snd->next;
		frst = frst->next->next;
		if (snd == frst)
			return (1);
	}

	return (0);
}
