#SCRIPT

>DATOS_R.txt
for i in {1..10000}

do
python CarlosCardona_9.py $i >> DATOS_R.txt
done
python grafica_R.py DATOS_R.txt
