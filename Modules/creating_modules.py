# you can import different functions as objects
from Modules.ecommerce.shopping.sales import calc_shipping, calc_tax

# you can import the entire module as an object
import Modules.ecommerce.shopping.sales as sales

# you can call the different methods
sales.calc_shipping()
# or, if imported separately, call them this way
calc_shipping()
calc_tax()
