#!/usr/bin/python

import sys
import time
import numpy as np

marker = 1
node = {}
local_skyline = {}
candidate_skyline = []
global_skyline = []
shadow_skyline = {}
virtual_point = {}
why_not_points = {}
n_updated_flag = {}
skyline = []
data_length = 0
t = 5

# def Insert_Local_Skyline(current_specs, current_bit):
# 	print("Insert_Local_Skyline : " + str(current_specs))
# 	global local_skyline
# 	global shadow_skyline
# 	global virtual_point
# 	global node

# 	dominated_by_local = 0
# 	dominated_by_virtual = 0
# 	for i in range(0, len(local_skyline[current_bit])):	#pengulangan sebanyak data yang ada didalam local_skyline, untuk dibandingkan satu persatu dengan data baru
# 		bit_dominated_by_local = 0
# 		local_greater_flag = 0
# 		bit_dominating_local = 0
# 		local_smaller_flag = 0
# 		for j in range(0, len(current_specs)):
# 			if(local_skyline[current_bit][i][j] == 'null' or current_specs[j] == 'null'):
# 				bit_dominating_local += 1
# 				bit_dominated_by_local += 1
# 			else:
# 				if(local_skyline[current_bit][i][j] >= current_specs[j]):
# 					bit_dominated_by_local += 1
# 					if(local_skyline[current_bit][i][j] > current_specs[j]):
# 						local_greater_flag = 1
# 				if(current_specs[j] >= local_skyline[current_bit][i][j]):
# 					bit_dominating_local += 1
# 					if(current_specs[j] > local_skyline[current_bit][i][j]):
# 						local_smaller_flag = 1
# 		if(bit_dominated_by_local == len(current_specs) and local_greater_flag == 1):
# 			dominated_by_local = 1					#####################PRUNING MAY APPLY
# 			return False
# 		if(bit_dominating_local == len(current_specs) and local_smaller_flag == 1):
# 			local_skyline[current_bit][i][-1] = "delete"

# 	if(dominated_by_local == 0):
# 		#if p is dominated only by virtual_point
# 			#Insert P to shadow_skyline
# 			#N.updated_flag = True
# 			#Delete all dominated shadow_skyline
# 		#else
# 			#Delete all dominated local_skyline
# 			#Insert P to local_skyline
# 			#Delete all dominated shadow_skyline
# 		#insert P into local_skyline list of N
# 		for i in range(0, len(virtual_point[current_bit])):
# 			bit_dominated_by_virtual = 0
# 			virtual_greater_flag = 0
# 			for j in range(0, len(current_specs)):
# 				if((virtual_point[current_bit][i][j] == 'null') or (current_specs[j] == 'null')):
# 					bit_dominated_by_virtual += 1
# 				else:
# 					if(virtual_point[current_bit][i][j] >= current_specs[j]):
# 						bit_dominated_by_virtual += 1
# 						if(virtual_point[current_bit][i][j] >= current_specs[j]):
# 							virtual_greater_flag = 1
# 			if(bit_dominated_by_virtual == len(current_specs) and virtual_greater_flag == 1):
# 				dominated_by_virtual = 1

# 		if(dominated_by_virtual == 1):
# 			content = list(current_specs)
# 			content.append("ok")
# 			shadow_skyline[current_bit].append(content)
# 			n_updated_flag[current_bit] = True
# 			for i in range(0, len(shadow_skyline[current_bit])):
# 				bit_dominating_shadow = 0
# 				shadow_smaller_flag = 0
# 				for j in range(0, len(current_specs)):
# 					# print("current_specs[j]                  : " + str(current_specs[j]))
# 					# print("shadow_skyline[current_bit][i][j] : " + str(shadow_skyline[current_bit][i][j]))
# 					if(current_specs[j] >= shadow_skyline[current_bit][i][j]):
# 						bit_dominating_shadow += 1
# 						if(current_specs[j] > shadow_skyline[current_bit][i][j]):
# 							shadow_smaller_flag = 1
# 				if(bit_dominating_shadow == len(current_specs) and shadow_smaller_flag == 1):
# 					shadow_skyline[current_bit][i][-1] = 'delete'
# 			for i in sorted(shadow_skyline[current_bit], reverse=True):
# 				if (i[-1] == 'delete'):
# 					print("XXXXX shadow  deleted  : " + str(i) + " from " + str(current_bit))
# 					shadow_skyline[current_bit].remove(i)
# 			#Membatalkan deletion local_skyline
# 			for i in range(0, len(local_skyline[current_bit])):
# 				if(local_skyline[current_bit][i][-1] == 'delete'):
# 					local_skyline[current_bit][i][-1] = 'ok'
# 		elif(dominated_by_virtual == 0):
# 			for i in sorted(local_skyline[current_bit], reverse=True):
# 				if (i[-1] == 'delete'):
# 					local_skyline[current_bit].remove(i)
# 			content = list(current_specs)
# 			content.append("ok")
# 			local_skyline[current_bit].append(content)
# 			for i in range(0, len(shadow_skyline[current_bit])):
# 				bit_dominating_shadow = 0
# 				shadow_smaller_flag = 0
# 				for j in range(0, len(current_specs)):
# 					if(current_specs[j] >= shadow_skyline[current_bit][i][j]):
# 						bit_dominating_shadow += 1
# 						if(current_specs[j] > shadow_skyline[current_bit][i][j]):
# 							shadow_smaller_flag = 1
# 				if(bit_dominating_shadow == len(current_specs) and shadow_smaller_flag == 1):
# 					shadow_skyline[current_bit][i][-1] = 'delete'
# 			for i in sorted(shadow_skyline[current_bit], reverse=True):
# 				if (i[-1] == 'delete'):
# 					shadow_skyline[current_bit].remove(i)
# 			return True
# 	return False


# def Insert_Candidate_Skyline(current_specs, current_bit):
# 	global candidate_skyline
# 	global virtual_point
# 	dominated = 0
# 	for i in range(0, len(candidate_skyline)):
# 		candidate_greater_flag = 0
# 		candidate_smaller_flag = 0
# 		bit_dominating_candidate = 0
# 		bit_dominated_by_candidate = 0
# 		for j in range(0, len(current_specs)):
# 			if((current_specs[j] == 'null') or (candidate_skyline[i][j] == 'null')):
# 				bit_dominating_candidate += 1
# 				bit_dominated_by_candidate += 1
# 			else:
# 				if(current_specs[j] > candidate_skyline[i][j]):
# 					bit_dominating_candidate += 1
# 					candidate_smaller_flag = 1
# 				elif(current_specs[j] < candidate_skyline[i][j]):
# 					bit_dominated_by_candidate += 1
# 					candidate_greater_flag = 1
# 				elif(current_specs[j] == candidate_skyline[i][j]):
# 					bit_dominating_candidate += 1
# 					bit_dominated_by_candidate += 1
# 		if(bit_dominating_candidate == len(current_specs) and candidate_smaller_flag == 1):	#if P dominating candidate_skyline
# 			candidate_skyline[i][-1] = 'delete'
# 			print("XXXXA virtual try      : " + str(current_specs) + " to   " + str(candidate_skyline[i][-2]))
# 			Insert_Virtual_Point(current_specs, candidate_skyline[i][-2])
# 		elif(bit_dominated_by_candidate == len(current_specs) and candidate_greater_flag == 1):	#if P dominated by candidate_skyline
# 			q = list(candidate_skyline[i][:-2])
# 			print("XXXXB virtual try      : " + str(q) + " to   " + str(current_bit))
# 			Insert_Virtual_Point(q, current_bit)
# 			dominated = 1
# 	shadow_skyline[current_bit] = [i for i in shadow_skyline[current_bit] if i[-1] == 'ok']
# 	candidate_skyline = [i for i in candidate_skyline if i[-1] == 'ok']
# 	if(dominated == 0):
# 		content = list(current_specs)
# 		content.append(current_bit)
# 		content.append("ok")
# 		candidate_skyline.append(content)

# def Insert_Virtual_Point(current_specs, current_bit):
# 	global local_skyline
# 	global virtual_point
# 	global shadow_skyline
# 	#Move all dominated local_skyline N to shadow_skyline
# 	for i in range(0, len(local_skyline[current_bit])):
# 		bit_dominating_local = 0
# 		local_smaller_flag = 0
# 		for j in range(0, len(current_specs)):
# 			if((current_specs[j] == 'null') or (local_skyline[current_bit][i][j] == 'null')):
# 				bit_dominating_local += 1
# 			elif(current_specs[j] > local_skyline[current_bit][i][j]):
# 				bit_dominating_local += 1
# 				local_smaller_flag = 1
# 			elif(current_specs[j] == local_skyline[current_bit][i][j]):
# 				bit_dominating_local += 1
# 		if((bit_dominating_local == len(current_specs)) and (local_smaller_flag == 1)):
# 			local_skyline[current_bit][i][-1] = 'delete'
# 	for i in sorted(local_skyline[current_bit], reverse=True):
# 		if (i[-1] == 'delete'):
# 			i[-1] = 'ok'
# 			shadow_skyline[current_bit].append(i)
# 			local_skyline[current_bit].remove(i)
# 	#Remove all dominated virtual_point that has same bit
# 	for i in range(0, len(virtual_point[current_bit])):
# 		bit_dominating_virtual = 0
# 		virtual_smaller_flag = 0
# 		superset_check = 0
# 		for j in range(0, len(current_specs)):
# 			if((current_specs[j] == 'null') or (virtual_point[current_bit][i][j] == 'null')):
# 				bit_dominating_virtual += 1
# 			else:
# 				if(current_specs[j] > virtual_point[current_bit][i][j]):
# 					bit_dominating_virtual += 1
# 					virtual_smaller_flag = 1
# 				elif(current_specs[j] == virtual_point[current_bit][i][j]):
# 					bit_dominating_virtual += 1
# 			if((current_specs[j] == 'null') and (virtual_point[current_bit][i][j] != 'null')):
# 				superset_check += 1
# 			elif((current_specs[j] != 'null') and (virtual_point[current_bit][i][j] != 'null')):
# 				superset_check += 1
# 			elif((current_specs[j] == 'null') and (virtual_point[current_bit][i][j] == 'null')):
# 				superset_check += 1
# 		if((bit_dominating_virtual == len(current_specs)) and (virtual_smaller_flag == 1) and (superset_check == len(current_specs))):
# 			virtual_point[current_bit][i][-1] = 'delete'
# 	for i in reversed(virtual_point[current_bit]):
# 		if(i[-1] == 'delete'):
# 			virtual_point[current_bit].remove(i)
# 	content = list(current_specs)
# 	content.append('ok')
# 	virtual_point[current_bit].append(content)


# def Update_Global_Skyline():
# 	global global_skyline
# 	global candidate_skyline
# 	global shadow_skyline
# 	global data_length
# 	print("Update_Global_Skyline")
# 	print("Data yang akan diproses sepanjang : " + str(data_length))
# 	#data_length = len(candidate_skyline[])
# 	for c in range(0, len(candidate_skyline)):
# 		for g in range(0, len(global_skyline)):
# 			bit_dominating_global = 0
# 			bit_dominating_candidate = 0
# 			global_greater_flag = 0
# 			candidate_greater_flag = 0
# 			for i in range(0, data_length):
# 				if((candidate_skyline[c][i] == 'null') or (global_skyline[g][i] == 'null')):
# 					bit_dominating_global += 1
# 					bit_dominating_candidate += 1
# 				elif(candidate_skyline[c][i] == global_skyline[g][i]):
# 					bit_dominating_global += 1
# 					bit_dominating_candidate += 1
# 				elif(candidate_skyline[c][i] > global_skyline[g][i]):
# 					bit_dominating_global += 1
# 					candidate_greater_flag = 1
# 				elif(candidate_skyline[c][i] < global_skyline[g][i]):
# 					bit_dominating_candidate += 1
# 					global_greater_flag = 1
# 			if((bit_dominating_global == data_length) and (candidate_greater_flag == 1)):
# 				global_skyline[g][-1] = 'delete'
# 			elif((bit_dominating_candidate == data_length) and (global_greater_flag == 1)):
# 				candidate_skyline[c][-1] = 'delete'
# 	for i in reversed(global_skyline):
# 		if(i[-1] == 'delete'):
# 			global_skyline.remove(i)
# 	for i in reversed(candidate_skyline):
# 		if(i[-1] == 'delete'):
# 			candidate_skyline.remove(i)
# 	print("DEBUG, n_updated_flag : " + str(n_updated_flag))
# 	for i in n_updated_flag:
# 		print("DEBUG, i : " + str(i))
# 		if (n_updated_flag[i] == True):
# 			print("DEBUG, shadow : " + str(shadow_skyline))
# 			for s in range(0, len(shadow_skyline[i])):
# 				for g in range(0, len(global_skyline)):
# 					bit_dominating_global = 0
# 					shadow_greater_flag = 0
# 					for j in range(0, data_length):
# 						if((shadow_skyline[i][s][j] == 'null') or (global_skyline[g][j] == 'null')):
# 							bit_dominating_global += 1
# 						elif(shadow_skyline[i][s][j] == global_skyline[g][j]):
# 							bit_dominating_global += 1
# 						elif(shadow_skyline[i][s][j] > global_skyline[g][j]):
# 							bit_dominating_global += 1
# 							shadow_greater_flag = 1
# 					if((bit_dominating_global == data_length) and (shadow_greater_flag == 1)):
# 						global_skyline[g][-1] == 'delete'
# 				for c in range(0, len(candidate_skyline)):
# 					bit_dominating_candidate = 0
# 					shadow_greater_flag = 0
# 					for j in range(0, data_length):
# 						if((shadow_skyline[i][s][j] == 'null') or (candidate_skyline[c][j] == 'null')):
# 							bit_dominating_candidate += 1
# 						elif(shadow_skyline[i][s][j] == candidate_skyline[c][j]):
# 							bit_dominating_candidate += 1
# 						elif(shadow_skyline[i][s][j] > candidate_skyline[c][j]):
# 							bit_dominating_candidate += 1
# 							shadow_greater_flag = 1
# 					if((bit_dominating_candidate == data_length) and (shadow_greater_flag == 1)):
# 						candidate_skyline[c][-1] = 'delete'
# 	for i in reversed(global_skyline):
# 		if(i[-1] == 'delete'):
# 			global_skyline.remove(i)
# 	for i in reversed(candidate_skyline):
# 		if(i[-1] == 'delete'):
# 			candidate_skyline.remove(i)
# 	for i in candidate_skyline:
# 		global_skyline.append(i)
# 	for i in n_updated_flag:
# 		n_updated_flag[i] == False

def insert_to_skyline(current_specs):
	global skyline
	print("INSERTED : " + str(current_specs))
	content = list(current_specs)
	content.append("ok")
	skyline.append(content)

def bruteforce_skyline():
	global skyline
	global data_length
	for i in range(0, len(skyline)):
		for j in range(0, len(skyline)):
			bit_dominating = 0
			bit_dominated = 0
			greater_flag = 0
			smaller_flag = 0
			for x in range(0, data_length):
				if((skyline[i][x] == 'null') or (skyline[j][x] == 'null')):
					bit_dominating += 1
					bit_dominated += 1
				elif(skyline[i][x] == skyline[j][x]) :
					bit_dominating += 1
					bit_dominated += 1
				elif(skyline[i][x] > skyline[j][x]):
					bit_dominating += 1
					greater_flag = 1
				elif(skyline[i][x] < skyline[j][x]):
					bit_dominated += 1
					smaller_flag = 1
			if((bit_dominating == data_length) and (greater_flag == 1)):
				skyline[j][-1] = 'delete'
			elif((bit_dominated == data_length) and (smaller_flag == 1)):
				skyline[i][-1] = 'delete'
	for i in reversed(skyline):
		if(i[-1] == 'delete'):
			skyline.remove(i)


product_specs = np.loadtxt('product_specs.txt', skiprows=1, unpack=True)
user_preference = np.loadtxt('user_preference.txt', skiprows=1, unpack=True)
#t = 3

for x in range(0, len(user_preference[0])):	#pengulangan sebanyak user preference
	print("")
	print("NEW")
	fp = open("sorted_paper_data.txt")
	node.clear()
	local_skyline.clear()
	candidate_skyline.clear()
	global_skyline.clear()
	shadow_skyline.clear()
	virtual_point.clear()
	# print("Initial condition : ")
	# print("local     : " + str(local_skyline))
	# print("candidate : " + str(candidate_skyline))
	# print("global    : " + str(global_skyline))
	# print("shadow    : " + str(shadow_skyline))
	# print("virtual   : " + str(virtual_point))
	for line in fp:
		current_bit = ""
		current_specs = line.split()
		for i in range(0, len(current_specs)):
			if(current_specs[i] == "null"):
				current_bit += "0"
			else:
				current_bit += "1"
				current_specs[i] = abs(int(current_specs[i]) - user_preference[i][x])
		if current_bit not in node:
			node[current_bit] = []
			node[current_bit].append(current_specs)
			local_skyline[current_bit] = []
			shadow_skyline[current_bit] = []
			virtual_point[current_bit] = []
			n_updated_flag[current_bit] = False
		else:
			node[current_bit].append(current_specs)
		data_length = len(current_specs)
		insert_to_skyline(current_specs)
		#bruteforce_skyline(current_specs)

		#is_skyline = Insert_Local_Skyline(current_specs, current_bit)
		#is_skyline = False
		# if is_skyline == True:
		# 	pass
			# Insert_Candidate_Skyline(current_specs, current_bit)
			# if(len(candidate_skyline) > t):
			# 	Update_Global_Skyline()
			# 	candidate_skyline.clear()
		# print("**************************************************")
		# print("local     : " + str(local_skyline))
		# print("candidate : " + str(candidate_skyline))
		# print("shadow    : " + str(shadow_skyline))
		# print("virtual   : " + str(virtual_point))
		# print("**************************************************")
	fp.close()
	bruteforce_skyline()
	print("GLOBAL : " + str(skyline))
	#Update_Global_Skyline()
	# print("777777777777777777777777777777777")
	# print("local   : " + str(local_skyline))
	# print("shadow  : " + str(shadow_skyline))
	# print("virtual : " + str(virtual_point))
	# print("canddte : " + str(candidate_skyline))
	# print("n_flag  : " + str(n_updated_flag))
	# print("GLOBAL  : " + str(global_skyline))
	# for x in n_updated_flag:
	# 	if (n_updated_flag[x] == True):
	# 		print(x + ' is true')
	# 	else:
	# 		print(x + ' is false')
	# 	n_updated_flag[x] = False
	# print("000000000000000000000000000000000")
	# print("update ;")
	# print("")
	# print("")
	#print("NEW")