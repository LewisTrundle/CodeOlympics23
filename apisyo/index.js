const express = require("express");
const fs = require("fs").promises;
const router = express.Router();
const axios = require("axios");
const PORT = 8000;
const HOST = "0.0.0.0";
let dataFormatted = [];


const app = express();
app.use("/static", express.static("public"));
app.use(express.json());
const appdir = __dirname;

function formatData() {
    axios.get("https://restcountries.com/v3.1/all").then((response) => {
        const data = response.data;
        dataFormatted = []
        data.forEach((country) => {
            formatted = {"name": country.capital, "location": country.capitalInfo.latlng}
            dataFormatted.push(formatted);
        })  
    })

}

formatData();



app.get("/", (req, res) => {
    fs.readFile(`${appdir}/app.html`)
    .then(content => {
        res.setHeader("Content-Type", "text/html");
        res.writeHead(200);
        res.end(content);
        return;
    })
    .catch(err => {
        res.writeHead(404);
        res.end("SOMETHING WENT WRONG");
    })

    

});

app.get("/quiz_question", (req, res) => {
    let correct = dataFormatted[Math.floor(Math.random()*dataFormatted.length)];
    let incorrect = dataFormatted[Math.floor(Math.random()*dataFormatted.length)]
    console.log(correct);
    axios.get(`https://api.what3words.com/v3/convert-to-3wa?coordinates=${correct.location[0]},${correct.location[1]}&key=AAY46H1S`)
    .then((response2) => {
        console.log(response2.data.words);
        const output = JSON.stringify({
            "words": response2.data.words,
            "correct": correct,
            "incorrect": incorrect
            
        });
        res.setHeader("Content-Type", "application/json");
        res.writeHead(200);
        res.end(output);
        return;
    })
})

app.get("/funny", (req, res) => {
    fs.readFile(`${appdir}/index.html`)
    .then(content => {
        res.setHeader("Content-Type", "text/html");
        res.writeHead(200);
        res.end(content);
        return;
    })
    .catch(err => {
        res.writeHead(404);
        res.end("SOMETHING WENT WRONG");
    })

})

app.get("//public/icons/salad_dog.png", (req, res) => {
    fs.readFile(`${appdir}/salad_dog.png`)
    .then(content => {
        res.setHeader("Content-Type", "image/x-png");
        res.writeHead(200);
        res.end(content);
        return;
    })
})



const server = app.listen(PORT, HOST);

server.on('connection', function(socket) {
    console.log("A new connection was made by a client.");
    socket.setTimeout(30 * 1000); 
    // 30 second timeout. Change this as you see fit.
});

console.log(`running on http://${HOST}:${PORT}`);