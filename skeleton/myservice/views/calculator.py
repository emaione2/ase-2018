from flakon import JsonBlueprint
from flask import Flask,request,jsonify

calc = JsonBlueprint('calculator', __name__)

@calc.route('/calc/sum', methods=['GET'])
def mysum():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    res = m
    if n<0:
        for i in range(0, -n):
            res -= 1
    else:
        for i in range(0,n):
            res+=1

    return jsonify({'Result':str(res)})

#a=21
#b=-3
#print("sum->",a,"+",b,"=",mysum(a,b))

@calc.route('/calc/div', methods=['GET'])
def divide():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    res=0
    sign=1
    if(m<0):
        m = abs(m)
        sign = sign * (-1)
    if (n < 0):
        n=abs(n)
        sign = sign * (-1)
    while(m>=0):
        m=m-n
        if(m>=0): # asd
            res+=1
    return jsonify({'Result':str(res*sign)})

#a=-21
#b=3
#print("divide->",a,":",b,"=",divide(a,b))

def subtract(m,n):
    res = m
    if n > 0:
        for i in range(0, n):
            res -= 1
    else:
        for i in range(0, -n):
            res += 1

    return res

def multiply(m,n):
    if(m==0 or n==0):
        return 0

    res = 0
    sign = 1
    if (m < 0):
        m = abs(m)
        sign = sign * (-1)
    if (n < 0):
        n = abs(n)
        sign = sign * (-1)
    for i in range(n):
        res+=m
    return res * sign

print("Fine")