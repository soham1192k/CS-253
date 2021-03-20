cd inputs;
rm -rf *.in;
cd ..;
rm -rf *.gcda;
rm -rf *.gcno;
rm -rf data.txt;
rm -rf new.txt;
rm -rf results.txt;
rm -rf ./test/S.txt;
rm -rf ./test/T.in;
cp ./test/p.cpp p.cpp;
echo "How many test cases?";
read n;
echo "Original Test Suite:">>./test/T.in;
for (( cnt=1; cnt<=$n; cnt++ ))
do
	g=$(($RANDOM % 2));
	h=$(($RANDOM % 2));
	a=$(($RANDOM % 2147));
	b=$(($RANDOM % 483));
	if [[ g -eq 0 ]]; then
		c=$(($RANDOM % 648));
		echo -n -$a>>inputs/test.in;
	else
		c=$(($RANDOM % 647));
		echo -n $a>>inputs/test.in;
	fi
	d=$(($RANDOM % 2147));
	e=$(($RANDOM % 483));
	echo -n $b>>inputs/test.in;
	echo $c>>inputs/test.in;
	if [[ h -eq 0 ]]; then
		f=$(($RANDOM % 648));
		echo -n -$d>>inputs/test.in;
	else
		f=$(($RANDOM % 647));
		echo -n $d>>inputs/test.in;
	fi
	echo -n $e>>inputs/test.in;
	echo $f>>inputs/test.in;
done
cp ./inputs/test.in ./test/T.in;
echo $n>data.txt;
echo $n>new.txt;
echo -n "Expected Time when run on my program:";
echo $n "seconds";
echo "Updating new.txt!Please be patient!";
for (( cnt=1; cnt<=$n; cnt++ ))
do
	g++ -fprofile-arcs -ftest-coverage p.cpp -o bin/p;
	cat ./inputs/test.in | head -n $((2*cnt)) | tail -n 2|bin/p>/dev/null;
	gcov -b p.cpp>/dev/null;
	if [[ cnt -eq 1 ]];then
		grep "branch" p.cpp.gcov>>temp.txt;
		lines=( $(wc -l temp.txt) );
		rm -rf temp.txt;
		echo $lines>>new.txt;
	fi
	for x in $(grep "branch" p.cpp.gcov| awk '{print $4}'); 
	do
		if [[ $x == "100%" ]]; then
			echo -n "1 " >> new.txt;
		else 
			echo -n "0 " >> new.txt;
		fi
	done 
	echo >>new.txt;
	rm -rf p.cpp.gcov;
	rm -rf p.gcda;
	rm -rf p.gcno;
done
g++ -fprofile-arcs -ftest-coverage p.cpp -o bin/p;
for (( cnt=1; cnt<=$n; cnt++ ))
do
	cat ./inputs/test.in | head -n $((2*cnt)) | tail -n 2|bin/p>/dev/null;
	s=( $(gcov -b p.cpp|grep "Lines"| awk '{print $2}') );
	t=( $(gcov -b p.cpp|grep "Branches"| awk '{print $2}') );
	echo -n ${s:9:5}>>data.txt;
	echo -n " ">>data.txt;
	echo ${t:9:5}>>data.txt;
done
echo "[Considering the entire test suite]:">>results.txt;
echo $(gcov -b p.cpp| awk "NR==3" )>>results.txt;

