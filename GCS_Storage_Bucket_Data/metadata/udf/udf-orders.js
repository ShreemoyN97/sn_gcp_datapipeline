function transform(line) {
    var values = line.split(',');
    var obj = new Object();

    obj.OrderId = values[0];
    obj.CustomerId = values[1];
    obj.OrderStatus = values[2];
    obj.SalesPerCustomer = parseFloat(values[3]);
    obj.OrderProfitPerOrder = parseFloat(values[4]);
    obj.ShippingMode = values[5];

    return JSON.stringify(obj);
}
