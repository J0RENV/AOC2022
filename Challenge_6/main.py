#line="nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
distChars = 14

with open('input.txt') as f: 
    line = f.readline()

    for i in range(0,len(line)-(distChars-1)):
        a=set(line[i:i+distChars])
        if len(a)==distChars:
            print(i+distChars)
            break

f.close()