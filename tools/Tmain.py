import trans
import temperature
import notebook
import leapyear

print('需要帮助请输入：help')
loop=True
while loop:
    
    cmd=input('root!:')

    if cmd=='trans':
        trans.trans()
        
    elif cmd=='temp':
        temperature.temp()

    elif cmd=='note':
        notebook.note()

    elif cmd=='leap':
        leapyear.leap()

    elif cmd=='<<':
        loop=True

    elif cmd=='exit':
        loop=False
        
    elif cmd=='help':
        print('命令：-- \n trans :翻译；\n temp :温度转换； \n note :笔记；\n leap : 判断闰年；\n << :返回主命令； \n exit :退出')

    else :
        print('无此命令！')
