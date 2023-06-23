CREATE FUNCTION calculate_order_total(order_id INT)
RETURNS DECIMAL(10,2)
BEGIN
  DECLARE total DECIMAL(10,2);
  SELECT SUM(price * quantity) INTO total FROM order_items WHERE order_id = order_id;
  SET total = total * (1 + tax_rate);
  RETURN total;
END;
