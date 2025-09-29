with open('files/write.txt','w') as write_file:
    write_file.write('Hey there ninjas, python is awesomw')

#junk    

with open('files/write.txt','a') as write_file:
    write_file.write('\nI I love it so much. i dream in python')    


quotes = [
    '\nI can resist everythong except temptation',
    '\nWe are all in the gutter, but some of us are looking at the stars',
    '\nAlways forgive your enemies - nothing annoys them so much'
]    


with open('files/write.txt','a') as write_file:
    write_file.writelines(quotes)    
