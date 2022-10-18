#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
<<<<<<< HEAD
* struct listint_s - singly linked list.
* @n: integer.
* @next: points to the next node.
*
* Description: singly linked list node structure
* for Holberton project.
*/
=======
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */

>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
