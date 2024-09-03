import basic 
while True:
    text = input('RAGHAVAN-BASIC>')
    result, error = basic.run('<stdin>',text)

    if error: print(error.as_string())
    else: print(result)
