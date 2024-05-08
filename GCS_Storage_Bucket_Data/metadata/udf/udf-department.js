function transform(line) {
    var values = line.split(',');
    var obj = new Object();

    obj.DepartmentID = values[0];
    obj.DepartmentName = values[1];

    return JSON.stringify(obj);
}
