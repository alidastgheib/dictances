from example_utils import generate_example_dicts
from distances import mse

a, b = generate_example_dicts()

print(mse(a,b))
# >>> 260954.64260908752