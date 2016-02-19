from __future__ import print_function

methods = ['OnEditBase', 'OnEditJ2KTS', 'OnEditArp', 'OnEditInfo', 'OnEditSdHd3gAsi']
#methods = ['OnEditBase']
keywords = 'void'
mibID = 'mdUVtx1sJ2K4K'
IDword = 'Add'
wordID = 'dlg'
notLook = 'dlg->'
mList=[]


def FileOpen():
  filename = input("Please enter a file name: ")
  print(filename)

  with open(filename) as f:
    content = f.readlines()
    return content

	
lines = FileOpen()
	
def extractRanges(content,Add, fName):
	inner = 0
	index=0
	rng = []
	
	if Add is 0:
		for s in content:
			index = index+1		
			for method in methods:
				if method in s and keywords in s:
					inner=index
					count=0
					loop = 1
					while loop is 1:
						var = content[inner]
						if '{' in var: 
							count=count+1
							if count is 1:
								rng.append(inner)
						if '}' in var:
							count=count-1
						inner=inner+1
					
						if count is 0:
							rng.append(inner)
							loop = 0
	return rng

	if Add is 1 :
		for s in content:
			if keywords in s and fName in s:
				while loop is 1:
					var = content[inner]
					if '{' in var: 
						count=count+1
						if count is 1:
							rng.append(inner)
					if '}' in var:
						count=count-1
					inner=inner+1
					if count is 0:
						rng.append(inner)
						loop = 0
	return rng

rng = extractRanges(lines,0,0)
print(rng) 
	
	
def extractTableRanges(rng, content):
	inner = -1
	index=0
	ix=0
	jx=1
	size = int(len(rng)/2)
	mList = []

	for i in range(index,size):
		index = rng[ix]
		end = rng[jx]
		loop=1
		while loop is 1:
			var = content[index]
			mList.append(([rng[ix],rng[jx]]))
			if IDword in var and wordID in var and keywords not in var:
				i=0
				while i < len(var) and var[i] is not '>':
					while var[i] is not'(':
						print(var[0:i])
						addRng = extractRanges(content,1,var[0:i])
						mList.append(addRng)
						i = len(var)
					i = i +1
			index = index +1
			if index > end:
				loop =0;
			
		ix = ix +2
		jx = jx +2
		
	return mList



 
print(extractTableRanges(rng, lines))

