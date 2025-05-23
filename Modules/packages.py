# this method is good for cleaner look
import Modules.ecommerce.shopping.sales as ec

# this method can get messy
from Modules.ecommerce.shopping.sales import calc_tax, calc_shipping

# another clean method. allows 'sales.' method
from Modules.ecommerce.shopping import sales

sales.calc_shipping()

calc_tax()

ec.calc_tax()
