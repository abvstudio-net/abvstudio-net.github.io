# Drawing Shapes with p5.js

p5.js is a JavaScript library for creative coding. You can embed live, interactive sketches directly into MkDocs pages.

## A Simple Sketch

<div id="sketch-1"></div>

<script>
  function simpleSketch(p) {
    p.setup = function() {
      p.createCanvas(300, 200);
    };
    p.draw = function() {
      p.background(220);
      p.fill(0, 100, 200);
      p.rect(50, 50, 100, 80);
      p.fill(200, 50, 50);
      p.ellipse(200, 100, 60, 80);
    };
  }
  new p5(simpleSketch, 'sketch-1');
</script>

## Interactive Example

<div id="sketch-2"></div>

<script>
  function mouseSketch(p) {
    p.setup = function() {
      p.createCanvas(300, 200);
    };
    p.draw = function() {
      p.background(220);
      p.fill(100, 150, 0);
      p.ellipse(p.mouseX, p.mouseY, 40, 40);
    };
  }
  new p5(mouseSketch, 'sketch-2');
</script>

## How It Works

Each sketch uses [p5.js instance mode](https://github.com/processing/p5.js/wiki/Instance-mode) so multiple independent sketches can coexist on the same page (important with `navigation.instant`).

p5.js is loaded globally via `extra_javascript` in `mkdocs.yml`. Just define your sketch function and call `new p5(sketchFn, 'container-id')`.