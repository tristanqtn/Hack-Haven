# REMEBER TO CHANGE THE NAME OF THE DICTIONARY
echo "Number of words before cleanup"
wc -l dictionary.txt
sort dictionary.txt | uniq > unique.txt
echo "Number of words after cleanup"
wc -l dictionary.txt