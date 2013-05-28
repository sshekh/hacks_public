	import fnmatch
	import os
	import sys
	import re

	src = sys.argv[1]
	string = sys.argv[2]
	pattern = sys.argv[3]
	#print  src

	count=0;
#print lines
	mylist1 = []
	my_list = {}
	count=count+1
	print "\n"
	print "Query #" + str(count) + ": "
	print "LIST 1#:"
	#print "query_string\tregular expression\tsubdirectoryname\tmatchedfilename"
#	print line
#	print word
#	print string
#	print pattern
	matches = []
	for root, dirnames, filenames in os.walk(src):
#	  print "yo"
	  for filename in fnmatch.filter(filenames,pattern):
        	found=0
		#print filename
		
      ##matches.append("\n")
	#matches.append(os.path.join(root, filename))
#		print filename
	#search for string as it is      
		string2 = string
		if string2 == filename:
			print string + '		' + pattern + '	' + root + '	' + filename
			found=1
			if root in my_list:
				my_list[root]=my_list[root]+1
			else: my_list[root]=1


		if found==1:
			continue
		string2 = string + ".*"
		#if(filename=="grid.o"):
		#	print filename + "  " + string2
		if fnmatch.fnmatch(filename,string2):
			print string + '		' + pattern + '	' + root + '	' + filename
			found=1
                        if root in my_list:
                                my_list[root]=my_list[root]+1
                        else: my_list[root]=1

#sesarch for string + 1 substitution, addition, deletion
		if found==1:
        	        continue
		string2 = string
		length = len(string)
		for i in range (0, length):
			string3 = string[:i] + '?' + string[i+1: ] + '.*'
		#print string3
			if fnmatch.fnmatch(filename, string3):
				print string + '		' + pattern + '	' + root + '	' + filename
				found=1
	                        if root in my_list:
        	                        my_list[root]=my_list[root]+1
                	        else: my_list[root]=1

			if found==1:
		                continue
			string3 = string[:i] + '?' + string[i+1: ]
			if fnmatch.fnmatch(filename, string3):
		                print string + '		' + pattern + '	' + root + '	' + filename
				found=1
	                        if root in my_list:
	                                my_list[root]=my_list[root]+1
        	                else: my_list[root]=1

			if found==1:
		                continue
	
			string3 = string[:i] + '?' + string[i:]
			if fnmatch.fnmatch(filename, string3):
				print string + '		' + pattern + '	' + root + '	' + filename
				found=1
	                        if root in my_list:
        	                        my_list[root]=my_list[root]+1
                	        else: my_list[root]=1

			if found==1:
		                continue
			string3 = string[:i] + '?' + string[i:] + ".*"
			if fnmatch.fnmatch(filename, string3):
        		        print string + '		' + pattern + '	' + root + '	' + filename
				found=1
	                        if root in my_list:
	                                my_list[root]=my_list[root]+1
        	                else: my_list[root]=1
			string3 = string[:i]  + string[i:] + ".*"
			if fnmatch.fnmatch(filename, string3):
        		        print string + '		' + pattern + '	' + root + '	' + filename
				found=1
	                        if root in my_list:
	                                my_list[root]=my_list[root]+1
        	                else: my_list[root]=1

			if found==1:
		                continue
			string3 = string[:i-1] + string[i:]
			if fnmatch.fnmatch(filename, string3):
				print string + '		' + pattern + '	' + root + '	' + filename
                	        found=1
	                        if root in my_list:
        	                        my_list[root]=my_list[root]+1
	                        else: my_list[root]=1

	                if found==1:
        	                continue
			string3 = string[:i-1] + string[i:] + '.*'
			if fnmatch.fnmatch(filename, string3):
				print string + '		' + pattern + '	' + root + '	' + filename
                	        found=1
	                        if root in my_list:
        	                        my_list[root]=my_list[root]+1
	                        else: my_list[root]=1

	                if found==1:
        	                continue

			string3 = string[:i] + '?' + string[i:] + ".*"
			if fnmatch.fnmatch(filename, string3):
        	        	print string + '		' + pattern + '	' + root + '	' + filename
                	        found=1
	                        if root in my_list:
        	                        my_list[root]=my_list[root]+1
                	        else: my_list[root]=1
	       
		        if found==1:
        	                continue

			string3 = string[:i] + '?' + string[i:]
			if fnmatch.fnmatch(filename, string3):
        	        	print string + '		' + pattern + '	' + root + '	' + filename
                	        found=1
	                        if root in my_list:
        	                        my_list[root]=my_list[root]+1
                	        else: my_list[root]=1
	       
		        if found==1:
        	                continue


		string3 = string + '?.*'
		if fnmatch.fnmatch(filename,string3):
				print string + '		' + pattern + '	' + root + '	' + filename
                        	found=1
	                        if root in my_list:
        	                        my_list[root]=my_list[root]+1
                	        else: my_list[root]=1

	        if found==1:
        	                continue

		string3 = string + '?'
		if fnmatch.fnmatch(filename, string3):
                	print string + '		' + pattern + '	' + root + '	' + filename
	                found=1
                        if root in my_list:
                                my_list[root]=my_list[root]+1
                        else: my_list[root]=1

        	if found==1:
                        continue



		string3 = string[:length-1] + '.*'
		if fnmatch.fnmatch(filename, string3):
				print string + '		' + pattern + '	' + root + '	' + filename
                        	found=1
	                        if root in my_list:
        	                        my_list[root]=my_list[root]+1
                	        else: my_list[root]=1

	        if found==1:
        	                continue

		string3 = string[:length-1]
		if fnmatch.fnmatch(filename, string3):
                	print string + '		' + pattern + '	' + root + '	' + filename
	                found=1
	                if root in my_list:
                                my_list[root]=my_list[root]+1
                        else: my_list[root]=1

        	if found==1:
                	        continue

#print matches
#print my_list
	print "LIST 2#"
	for x,y in my_list.iteritems():
		print x + "\t" + str(y)
