def main():
    my_file = open('customers.txt', 'w')

    my_file.write('Flynn Sperlich\n')
    my_file.write('Luke Lambert\n')
    my_file.write('Jeremy Leonard\n')
    my_file.write('Finn Sampson\n')
    my_file.write('Jake Falzon\n')

    my_file.close()

main()
