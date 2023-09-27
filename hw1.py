from ArrayStack import ArrayStack

#파일 읽기
f = open("test.txt",'r') 
lines = f.readlines() # 파일의 내용이 line의 배열에 담김
lines = [line.rstrip('\n') for line in lines] #공백문자 제거

def evalPostfix(expr) :
     s = ArrayStack(100)
     for token in expr :
     #    print(token)
        if token in "+-*/%":
               val2 = s.pop()
               val1 = s.pop()
               if (token == '+'): s.push(val1 + val2)
               elif (token == '-'):s.push(val1 - val2)
               elif (token == '*'):s.push(val1 * val2)
               elif (token == '/'):s.push(int(val1 / val2))
               elif (token == '%'):s.push(val1 % val2)
        elif token == '++' or token == '--':
             val3 = s.pop()
             if(token == '++'): 
                  val3 += 1
                  s.push(val3)          
             elif(token == '--'):
                  val3 -= 1
                  s.push(val3)
        elif token =='p':
             print(s.peek())
        elif token =='c':
             s.top = -1
        elif token =='l':
          #    print('top의 위치:',s.top)
          #    print('s.array[:s.top+1]의 출력값은 --> ',s.array[:s.top+1])
             for a in reversed(s.array[:s.top+1]):
                  print(a)

        elif token =='q':
             break
        else:
          #    print('top 1 증가')
             s.push(int(token))
          #    print('top의 위치:',s.top)

     return s.pop()


print(evalPostfix(lines))