def div(num1, num2):
    try:
        res = num1 / num2

    except Exception as e:
        # return f'Error: {e}'
        print(f'Error: {e}')
    
    else:
        # return f'Division: {res}'
        print(f'Division: {res}')
    
    finally:
        return f"This code block will execute at any point."
    

x = 10
y = 0
print(div(x, y))