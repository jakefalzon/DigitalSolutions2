def main():
    my_file = open('customers.txt', 'r')

    file_contents = my_file.read()

    my_file.close()

    print(file_contents)

    for line in file_contents:
        print(line)

main()