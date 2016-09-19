import time
def note():
    
    print('                                日志')
    print('输入内容，“<<”退出，-->“ENTER”键-->“Y”键保存，“N”键放弃-->任意键退出。')
    print()
    f=open('test.txt','a+')
    f.write('\n \n'+time.strftime('%Y-%m-%d %A ',time.localtime()))
    c=time.time()
    f.write('（'+str(c)+'）')

    running=True
    while running:
        a=input('root!notebook!:请输入事项：')
        if a=='<<':
            break
        b=input('是否储存？（y/n/其他字符结束）:')
        if b=='y' or b=='Y':
            f.write('\n'+time.strftime('%H:%M:%S',time.localtime())+'\n \t'+a)
            
            print('已储存至 test.txt。')
        elif b=='n' or b=='N':
            print('\n请重新输入！')
            print()
        
        else:
            running=False

    f.close()
    print('结束！')

if __name__=='__main__':
    note()
    
