#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: A PyObject list
 *
 * Description: This function prints the size, allocated memory,
 * and type of each element in a Python list.
 */
void print_python_list_info(PyObject *p)
{
	/* Check if the provided object is a list */
	if (!PyList_Check(p))
	{
		fprintf(stderr, "The provided object is not a list.\n");
		return;
	}

	/* Retrieve the size and allocated memory of the list */
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	/* Print the basic info about the list */
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	/* Iterate through the list and print the type of each element */
	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
