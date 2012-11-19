
def main ():
	nimi = raw_input("Anna nimesi: ")
	f = open ('nimet.txt','r+')
	print 'Listassa on seuraavat nimet:\n'
	f.read()

main()
