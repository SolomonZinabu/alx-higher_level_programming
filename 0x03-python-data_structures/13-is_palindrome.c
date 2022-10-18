#include "lists.h"

/**
<<<<<<< HEAD
* list_len - finds no. of elements ina linked list.
* @h: pointer to linked list.
*
* Return: number of elements in linked list.
*/
size_t list_len(listint_t *h)
{
	size_t  nodes = 0;

	if (h == NULL)
		return (0);
	while (h != NULL)
	{
		nodes++;
		h = h->next;
	}
	return (nodes);
}

/**
* is_palindrome - checks if a singly linked list is a palindrome.
* @head: double pointert to head of d-list.
*
* Return: 1 if palindrome, 0 otherwise.
*/
int is_palindrome(listint_t **head)
{
	int *nArr, i = 0, j = 0, len = 0;
	listint_t *temp;

	if (*head == NULL)
		return (1);
	temp = *head;
	len = list_len(temp);
	nArr = (int *)malloc(sizeof(int) * len);
	if (nArr == NULL)
		return (2);
	temp = *head;
	while (temp != NULL)
	{
		nArr[j] = temp->n;
		j++;
		temp = temp->next;
	}
	for (i = 0, j = len - 1; i < j; i++, j--)
	{
		if (nArr[i] != nArr[j])
			return (0);
	}
	return (1);
=======
 * is_palindrome - check if a linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
    const listint_t *current;
    const listint_t *tail;
    unsigned int n = 0;

    //Get length
    //Use a function to get a node on a specific index
    //check the first to the last and, second to second last ....
    //return false if one check was False
    //return true at the end (if all passed the checks)

    return (n);
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
}
