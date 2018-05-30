function goToExamples() {
    document.getElementById("overlay").style.display = "none";
    window.location.href = "examplesPage.html";
  }
  
  function goToGeneratePage() {
    document.getElementById("overlay").style.display = "none";
    window.location.href = "createTreePage.html";
  }

  function generateTree() {
    clipsCode = document.getElementById("textareaValue").value.split("\n")
    var jsonResponse;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        jsonResponse = JSON.parse(this.responseText);
        var my_chart = new Treant(jsonResponse[0].graph);
        console.log(jsonResponse[0].graph)
        document.getElementById("activationText").innerText = jsonResponse[0].activations;
       
        let min = 0;
        let max = jsonResponse.length - 1;
        let count = min;
        let treeRefactor = currentIteration => {
        var my_chart = new Treant(jsonResponse[currentIteration].graph);
        document.getElementById("activationText").innerText =
          jsonResponse[currentIteration].activations;
          document.getElementById("clips_code").innerText =jsonResponse.text;
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
      }
    };
    xhttp.open("POST", "http://127.0.0.1:5000/clips-code", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send(JSON.stringify({"code": clipsCode }));
      
  }
