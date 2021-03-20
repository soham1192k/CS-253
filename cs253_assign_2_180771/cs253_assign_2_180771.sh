wget https://api.covid19india.org/v4/data.json;#downloading the required json file
mv data.json covid_Data.json;#moving the downloaded json file to the correct file.
>processed_Covid_Data_180771.csv;#creating the csv file
>error.txt;#creating the file where all errors will be redirected
printf "State,District,Confirmed_Cases,Recovery_Rate\n">>processed_Covid_Data_180771.csv; #header row for the csv file
arr=( $(jq -r '.|keys' covid_Data.json) ); #creating an array of the state codes
count=${#arr[@]};#size of the array
IFS=$'\n';#the only separator should be a new line
for state in "${arr[@]:1:count-2}";#iterating over the state codes(from 1:count-2, since arr[0]="[" and arr[count-1]="]")
do
	opt=$state;
	temp="${opt%\,}";#removing any comma from the suffix
	temp="${temp%\"}";#removing any quotes from the suffix
	temp="${temp#\"}";#removing any quotes from the prefix
	max=0;#to store the maximum recovery rate
	max_where="";#to store the name of the district with the maximum recovery rate
	max_conf=0;#number of confirmed cases in that district
	for district in $(jq ".$temp.districts|keys|.[]" covid_Data.json 2>>error.txt);#itearing over the district names in that state
	do
		opt1=$district;
		temp1="${opt1%\,}";#removing any comma from the suffix
		temp2="${temp1%\"}";#removing any quotes from the suffix
		temp2="${temp2#\"}";#removing any quotes from the prefix
		confirmcases=$(jq ".$temp.districts.$temp1.total.confirmed|values" covid_Data.json);#storing the number of confirmed cases in this district
		if [[ confirmcases -ge 5000 ]] && [[ $temp2 != "Unknown" ]] #if confirmed cases is more than or equal to 5000 and the name of the district is not "Unknown"
		then
			recov=$(jq ".$temp.districts.$temp1.total.recovered|values" covid_Data.json);#number of recoveries
			rate=$(echo "scale=2;100*$recov/$confirmcases"|bc);#recovery rate(have to use bc, since bash by default doesnt support floating point numbers)
			if (( $(echo "$rate >= $max"|bc -l) )); #if the current recovery rate is more than the maximum recovery rate obtained so far
			then 
				max=$rate;#update the max recovery rate
				max_where=$temp1;#update the district name of the max recovery rate district
				max_conf=$confirmcases;#update the confirmed case number in this district
			fi
		fi
	done
	if [[ $max != 0 ]] #if max is still 0, it implies that there were no such district with confirmed cases>=5000 and whose name was not unknown
	then
		max_where="${max_where%\"}";#remove quotes from suffix
		max_where="${max_where#\"}";#remove quotes from prefix
		echo "$temp,$max_where,$max_conf,$max">>processed_Covid_Data_180771.csv;#send this line to the required csv file
	fi
done
