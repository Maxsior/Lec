function setup() {
    createCanvas(300, 300);
}

function draw() {
    stroke(0, 0, 0);
    strokeWeight(1);
    ellipseMode(RADIUS);
    fill("none");
    ellipse(105, 77, 37, 62);

    strokeWeight(0);
    fill("blue");
    rect(43, 190, 125, 92);

    fill("black");
    textAlign(CENTER, CENTER);
    text("centered text", 43, 190, 125, 92);

    strokeWeight(1);
    line(105, 140, 105, 190);

    strokeWeight(0);
    text("arrow", 130, 160);

    triangle(105, 140, 100, 150, 110, 150);
}
