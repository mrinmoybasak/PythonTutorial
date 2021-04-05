class Dad:
    basketball =1


class Son(Dad):
    dance = 1
    basketball = 9
    def isdance(self):
        return f"Yes I have Dance {self.dance} no of Times"



class Grandson(Son):
    dance = 6
    # def  isdance(self):
    #     return f"Jaskson Yahah!" \
    #         f"Yes I have Dance Awsomely {self.dance} no of Times"

darry = Dad()
larry = Son()
harry= Grandson()
v= harry.basketball
print(v)

# print(harry.isdance())

