def change(cost,given):
	coins={'quarters':0.25, 'dimes':0.1, 'nickel':0.05, 'penny':0.01}
	change=given-cost
	num_quarters=0
	num_dimes=0
	num_nickel=0
	num_penny=0
	if int(change)>=1.0:
		num_quarters+=int(change/coins['quarters'])
		change-=num_quarters*0.25
	if round(change,1) >=0.10:
		num_dimes+=int(change/coins['dimes'])
		change-=num_dimes*0.1
	if round(change,2) <0.1 and round(change,2)>=0.05:
		num_nickel+=int(change/coins['nickel'])
		change-=num_nickel*0.05
	if round(change,3) <0.05 and round(change,3)>=0.01:
		num_penny+=int(change/coins['penny'])
		change-=num_penny*0.01
	print ('quarters: '+ str(num_quarters))
	print ('dimes :'+str(num_dimes))
	print ('nickel :'+str(num_nickel))
	print ('penny :'+str(num_penny))


