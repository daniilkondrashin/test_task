import os
env_var_1 = os.getenv('ENV_VAR_1', 'Не установлено')
env_var_2 = os.getenv('ENV_VAR_2', 'Не установлено')
print(env_var_1, env_var_2, sep=" | ")