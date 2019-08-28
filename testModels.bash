rm scoreHistory.py

#high, low, double
#high-low
#high-double
#low-double


for x in {1..100};
do
	echo ${x};
	python domino.py silent high low;
	python appendScore.py high low;
	python domino.py silent high double;
	python appendScore.py high double;
	python domino.py silent low double;
	python appendScore.py low double;
done;
