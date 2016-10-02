from datetime import datetime
from dateutil.relativedelta import relativedelta

def now():
	return datetime.now()

def diffTime(t_start, t_end):
	t_diff = relativedelta(t_start, t_end)
	return '{h}h {m}m {s}s'.format(h = t_diff.hours, m = t_diff.minutes, s = t_diff.seconds)
