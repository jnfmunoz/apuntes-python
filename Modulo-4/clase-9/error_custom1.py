try:
    raise Exception("rut", "20.045.286-0", "Invalidate Rut Format")
except Exception as error:
    print(type(error))
    print(error.args)
    print(error)
    
#Haciendo un destructuring de los args
    key, value, message = error.args

    print(f'key ->{key}')
    print(f'value ->{value}')
    print(f'message ->{message}')