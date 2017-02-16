strtest: main.py display.py draw.py
	python main.py

clean:
	rm *.pyc
	rm *.png
	rm *.ppm

run: strtest
	
