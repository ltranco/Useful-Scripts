import os
import sys

def list_files(startpath):
	for root, dirs, files in os.walk(startpath):
		level = root.replace(startpath, '').count(os.sep)
		indent = ' ' * 4 * (level) + '/'
		dir = os.path.basename(root)
		if dir != 'WCS' and dir != 'CVS':
			print('%s%s' % (indent, os.path.basename(root)))
        	subindent = ' ' * 4 * (level + 1)
		#for f in files:
			#print f
	
def main():
	if len(sys.argv) == 2:
		list_files(str(sys.argv[1]))
	else:
		print 'Usage: python ls_tree.py path'

main()
