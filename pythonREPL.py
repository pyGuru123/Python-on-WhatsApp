import sys
from io import StringIO
import contextlib

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
