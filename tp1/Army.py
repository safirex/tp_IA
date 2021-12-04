class Army:
    def __init__(self,moralValue, moralBoost) -> None:
        self.moralValue = moralValue
        self.moralBoost = moralBoost

    def __repr__(self) -> str:
        val ='moral value of '+str(self.moralValue)+ " and boost of "+str(self.moralBoost)
        return val
    
    def get_Total_Moral(self) -> float:
        return self.moralValue*self.moralBoost

def get_sum_moral(arr) -> float:
    sum=0
    for i in arr:
        if(type(i)==Army):
            sum+=i.get_Total_Moral()