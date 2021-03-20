#!/bin/bash
for i in {0..4};
do
for ((j=$((i+1));j<=5;j++)); 
do
arr=(1 8 0 7 7 1);
for k in {a..z}; 
do
for l in {a..z};
do
arr[$i]=$k;
arr[$j]=$l;
pword="${arr[0]}${arr[1]}${arr[2]}${arr[3]}${arr[4]}${arr[5]}";
./zipfilegen.out 180771 $pword 1>>/dev/null;
var=( $(echo $?) );
if (($var==0)); then
    ans=$pword;break;
fi
done
done
done
done
echo $ans;