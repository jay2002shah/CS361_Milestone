import time

if __name__ == '__main__':

        while True:
                user_input = input('Enter 1 to get information from the request.json: ');

                if user_input == '1':
                        f = open('books.txt', 'w')
                        f.write('request')
                        f.close()

                        time.sleep(2)

                        w = open('getjson.txt', 'w')
                        w.write('recieved')
                        w.close()

                exit()
