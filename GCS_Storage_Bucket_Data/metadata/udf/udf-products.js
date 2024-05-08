function transform(line) {
    var values = line.split(',');
    var obj = new Object();

    obj.ProductID = values[0];
    obj.ProductName = values[1];
    obj.Price = values[2];
    obj.CategoryID = values[3];

    return JSON.stringify(obj);
}
