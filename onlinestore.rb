# A program that implements a simple online store

class Product
  attr_accessor :name, :price

  def initialize(name, price)
    @name = name
    @price = price
  end
end

class Cart
  attr_accessor :items

  def initialize
    @items = []
  end

  def add_item(product)
    @items << product
  end

  def remove_item(product)
    @items.delete(product)
  end

  def total_cost
    total = 0
    @items.each { |item| total += item.price }
    total
  end
end

class Order
  attr_accessor :cart, :status

  def initialize(cart)
    @cart = cart
    @status = :pending
  end

  def submit
    if @cart.items.empty?
      puts "Cannot submit an empty cart"
    else
      @status = :submitted
      puts "Order submitted, total cost: $#{@cart.total_cost}"
    end
  end
end

# create products
book = Product.new("Ruby Programming", 39.99)
shirt = Product.new("Ruby T-Shirt", 19.99)

# create cart and add items
cart = Cart.new
cart.add_item(book)
cart.add_item(shirt)

# create order and submit
order = Order.new(cart)
order.submit

# Output: "Order submitted, total cost: $59.98"

