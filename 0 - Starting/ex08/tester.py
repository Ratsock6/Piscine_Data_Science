from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for _ in ft_tqdm(range(333)):
    sleep(0.005)
print()
for _ in tqdm(range(333)):
    sleep(0.005)
print()