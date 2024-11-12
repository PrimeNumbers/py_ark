# py_ark
All my python scripts that interact with the video game Ark: Survival Ascended on my behalf will be under this MIT license. \
My scripts are written in python, but depend on libraries that may contain other languages and dependencies. \
All the libraries and modules referenced have their own licenses. \
------------------------------------------------------------\
Ubuntu: 24.04.1 LTS \
Python: 3.12.3 \
venv: "snek" \
------------------------------------------------------------ \
(handy setup commands that I forget) \
#create a virtual environment in the current directory \
python3 -m venv snek

change the current directory to the snek/bin \
cd /home/prime/Desktop/snek/bin/

while in the snek/bin, activate the virtual environment\
source activate

deactivate the virtual environment\
deactivate

save a file with the current modules installed\
pip freeze > reqs.txt

read from a file and install the required modules\
pip install -r reqs.txt
