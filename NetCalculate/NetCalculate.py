from termcolor import colored, cprint

def _calculate_network_id_Broadcast_address(binary_ip,binary_mask_address,mask):
    
    #Network ID calculation
    binary_network_id = []
    decimal_network_id = []
    network_id = ""
    decimal_network = ""

    
    for ip_bit, mask_bit in zip(binary_ip, binary_mask_address):
        ip_bit = int(ip_bit, 2)
        mask_bit = int(mask_bit, 2)
        
        network_bit = ip_bit & mask_bit
        binary_network_id.append(format(network_bit, '08b'))
    
    for i in binary_network_id:
        network_id = network_id + i
        network_id = ("{}.".format(network_id))
         
    network_id = network_id.rstrip(network_id[-1])
    
    for i in binary_network_id:
        decimal_network_id.append(int(i, 2))
    
    for i in decimal_network_id:
        i = (str(i))
        decimal_network = decimal_network + i
        decimal_network = ("{}.".format(decimal_network))
    
    decimal_network = decimal_network.rstrip(decimal_network[-1])
    
    # Calcular Broadcast Address
    binary_direcction_ip = ""
    broadcast_address = ""
    current_group = ""
    
    binary_broadcast_address = []
    decimal_broadcast_address = []
    
    
    for i in binary_ip:
        binary_direcction_ip = binary_direcction_ip + i
        
    large_binary_ip = ((len(binary_direcction_ip)) - mask)
    broadcast_address = binary_direcction_ip[:-large_binary_ip]
    
    for i in range(large_binary_ip):
        broadcast_address = broadcast_address + "1"
        
    separated_binary_broadcast_address = '.'.join([broadcast_address[i:i+8] for i in range(0, len(broadcast_address), 8)])
    

    for i in range(len(broadcast_address)):
        current_group = current_group + broadcast_address[i]
        if (i + 1) % 8 == 0:
            binary_broadcast_address.append(current_group)
            current_group = ""
        
    for i in binary_broadcast_address:
        decimal_broadcast_address.append(int(i, 2))
    
    broadcast_address = ""
    for i in decimal_broadcast_address:
        i = str(i)
        broadcast_address = broadcast_address + i
        broadcast_address = ("{}.".format(broadcast_address))
    
    broadcast_address = broadcast_address.rstrip(broadcast_address[-1])
        
    cprint("[+] {} <--------------- {}/{} Network ID".format(network_id, decimal_network, mask), 'blue')
    cprint("[+] {} <--------------- {} Broadcast Address".format(separated_binary_broadcast_address, broadcast_address), 'yellow')
    cprint("---------------------------------------", 'blue')
    

#Binary ip address generation
def _binary_direcction_ip(ip_address,mask):
    
    binary_ip = []
    direcction_bin_ip = ""

    ip_parts = ip_address.split(".")
    ip_parts = [int(part) for part in ip_parts]
    
    for i in ip_parts:
        i = format(int(i),'08b')
        binary_ip.append(i)
    
    for i in binary_ip:
        direcction_bin_ip = direcction_bin_ip + i
        direcction_bin_ip = ("{}.".format(direcction_bin_ip))
         
    direcction_bin_ip = direcction_bin_ip.rstrip(direcction_bin_ip[-1])
    cprint("[+] {} <--------------- {}/{} Direcction Ip".format(direcction_bin_ip, ip_address, mask), 'green')
    _bin_mask_address(mask, binary_ip)

#Binary netmask generation
def _bin_mask_address(mask,binary_ip):
    
    binary_ip = binary_ip
    bin_mask_address = []
    decimal_mask_address = []
    
    mask_address = ""
    Network_mask = ""
    
    mask = (int(mask))
    
    for i in range(mask):
        mask_address = mask_address + "1"
        
        if len(mask_address) == 8:
            bin_mask_address.append(mask_address)
            mask_address = ""
    
    if mask_address:
        bin_mask_address.append(mask_address.ljust(8, '0'))
    
    mask_address = ""
    large_mask_bin = 32 - mask

    for i in range(large_mask_bin):
        mask_address = mask_address + "0"
        
        if len(mask_address) == 8:
            bin_mask_address.append(mask_address)
            mask_address = ""
    
    for i in bin_mask_address:
        decimal_mask_address.append(int(i,2))
           
    mask_address = ""
    for i in bin_mask_address:
        mask_address = mask_address + i
        mask_address = ("{}.".format(mask_address))
    
    mask_address = mask_address.rstrip(mask_address[-1])
    
    for i in decimal_mask_address:
        i = str(i)
        Network_mask = Network_mask + i
        Network_mask = ("{}.".format(Network_mask))
    
    Network_mask = Network_mask.rstrip(Network_mask[-1])           
    cprint("[+] {} <--------------- {} Network Mask".format(mask_address,Network_mask), 'red')
    cprint("---------------------------------------", 'blue')
    
    _calculate_network_id_Broadcast_address(binary_ip,bin_mask_address,mask)
    
def calculate_network(direcction_ip,mask_address):
    
    ip_address = direcction_ip
    mask_address = int(mask_address)
    cprint("\n")
    
    if mask_address >= 1 and mask_address <= 32:
        mask_address = str(mask_address)
        _binary_direcction_ip(ip_address,mask_address)
        mask_address = int(mask_address)
        
        #Defines the type of class you are working in
        if (mask_address <= 16):
            cprint("[+]it's class: A", 'red')
        elif (mask_address <= 24):
            cprint("[+]it's class: B", 'yellow')
        else:
            cprint("[+]it's class: C", 'green')
        
    else:
        cprint("[-]The netmask you entered is not correct, it must be between 1 and 32", 'red')
