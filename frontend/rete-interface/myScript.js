var jsonResponse;
function loadJSON(callback) {
  var xobj = new XMLHttpRequest();
  xobj.overrideMimeType("application/json");
  xobj.open("GET", "treeJson.json", true);
  xobj.onreadystatechange = function() {
    if (xobj.readyState == 4) {
      callback(xobj.responseText);
    }
  };
  xobj.send(null);
}
loadJSON(function(response) {
  let initializeNewJson = () => {
    jsonResponse = JSON.parse(response);
    var my_chart = new Treant(jsonResponse.states[0].graph);

    document.getElementById("activation_text").innerText =
      jsonResponse.states[0].activations;

    if (document.getElementById("clips_code") != null) {
      document.getElementById("clips_code").innerText =
        jsonResponse.states[0].code;
    }
  };

  initializeNewJson();

  let min = 0;
  let max = jsonResponse.states.length - 1;
  let count = min;

  let treeRefactor = currentIteration => {
    var my_chart = new Treant(jsonResponse.states[currentIteration].graph);
    document.getElementById("activation_text").innerText =
      jsonResponse.states[currentIteration].activations;

    if (document.getElementById("clips_code") != null) {
      document.getElementById("clips_code").innerText =
        jsonResponse.states[0].code;
    }
  };

  document.getElementById("previousIteration").onclick = function() {
    if (count > min) {
      count--;
      treeRefactor(count);
    }
    console.log(count);
  };

  document.getElementById("nextIteration").onclick = function() {
    if (count < max) {
      count++;
      treeRefactor(count);
    }
    console.log(count);
  };

  document.getElementById("buton_exemplu_1").onclick = function() {
    initializeNewJson();
  };
  document.getElementById("buton_exemplu_2").onclick = function() {
    initializeNewJson();
  };
  document.getElementById("buton_exemplu_3").onclick = function() {
    initializeNewJson();
  };
  document.getElementById("buton_exemplu_4").onclick = function() {
    initializeNewJson();
  };
});

function goToExamples() {
  document.getElementById("overlay").style.display = "none";
  window.location.href = "examplesPage.html";
}

function goToGeneratePage() {
  document.getElementById("overlay").style.display = "none";
  window.location.href = "createTreePage.html";
}
