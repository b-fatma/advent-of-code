hierarchy = {}
curr_dir = []
sizes = {}

f = open("input.txt", 'r')
input = f.readlines()
for line in input:
    cmd = line.split()
    if cmd[0] == '$':
        if cmd[1] == 'cd':
            if cmd[2] == '..':
                curr_dir.pop()
            else:
                curr_dir.append(cmd[2])
                hierarchy["/".join(curr_dir)] = []
                sizes["/".join(curr_dir)] = 0
        else: #ls
            continue
    elif cmd[0] == 'dir':
        hierarchy["/".join(curr_dir)].append("/".join(curr_dir)+"/"+cmd[1])
    else: #size file
        sizes["/".join(curr_dir)] += int(cmd[0])


def total_size(dir):
    if len(hierarchy[dir]) == 0:
        return sizes[dir]
    return sizes[dir] + sum(total_size(sub_dir) for sub_dir in hierarchy[dir])


def part1():
    x = 0
    max_size = 100000
    for dir in hierarchy:
        if total_size(dir) <= max_size:
            x = x + total_size(dir)
    return x

def part2():
    disc_space = 70000000
    used_space = sum(list(sizes.values()))
    update_size = 30000000
    del_dir = disc_space
    space_needed = update_size - (disc_space - used_space)
    for dir in hierarchy:
        if total_size(dir) >= space_needed and total_size(dir) < del_dir:
            del_dir = total_size(dir)
    return del_dir



print("sum" , part1())
print("size", part2())

f.close()

