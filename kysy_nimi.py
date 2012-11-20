
def main ():
	try:
		f = open('nimet.txt', 'a')
	except f == EOF:
		f = open('nimet.txt', 'w')
	nimi =str(raw_input("Anna nimesi: "))
	f = open ('nimet.txt','a')
	f.write(nimi + '\n')
	f.close()
	f = open('nimet.txt', 'r')
	print 'Listassa on seuraavat nimet:\n'
	for names in f.readlines():
		print names
	f.close()
main()
