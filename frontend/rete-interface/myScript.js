// var fs = require('fs');
var simple_chart_config={
    "chart": {
        "container": "#tree-simple"
    },
    "nodeStructure": {
        "text": {
            "name": "Parent node"
        },
        "children": [
            {
                "text": {
                    "name": "primul copil"
                },
                "children": [
                    {
                        "text": {
                            "name": "primul copil"
                        }
                    },
                    {
                        "text": {
                            "name": "primul copil"
                        }
                    }
                ]
            },
            {
                "text": {
                    "name": "al doilea child"
                },
                "children": [
                    {
                        "text": {
                            "name": "primul copil"
                        }
                    },
                    {
                        "text": {
                            "name": "primul copil"
                        }
                    }
                ]
            },
            {
                "text": {
                    "name": "al 3-lea child"
                }
            },
            {
                "text": {
                    "name": "al 4-lea child"
                }
            }
        ]
    }
}

// fs.readFile('myJson.js', 'utf8', function (err, data) {
//   if (err) throw err;
//   simple_chart_config = JSON.parse(data);
// });
fetch("/myJson")
    .then((result) => {
        console.log(result);
        JSON.parse(result);
    })
    .then((result) => {
        console.log(result);        
    })

var my_chart = new Treant(simple_chart_config);
