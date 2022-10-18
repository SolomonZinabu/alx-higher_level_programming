#include <stdio.h>
<<<<<<< HEAD
#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle within.
* @list: singly linked list.
* Return: 0 is there is no cycle, 1 if there is a cycle.
*/

int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *tail;

	if (list == NULL)
		return (0);

	head = list;
	tail = list;

	while (tail != NULL && tail->next != NULL)
	{
		head = head->next;
		tail = tail->next->next;

		if (head == tail)
			return (1);

=======
#include <string.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: The singly linked list
 *
 * Return: 1 if there is a cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast != NULL && slow != NULL)
	{
		slow = slow->next;
		if (fast->next == NULL)
			return (0);
		fast = fast->next;
		fast = fast->next;

		if (fast == slow)
			return (1);
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
	}
	return (0);
}
