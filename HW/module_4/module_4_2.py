def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

test_function()
# При вызове inner_function() ничего не выводится, потому что
# При попытке вызвать inner_function вне test_function, получим ошибку (NameError: name 'inner_function' is not defined.
# Did you mean: 'test_function'?), # так как inner_function определена только внутри test_function
# и не существует вне её области видимости.