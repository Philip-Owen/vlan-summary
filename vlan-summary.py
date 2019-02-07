import re
from operator import itemgetter

def build_vlan_list(vlan_file):
    vlan_file = open(vlan_file)
    file_lines = vlan_file.readlines()
    check_num = re.compile('[0-9]')
    vlan_sum = []

    for line in file_lines:
        rm_whitespace = ' '.join(line.split())
        split_columns = rm_whitespace.split(' ')
        if check_num.match(split_columns[0]):
            vlan_sum.append([int(split_columns[0]),split_columns[1]])
    return vlan_sum

def unique_vlans(vlan_file):
    vlan_sum = build_vlan_list(vlan_file)
    unique_list = []

    for x in vlan_sum:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def sort_vlans(vlan_list):
    return sorted(vlan_list, key=itemgetter(0))

def main():
    unique = unique_vlans('vlans.txt')
    final_sort = sort_vlans(unique)
    with open('vlans_sorted.txt', 'w') as file:
        for vlan in final_sort:
            line = str(vlan[0]) + ' ' + vlan[1] +'\n'
            file.write(line)

if __name__ == '__main__':
    main()