student_id = input()
first = student_id[0]
second = student_id[1]
third = student_id[2]
fourth = student_id[3]
sixth = student_id[5]
if student_id.find("?") == -1 and student_id.count("?") == 0 :
	check_digit = (2*int(first) + 3*int(second)+ 5*int(third) + 7*int(fourth)) %11
	if check_digit == 10:
		check_digit = "X"
		if sixth == check_digit:
			print("VALID")
		else:
			print("INVALID")
	elif check_digit != 10:
		if str(check_digit) == sixth:
			print("VALID")
		else:
			print("INVALID")
elif student_id.count("?") == 1 and student_id[5] == "?" :
	check_digit = (2 * int(first) + 3 * int(second) + 5 * int(third) + 7 * int(fourth)) %11
	if check_digit == 10:
		check_digit = "X"
		sixth = check_digit
		student_id2 = "{}{}{}{}-{}".format(first,second,third,fourth,sixth)
		print(student_id2)
	else:
		sixth = check_digit
		student_id2 = "{}{}{}{}-{}".format(first, second, third, fourth, sixth)
		print(student_id2)
elif student_id.count("?") == 1 and student_id.find("?") < 5 :
	index = student_id.find("?")
	if index == 0:
		inverse = 6
		if sixth == "X":
			unknown = (((10-((3 * int(second) + 5 * int(third) + 7 * int(fourth)) % 11)) %11)* inverse) %11
			student_id2 = "{}{}{}{}-{}".format(unknown, second, third, fourth, sixth)
			print(student_id2)
		else:
			unknown = (((int(sixth)-((3 * int(second) + 5 * int(third) + 7 * int(fourth)) % 11)) %11)* inverse) %11
			student_id2 = "{}{}{}{}-{}".format(unknown, second, third, fourth, sixth)
			print(student_id2) 	
	elif index == 1:
		inverse = 4
		if sixth == "X":
			unknown = (((10- ((2* int(first) + 5 * int(third) + 7 * int(fourth)) % 11)) % 11) * inverse) %11
			student_id2 = "{}{}{}{}-{}".format(first, unknown, third, fourth, sixth)
			print(student_id2)
		else:
			unknown = (((int(sixth)- ((2* int(first) + 5 * int(third) + 7 * int(fourth)) % 11)) % 11) * inverse) %11
			student_id2 = "{}{}{}{}-{}".format(first, unknown, third, fourth, sixth)
			print(student_id2)
	elif index == 2:
		inverse = 9
		if sixth == "X":
			unknown = (((10- ((3 * int(second) + 2* int(first)  + 7 * int(fourth)) % 11)) % 11) * inverse) %11
			student_id2 = "{}{}{}{}-{}".format(first,second, unknown, fourth, sixth)
			print(student_id2)
		else:
			unknown = (((int(sixth) - ((3 * int(second) + 2* int(first)  + 7 * int(fourth)) % 11)) % 11) * inverse) %11
			student_id2 = "{}{}{}{}-{}".format(first,second, unknown, fourth, sixth)
			print(student_id2)
	elif index == 3:
		inverse = 8
		if sixth == "X":
			unknown = (((10- ((3 * int(second) + 5 * int(third) + 2* int(first) ) % 11)) % 11) * inverse) %11
			student_id2 = "{}{}{}{}-{}".format(first,second, third, unknown, sixth)
			print(student_id2)
		else:
			unknown = (((int(sixth) - ((3 * int(second) + 5 * int(third) + 2* int(first) ) % 11)) % 11) * inverse) %11
			student_id2 = "{}{}{}{}-{}".format(first,second, third, unknown, sixth)
			print(student_id2)
