from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    
    final = ''
    for x in range(n):
        final += str(x+1)
    print(final)