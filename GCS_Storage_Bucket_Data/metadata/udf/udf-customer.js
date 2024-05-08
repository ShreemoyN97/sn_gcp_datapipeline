function transform(line) {
    var values = line.split(',');
    var obj = new Object();

    obj.CustomerID = values[0];
    obj.Email = values[1];
    obj.FirstName = values[2];
    obj.LastName = values[3];
    obj.Password = values[4];
    obj.Segment = values[5];
    obj.Street = values[6];
    obj.City = values[7];
    obj.State = values[8];
    obj.Country = values[9];
    obj.Zipcode = values[10];

    return JSON.stringify(obj);
}
