ip_addres = '192.168.3.1'
ip_spl = ip_addres.split('.')
bin_exp = ''
for num in ip_spl:
    bin_exp += bin(int(num))[2:] + '.' 
print(bin_exp[:-1])
print(type(bin_exp))
