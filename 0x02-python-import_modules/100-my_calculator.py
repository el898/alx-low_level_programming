#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size, i;
    char *string;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(bytes))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(bytes);
    string = PyBytes_AsString(bytes);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);
    printf("  first %ld bytes:", size < 10 ? size + 1 : 10);
    for (i = 0; i < size && i < 10; i++)
        printf(" %02x", string[i] & 0xff);
    printf("\n");
}

void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    PyObject *item;
    Py_ssize_t size, i;
    const char *type;

    printf("[*] Python list info\n");

    if (!PyList_Check(list))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(list);

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)list)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(list, i);
        type = Py_TYPE(item)->tp_name;

        printf("Element %ld: %s\n", i, type);
        if (!strcmp(type, "bytes"))
            print_python_bytes(item);
    }
}

