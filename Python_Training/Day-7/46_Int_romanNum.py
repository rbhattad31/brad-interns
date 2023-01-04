class solution:
    def integer_to_roman(self,num):
        x=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symb=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        i=0
        roman_num=""
        while(num>0):
            for _ in range(num//x[i]):
                roman_num+=symb[i]
                num=num-x[i]

            i=i+1
        return roman_num

print(solution().integer_to_roman(1))

