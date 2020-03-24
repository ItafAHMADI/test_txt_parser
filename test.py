import re
with open('test.txt') as infile, open('output.txt', 'w') as outfile:
    copy = False
    for line in infile:
        if line.strip() == "# begin >>>>>>>>>>>>":
            copy = True
            continue
        elif line.strip() == "# <<<<<<<<< End":
            copy = False
            continue
        elif copy:
            
            words = line.split()
            s = line
            for i,w in enumerate(words):
    
                if w == "bind":
                    if  words[i+1] in dict.values():
                        found = True
                        print ("VIP : " + words[i+1] + " "+ words[i+2] )
                        sentence = "VIP : " + words[i+1] + " "+ words[i+2]
                        outfile.write(sentence)
                        outfile.write("\n")
                    else :
                        found = False
                if w == "server" and found:
                        your_string = s[s.find("server")+len("server"):s.find("check")].strip()
                        outfile.write(your_string)
                        outfile.write("\n")
                        print (your_string)
