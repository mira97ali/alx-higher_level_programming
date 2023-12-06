#include <Python.h>

/**
 * print_python_bytes - Print information about Python bytes object.
 * @p: PyObject representing the Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);

	printf("  size: %ld\n", size);

	char *string = PyBytes_AsString(p);

	if (!string)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  trying string: %s\n", string);

	printf("  first %d bytes:", (int)(size > 10 ? 10 : size));
	for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size); ++i)
	{
		printf(" %02x", string[i]);
	}
	printf("\n");
}

/**
 * print_python_list - Print information about Python list object.
 * @p: PyObject representing the Python list object.
 */
void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("[*] Invalid Python List\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);

	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *elem = PyList_GET_ITEM(p, i);

		printf("Element %ld: ", i);

		if (PyBytes_Check(elem))
			printf("bytes\n");
		else if (PyLong_Check(elem))
			printf("int\n");
		else if (PyFloat_Check(elem))
			printf("float\n");
		else if (PyTuple_Check(elem))
			printf("tuple\n");
		else if (PyList_Check(elem))
			printf("list\n");
		else if (PyUnicode_Check(elem))
			printf("str\n");
		else
			printf("Unknown\n");

		if (PyBytes_Check(elem))
			print_python_bytes(elem);
	}
}
