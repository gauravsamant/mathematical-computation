#this check the utf-32 characters and return them

def utf32_to_printable():
    '''Take and integer value and print its utf-32 equivalent'''

    counter = 0

    try:
        fs = open("utf_to_ascii.txt", "w", encoding='utf-16')

        for i in range(2**32):
            if counter == 20:
                fs.write('\n')
                counter = 0
            else:
                fs.write("""  """+chr(i)+"""  """)
                counter += 1

    except Exception as e:
        print("Error occured during execution." + str(e))
    finally:
        fs.close()

# try:
#     utf32_to_printable()
# except Exception as e:
#     print(e)
utf32_to_printable()
