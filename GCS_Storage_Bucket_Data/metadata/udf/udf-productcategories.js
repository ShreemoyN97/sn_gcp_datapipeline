function transform(line) {
    var values = line.split(',');
    var obj = new Object();

    obj.CategoryID = values[0];
    obj.CategoryName = values[1];

    return JSON.stringify(obj);
}
