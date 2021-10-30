import sys
import contextlib
import subprocess
from io import StringIO

@contextlib.contextmanager
def stdoutIO(stdout=None):
	old = sys.stdout
	if stdout is None:
		stdout = StringIO()
	sys.stdout = stdout
	yield stdout
	sys.stdout = old

def execute_python(code):
	with stdoutIO() as c:
		try:
			exec(code)
		except:
			print("Something wrong with the code")
	return c.getvalue()

def install_package(package):
	try:
		subprocess.check_call([sys.executable, "-m", "pip", "install", package])
		return f'{package} installed successfully'
	except:
		return 'cannot install this package'