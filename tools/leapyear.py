def leap():
    
    running=True
    while running:
        y=input('root!leapyear!:请输入年份：')
        if y=='<<':
            break
        elif not y.isdigit():
            print("请输入数字年份，如‘1994’。")
        else:

            year=int(y)
            if year%4==0 and year%100!=0 or year%400==0:
                year=str(year)
                print(year+'是闰年。')
            else:
                year=str(year)
                print(year+'不是闰年。')

if __name__=='__main__':
    leap()
    
