

if __name__ == '__main__':

    birthday = {
'peyton conner' : '2/13/2000' ,
'jenna kimble' : '7/26/1999' ,
'jensen conner' : '11/25/2011',
'barack obama' : '8/4/1961' , 
'lee taemin'  : '7/18/1993' 
}

print('Peyton Conners Birthday Directory')
for name in birthday:
    print(name)

print('Whos birthday would you like to search?')
name = input()
if name in birthday:
    print('{} was born on {}'.format(name, birthday[name]))
else:
    print('Birthday Unknown')
