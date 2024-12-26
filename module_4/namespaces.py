def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

inner_function() # данный вызов функции порождает ошибку,
                 # область видимости для inner_function() только внутри функции test_function
