# Drawing Shapes with p5.js

p5.js is a JavaScript library for creative coding. You can embed live, interactive sketches directly into MkDocs pages.

## A Simple Sketch

Here's a basic sketch that draws a rectangle and an ellipse:

<div id="sketch-1" data-sketch></div>

<script type="text/p5js" data-target="sketch-1">
function setup() {
  createCanvas(300, 200);
}

function draw() {
  background(220);

  // Draw a rectangle
  fill(0, 100, 200);
  rect(50, 50, 100, 80);

  // Draw an ellipse
  fill(200, 50, 50);
  ellipse(200, 100, 60, 80);
}
</script>

## Interactive Example

Move your mouse over the canvas to control the circle:

<div id="sketch-2" data-sketch></div>

<script type="text/p5js" data-target="sketch-2">
function setup() {
  createCanvas(300, 200);
}

function draw() {
  background(220);
  fill(100, 150, 0);
  ellipse(mouseX, mouseY, 40, 40);
}
</script>

## How It Works

Each sketch needs two things:

1. A **container div** with `id` and `data-sketch`
2. A **`<script type="text/p5js">`** block with `data-target` pointing to that div's id

The loader script (in `extra.html`) finds all these pairs and boots them using [p5.js instance mode](https://github.com/processing/p5.js/wiki/Instance-mode), which lets you run multiple sketches on the same page without conflicts.

---

<!-- p5.js loader — loads the library and boots all sketches -->
<script>
(function () {
  var loaded = window._p5Ready;
  if (!loaded) {
    var s = document.createElement('script');
    s.src = 'https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.4/p5.min.js';
    s.onload = boot;
    document.head.appendChild(s);
  } else {
    boot();
  }

  function boot() {
    window._p5Ready = true;
    document.querySelectorAll('script[type="text/p5js"]').forEach(function (tag) {
      var targetId = tag.getAttribute('data-target');
      var container = document.getElementById(targetId);
      if (!container) return;

      var sketch = {};
      new Function(tag.textContent + '; return { setup: setup, draw: draw };').call(sketch);
      new p5(sketch, container);
    });
  }
})();
</script>
