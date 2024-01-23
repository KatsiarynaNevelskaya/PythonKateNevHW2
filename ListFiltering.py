# Используя цикл for
def filter_list_with_for(lst):
    result = []
    for item in lst:
        if isinstance(item, int):
            result.append(item)
    return result

# Используя list comprehensions
def filter_list_with_list_comprehension(lst):
    return [item for item in lst if isinstance(item, int)]

# Используя filter() + lambda
def filter_list_with_filter_lambda(lst):
    return list(filter(lambda item: isinstance(item, int), lst))

# Пример использования
l = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]

print('With for:', filter_list_with_for(l))
print('With list comprehensions:', filter_list_with_list_comprehension(l))
print('With lambda:', filter_list_with_filter_lambda(l))
