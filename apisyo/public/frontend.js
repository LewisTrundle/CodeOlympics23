const score = document.getElementById("scoreLabel");
const wordLabel = document.getElementById("wordsLabel");
console.log(wordLabel);
const options = document.getElementById("options");

function shuffle(array) {
    let currentIndex = array.length,  randomIndex;
  
    // While there remain elements to shuffle.
    while (currentIndex != 0) {
  
      // Pick a remaining element.
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;
  
      // And swap it with the current element.
      [array[currentIndex], array[randomIndex]] = [
        array[randomIndex], array[currentIndex]];
    }
  
    return array;
}


function getQuestion() {
    fetch("/quiz_question")
    .then(res => res.json())
    .then(res2 => {
        
        console.log(res2);
        wordLabel.innerHTML = res2.words
        const answers = shuffle([{"name": res2.correct.name[0], "correct": true}, {"name": res2.incorrect.name[0], "correct": true}]);
        const selection = document.createElement("form");
        answers.forEach((answer) => {
            const option = document.createElement("input");
            option.type = "radio";
            option.value = answer.name;
            option.text = answer.name;
            option.id = answer.name;
            option.name = "answer";
            const optionLabel = document.createElement("label");
            optionLabel.innerHTML = answer.name;
            optionLabel.for = answer.name;
            selection.appendChild(option);
            selection.appendChild(optionLabel);
            
            
        });
        const submitButton = document.createElement("input");
        submitButton.type = "Submit";
        selection.appendChild(submitButton);
        options.appendChild(selection);
        selection.onsubmit = (event) => {
            const answerButtons = document.getElementsByName("answer");
            for (var i = 0; i < answerButtons.length; i++) {
                if (answerButtons[i].checked && answers[i].correct) {
                    scoreLabel.innerHTML = Number(scoreLabel.innerHTML) + 1;
                }
                
            }
            getQuestion();
            return false;
        }
        

    })
}

getQuestion();


