#!/bin/bash
g++ code.cpp -o code.out;
var="Soham 180771";
temp="Soham 180771";
temp+=" ";
temp+="Dummy 000000";
for (( i=1;i<=65536;i++ ));
do
    temp+=" ";
    temp+=$var;
done
./code.out $temp;
echo "********************************";
sleep 5;
echo "Now running code_without_vulnerabilities1.cpp";
g++ code_without_vulnerabilities1.cpp -o cwv1.out;
./cwv1.out $temp;
echo "********************************";
sleep 5;
echo "Now running code_without_vulnerabilities2.cpp";
g++ code_without_vulnerabilities2.cpp -o cwv2.out;
./cwv2.out $temp;
echo "********************************";
sleep 5;
echo "Now running code_without_vulnerabilities3.cpp";
g++ code_without_vulnerabilities3.cpp -o cwv3.out;
./cwv3.out $temp;
echo "********************************";