#include "lists.h"
<<<<<<< HEAD

/**
* insert_node - inserts  node in a sorted singly linked list
* @head: head of the linked list.
* @number: data in the new node.
* Return: address of the new node.
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode;
	listint_t *first;

	first = *head;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->n = number;
	newNode->next = NULL;

	if (*head == NULL || first->n > newNode->n)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}
	while (first->next != NULL)
	{
		if ((first->next->n > newNode->n && first->n < newNode->n)
			|| newNode->n == first->n)
		{
			newNode->next = first->next;
			first->next = newNode;
			return (newNode);
		}
		first = first->next;
	}
	newNode->next = first->next;
	first->next = newNode;
	return (newNode);
=======
#include <stdlib.h>

/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head: singly list head
 * @number: number to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
		{
			if (current->next->n > number)
				break;

			current = current->next;
		}
		new->next = current->next;
		current->next = new;
	}

	return (new);
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
}
