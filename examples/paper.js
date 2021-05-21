var e = new Shape.Ellipse({
    center: [105, 77],
    radius: [37, 62],
    strokeColor: 'black'
});

var r = new Shape.Rectangle({
    point: [43, 190],
    size: [125, 92],
    fillColor: 'blue'
});

var t = new PointText({
    content: 'centered text',
});
t.point = r.bounds.center - t.bounds.size / 2

var a = new Path.Line({
    from: r.bounds.topCenter,
    to: e.bounds.bottomCenter,
    strokeColor: 'black'
});

new Path.RegularPolygon({
    center: e.bounds.bottomCenter + [0, 8], 
    sides: 3,
    radius: 8,
    fillColor: 'black'
});

var t = new PointText({
    content: 'arrow',
    point = a.bounds.center + 8 
});
