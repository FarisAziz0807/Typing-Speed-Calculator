from time import *
import random as r
def main():
    def mistake(par,test):
        error=0
        for i in range(len(par)):
            try:
                if par[i]!=test[i]:
                    error= error+1
            except :       
                    error= error+1
        return error
        
    def speed_time(time_s,time_e,userinput):
        time_delay=time_e-time_s
        time_R=round(time_delay,2)
        speed=len(userinput)/time_R
        return round (speed)
        
    if __name__ == '__main__':
        while True:
            ck = input(" read  test : yes / no :  ")
            if ck == "yes":
                test =["A paragrah is a self contained unit of  discourse in writing dealing with a particulr point or idea.","My name is Faris ","welcom to my Projects"]
                test1=r.choice(test)
                print("***** Typeining Speed Calculator *****")
                print(test1)
                print()
                print()
                time_1=time()
                testinput=input(" Enter : ")
                time_2=time()

                print("Speed : ",speed_time(time_1,time_2,testinput),"w/sec")
                print("Error :",mistake(test1,testinput))
            elif ck == "no":
                print("Thank you")
                break
            else:
                print("invalid input")    
main()