#Create a list of container names and print only those starting with “n”

container = ["node-a","goit","nginx"]
'''
for i in  container:
  if i[0] == 'n':
    print(i) 

'''

n_containers = [i for i in container if i[0] == 'n']

print(n_containers)

