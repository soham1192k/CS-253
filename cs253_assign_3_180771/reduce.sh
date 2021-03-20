rm -rf ./test/S.txt;
cp ./test/p.cpp p.cpp;
echo "Enter the reduced number of tests:"
read k;
n=$(head -1 new.txt);
b=$(awk "NR==2" new.txt);
newlines=( $(wc -l new.txt) );
for (( c=$n+3; c<=$newlines; c++ ))
do 
    sed -i '$d' new.txt;
done
echo $k>>new.txt;
g++ logic.cpp -o bin/logic;
./bin/logic 1>choice.txt;
arr=()
while IFS= read -r line; do
  arr+=("$line")
done < choice.txt;
rm -rf *.gcov;
rm -rf *.gcno;
rm -rf *.gcda;
l=( $(wc -l results.txt) );
for (( c=1; c<=$l-2; c++ ))
do 
    sed -i '$d' results.txt;
done
g++ -fprofile-arcs -ftest-coverage p.cpp -o bin/p;
for i in "${arr[@]}"
do
    cat ./inputs/test.in | head -n $((2*i)) | tail -n 2|bin/p>/dev/null;
done
echo "********************">>results.txt;
echo "[Considering the reduced test suite]:">>results.txt;
echo $(gcov -b p.cpp| awk "NR==3" )>>results.txt;
echo "********************">>results.txt;
echo "Test Cases Selected:">>results.txt;
echo "Reduced Test Suite:">>./test/S.txt;
for i in "${arr[@]}"
do
    echo -n $i>>results.txt;
    echo -n "-->">>results.txt;
    echo -n "a = ">>results.txt;
    echo -n $(cat ./inputs/test.in|head -n $((2*i-1))|tail -n 1)>>results.txt;
    echo -n ",">>results.txt;
    echo -n " b = ">>results.txt;
    echo $(cat ./inputs/test.in|head -n $((2*i))|tail -n 1)>>results.txt;
    echo -n $i>>./test/S.txt;
    echo -n "-->">>./test/S.txt;
    echo -n "a = ">>./test/S.txt;
    echo -n $(cat ./inputs/test.in|head -n $((2*i-1))|tail -n 1)>>./test/S.txt;
    echo -n ",">>./test/S.txt;
    echo -n " b = ">>./test/S.txt;
    echo $(cat ./inputs/test.in|head -n $((2*i))|tail -n 1)>>./test/S.txt;
done
echo "[For a comparison,please see results.txt]">>./test/S.txt;
echo "Results redirected to results.txt!";
rm -rf choice.txt;
rm -rf *.gcov;
rm -rf *.gcno;
rm -rf *.gcda;
rm -rf p.cpp;