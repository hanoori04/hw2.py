# 202310992 하누리 파이썬 과제

def exchange(payment) :
    
    ohback = payment // 500 
    back = (payment - 500 * ohback) // 100 
    ohship =( (payment - 500 * ohback) - (100 * back) ) // 50 
    ship =( (payment - 500 * ohback) - (100 * back) - (50 * ohship) ) // 10 

    print("500원 동전의 개수:",ohback, "100원 동전의 개수:",back,"50원 동전의 개수:",
     ohship,"10원 동전의 개수: " ,ship)
    
def get_integer() :

    integer = int(input("동전으로 교환하고자 하는 금액은? : "))
    return integer

result_integer = get_integer()

exchange(result_integer)






    