import random

my_dict={'R':"Rock",'P':"Paper",'S':"Scissors"}
user_count=0
comp_count=0


games=int(input("\nEnter the number of games you want to play: "))

while(comp_count+user_count<games):

	flag=0

	user_input=input("\nUser's Input: ")[0]
	user_input=user_input.upper()


	for i in my_dict.keys():
		if(user_input==i):		#If the entered input is confined to Rock, Paper or Scissors;
			flag=1
			break
	if(flag!=1):				#If not, run the loop again;
		print("INVALID INPUT")
		continue

	comp_input=random.choice(list(my_dict.keys()))	#Random Key from the dictionary my_dict i.e. R,P or S;

	print("Computer's Input: ", my_dict[comp_input])
	
	if ( user_input=='R' and comp_input=='P' ) or ( user_input=='P' and comp_input=='S' ) or ( user_input=='S' and comp_input=='R' ):
		comp_count=comp_count+1
		
	elif ( user_input=='P' and comp_input=='R' ) or ( user_input=='S' and comp_input=='P' ) or ( user_input=='R' and comp_input=='S' ):
		user_count=user_count+1
		
	else:
		print("TIE")

	print("\nSCORE:")
	print("User Score:",user_count,"\tComputer Score:",comp_count,"\n")

	#LOOP ENDS;

print("\n\t\tFINAL SCORE:")

print("User Score:",user_count,"\t\t\tComputer Score:",comp_count,"\n")
if user_count>comp_count:
	
	print("\n\tCONGRATULATIONS! YOU WON!")
	
elif user_count<comp_count:
	print("\n\t\tSORRY! YOU LOST!")
	
else:
	print("\n\t\tOOPS! IT'S A TIE!")
	