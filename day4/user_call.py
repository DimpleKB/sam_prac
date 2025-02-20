def f1():
    print("from f1")
def f2():
    print("from f2")
def f3():
    print("from f3")
fun_name=input("enter function name to be called")
#method 1
exec(fun_name + '()')
#method 2
functions={'f1':f1,'f2':f2,'f3':f3}
if fun_name in functions:
    functions[fun_name]()