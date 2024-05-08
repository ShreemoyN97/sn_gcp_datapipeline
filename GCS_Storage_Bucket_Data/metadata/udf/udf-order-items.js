function transform(line) {
    var values = line.split(',');
    var obj = new Object();

    obj.OrderItemId = values[0];
    obj.OrderId = values[1];
    obj.ProductPrice = parseFloat(values[2]);
    obj.Quantity = parseInt(values[3]);
    obj.DiscountRate = parseFloat(values[4]);

    return JSON.stringify(obj);
}
