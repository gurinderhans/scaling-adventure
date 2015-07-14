import os,sys

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print 'no directory'
		sys.exit()


	for i in os.listdir(sys.argv[1]):
		directory = i.split(".")[0].split("_")[1]
		cmd = 'python recognise.py detected/{0} {1} {2} eigen_models/eigenModel_{0}.xml'.format(directory, sys.argv[2], sys.argv[3])
		os.system(cmd)
