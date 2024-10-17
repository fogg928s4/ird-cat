for i in range(20, 60,10):
    print(f'int gi0/0.{i}', end ='\n')
    print('ip access-group 123 in', end='\n')
    print('ex', end='\n')
    
for i in range(20, 60,10):
    print(f'access-list 1 permit 192.168.{i}.0 0.0.0.255', end ='\n')
   