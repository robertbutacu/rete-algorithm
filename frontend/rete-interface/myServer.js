let http = require("http");
let fs = require("fs");

let server = http.createServer((req, res) => {
    if (req.url === "/myJson") {
        res.writeHead(200, "Content-type: application/json");
        res.write(JSON.stringify({
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
        }));
        res.end();
    }
    else {
        let fileString = req.url.substr(1, req.url.length);
        if (fs.exists(fileString)) {
            let file = fs.createReadStream(fileString);
            file.pipe(res);
        }
        else {
            console.log(`File ${fileString} does not exist`);
        }
    }
});

server.listen(2323);
console.log("Server running");