import random
lower_case="ertyuiplkjhfdsazxc"
upper_case="ASDFRETYOPLMNBVCXZ"
num="1234567890"
symbol="{}!'^+%&/()="
alfabe=lower_case+upper_case+num+symbol
length=9
password="".join(random.sample(alfabe,length))
print(password)