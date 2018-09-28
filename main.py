equation = input()

brackets = equation.count('{')

while True:
    breakC = 1
    if "}/{" in equation:                           # division to \frac
        breakC = 0
        pos = equation.find('}/{')
        levels = 1
        for i in range(pos-1, -1, -1):
            if equation[i] == "}":
                levels += 1
            if equation[i] == "{":
                levels -= 1
            if levels == 0:
                fracStart = i
                break
        levels = 1
        for i in range(pos+3, len(equation)):
            if equation[i] == "{":
                levels += 1
            if equation[i] == "}":
                levels -= 1
            if levels == 0:
                fracEnd = i
                break
        equation = equation[:fracStart]+"\\frac{"+equation[fracStart+1:pos]+"}{"+equation[pos+3:fracEnd]+"}"+equation[fracEnd+1:]

    if "{int}" in equation:                         # {int} to integral format
        breakC = 0
        pos = equation.find("{int}")+4
        if equation[pos+1] == "^" or equation[pos+1] == "_":
            if equation[pos+2] == "{":
                levels = 1
                for i in range(pos+3, len(equation)):
                    if equation[i] == "{":
                        levels += 1
                    if equation[i] == "}":
                        levels -= 1
                    if levels == 0:
                        powEnd = i
                        break
                levels = 1
                if equation[powEnd+1] == "_":
                    for i in range(powEnd+3, len(equation)):
                        print(equation[i])
                        if equation[i] == "{":
                            levels += 1
                        if equation[i] == "}":
                            levels -= 1
                        if levels == 0:
                            subEnd = i
                            break
                    equation = equation[:pos-4]+"\\int"+equation[pos+1:subEnd+1]+"\\! " +equation[subEnd+2:]
                else:
                    equation = equation[:pos-4]+"\\int"+equation[pos+1:powEnd+1]+"\\! "+equation[powEnd+2:]
            else:
                try:
                    if equation[pos+3] == "_":
                        equation = equation[:pos-4]+"\\int"+equation[pos+1:pos+5]+"\\! "+equation[pos+5:]
                    else:
                        equation = equation[:pos-4]+"\\int"+equation[pos+1:pos+3]+"\\! "+equation[pos+3:]
                except:
                    equation = equation[:pos-4]+"\\int"+equation[pos+1:pos+3]+"\\! "+equation[pos+3:]                    
        else:
            pos = pos - 4
            equation = equation[:pos]+"\\int \\! "+equation[pos+5:]
        
    if "dx" in equation:
        breakC = 0
        pos = equation.find("dx")
        equation = equation[:pos]+"\\,\\,\\mathrm{d}x "+equation[pos+2:]
    if "{spc}" in equation:
        breakC = 0
        pos = equation.find(" ")
        equation = equation[:pos]+" \\, "+equation[pos+5:]
    if breakC == 1:
        break


print("$$ "+equation+" $$")
    
