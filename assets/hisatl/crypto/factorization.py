""""""
from random import randint 

class Factorization :
    """"""
    @classmethod 
    def factorize (cls ,pq ):
        """"""
        if pq %2 ==0 :
            return 2 ,pq //2 

        y ,c ,m =randint (1 ,pq -1 ),randint (1 ,pq -1 ),randint (1 ,pq -1 )
        g =r =q =1 
        x =ys =0 

        while g ==1 :
            x =y 
            for i in range (r ):
                y =(pow (y ,2 ,pq )+c )%pq 

            k =0 
            while k <r and g ==1 :
                ys =y 
                for i in range (min (m ,r -k )):
                    y =(pow (y ,2 ,pq )+c )%pq 
                    q =q *(abs (x -y ))%pq 

                g =cls .gcd (q ,pq )
                k +=m 

            r *=2 

        if g ==pq :
            while True :
                ys =(pow (ys ,2 ,pq )+c )%pq 
                g =cls .gcd (abs (x -ys ),pq )
                if g >1 :
                    break 

        p ,q =g ,pq //g 
        return (p ,q )if p <q else (q ,p )

    @staticmethod 
    def gcd (a ,b ):
        """"""
        while b :
            a ,b =b ,a %b 

        return a 
