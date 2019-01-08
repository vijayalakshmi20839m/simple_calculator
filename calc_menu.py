#######################################################################################################################################################################3########################################################CALCULATOR##############################################################################################################################################################################################################################################################################

import calc_operation
import os
import sys


def main():
	choice=input("enter the choice: 1)simple calculator 2)scientific calculator 3)exit")

	while(1):
	
		if(choice==1):

			ch=input("simple calculator enter: 1)add 2)sub 3)mul 4)div 5)go back")

			if(ch==1):

					x=input("enter the first value")
					y=input("enter the second value")
					sum=calc_operation.myaddition(x,y)
					print sum

			if(ch==2):

					x=input("enter the first value")
					y=input("enter the second value")
					sub=calc_operation.mysubtraction(x,y)
					print sub

			if(ch==3):

					x=input("enter the first value")
					y=input("enter the second value")
					multiply=calc_operation.mymultiplication(x,y)
					print multiply

			if(ch==4):
				
					x=input("enter the first value")
					y=input("enter the second value")
					division=calc_operation.mydivision(x,y)
					print division

			if(ch==5):
					
					os.system('clear')
					main()

		if(choice==2):
			
			
			ch=input("scientific calculator enter: 1)sine 2)cosine 3)squareroot 4)powerof 5)go back")

			if(ch==1):

					x=input("enter the first value")
					y=calc_operation.mysine(x)
					print y

			if(ch==2):

					x=input("enter the first value")
					y=calc_operation.mycosine(x)
					print y


			if(ch==3):

					x=input("enter the first value")
					y=calc_operation.myroot(x)
					print y

			if(ch==4):

					x=input("enter the base value")
					y=input("enter the exponent value")
					z=calc_operation.mypowerof(x,y)
					print z

			if(ch==5):
					os.system('clear')
					main()

		if(choice==3):
		
			sys.exit()
			
main()
				





				



				


				


				


				





				



				


				


				


				





				



				


				


				


				





				



				


				


				


				





				



				


				


				


				





				



				


				


				


				





				



				


				


				


				





				



				


				


				


