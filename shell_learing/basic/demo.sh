#!/bin/sh


cd ~
mkdir shell_tut
cd shell_tut

for ((i=0;i<10;i++));do
    touch test_$i.txt
done

#ls -ls .

#rm -rf ../shell_tut
#定义变量
#注意，变量名和等号之间不能有空格，这可能和你熟悉的所有编程语言都不一样
name="weiyudang"

#for  file in `ls ../shell_tut`
#加花括号是为了帮助解释器识别变量的边界

echo $name
echo ${name}
for skill  in Ada Coffe Action Java;do
    echo "I'am good at ${skill} Script"
done


name="alibaba"
echo name

#2.字符串
# - 单引号里的任何字符都会原样输出，单引号字符串的变量是无效的
# - 单引号字串中不能出现单引号，对单引号的转义也不行
#双引号里可以有变量/可以存在转义字符

greeting="hello ,$name"
greeting="hello ,${name}"
echo $greeting

## 2.1字符串操作
#1. 拼接

greeting_len="greeting lenght:${#greeting}"
echo ${greeting_len}  # len
echo ${greeting:1:5}   #slice
#echo `expr index "$greeting" is`

## 3 printf
printf "%d %s\n" 1 "abc"
printf  "%s\t%s\n" "abc" "dd"

## 4. 流程控制


## 5。 函数 [function]

func_name() {
    echo "func_inn\n"
    echo "$1"
    echo "$2"
    echo "${10}"
    echo "参数的个数 $#"
    echo "作为一个字符串输出所有参数 $*\n"
}

func_name 1 2 3 45  6 6 7 7 7 8 20

## 6 。数组
myarray=(1 3  55 6)
echo ${myarray[2]}

#命令行输入top回车，然后按下大写M按照memory排序，按下大写P按照CPU排序。
