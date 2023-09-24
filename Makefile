VENV_NAME = owo
owo:
	source /project/owo/bin/activate

stop_owo:
	source /project/owo/bin/deactivate

install:
	pip install -r requirements.txt