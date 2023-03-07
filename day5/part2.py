import re

def parseStacks(text:str):
    stacks = []
    text = text.splitlines()
    size = int(text[-1].strip()[-1])
    for i in range(size):
        stack = []
        for line in text[:-1]:
            if line[4*i+1]!= ' ':
                stack.insert(0, line[4*i+1]) 
        stacks.append(stack)
    return stacks

def execute(stack, crates, to_stack, from_stack):
        tempStack = []
        for _ in range(crates):
            tempStack.insert(0, stack[from_stack].pop())
        stack[to_stack].extend(tempStack)

if __name__ == '__main__':
    input = open("input.txt", 'r').read()
    stacks_input, move_input = input.split("\n\n")
    stacks = parseStacks(stacks_input)
    move_input = move_input.split('\n')
    for instruction in move_input:
        print(instruction)
        x = re.search("move (\d+) from (\d+) to (\d+)", instruction)
        if(x != None):
            crates, to_stack, from_stack = x.groups()
            execute(stacks, int(crates), int(from_stack) - 1, int(to_stack) - 1)
    print(''.join(stack.pop() for stack in stacks))