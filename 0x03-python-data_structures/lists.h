#ifndef LISTS_H
#define LISTS_H

<<<<<<< HEAD
#include <stdlib.h>
#include <stdio.h>

/**
* struct listint_s - singly linked list.
* @n: integer
* @next: pointer to next node.
*
* Description: singly linked node structure
* for Holberton project.
*/
typedef struct listint_s
{
	int n;
	struct listint_s *next;
=======
#include <stddef.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
<<<<<<< HEAD
=======

>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
int is_palindrome(listint_t **head);

#endif /* LISTS_H */
