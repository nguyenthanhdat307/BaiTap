import os
env_vars = os.environ
for key, value in env_vars.items():
   print('{}: {}'.format(key, value))