hardcodeCheckButton = document.getElementById("check-hardcode");
hardcodeCheckButton.addEventListener("click", async function(){
    const titleValue = document.getElementById("title").value;
    const contentValue = document.getElementById("input-art").value;
    const payload = {
        "title": titleValue,
        "article": contentValue
    }
    const response = await axios.post("/hardcode", payload);
    dePopulateResultContainer();
    populateResultContainer(response.data);
})

urlCheckButton = document.getElementById("check-url");
urlCheckButton.addEventListener("click", async function(){
    const urlValue = document.getElementById("url").value
    const payload = {
        "url": urlValue
    };
    const response = await axios.post("/url", payload);
    console.log(response.data)
    dePopulateResultContainer();
    populateResultContainer(response.data);
});

const imageCheckButton = document.getElementById("check-img");
imageCheckButton.addEventListener("click", async function(){
    const inputImage = document.getElementById("images");
    const file = inputImage.files[0];

    if (file) {
        console.log("File name:", file.name);
        console.log("File size:", file.size, "bytes");
        console.log("File type:", file.type);
        const payload = {
            "file_name": file.name
        }
        const response = await axios.post("/image", payload)
        dePopulateResultContainer();
        populateResultContainer(response.data);
    } else {
        console.log("No file selected.");
    }
})

function populateResultContainer(responseData){
    const resultContainer = document.getElementById("results-container");
    const predictionContainer = document.createElement("div");
    predictionContainer.className = "results-cards";
    predictionContainer.id = "prediction";
    predictionContainer.innerHTML = `
        <h3>Model Prediction</h3>
        <h3>${responseData.prediction}</h3>
    `;

    if (responseData.prediction === "True"){
        predictionContainer.style.border = "4px solid green";
    } else{
        predictionContainer.style.border = "4px solid red";
    }

    const confidenceContainer = document.createElement("div");
    confidenceContainer.className = "results-cards";
    confidenceContainer.innerHTML = `
        <h3>Confidence Percentage</h3>
        <h3>${responseData.confidence.toFixed(2)}%</h3>
    `;

    if (responseData.confidence > 70) {
        confidenceContainer.style.border = "4px solid green";
    } else if (responseData.confidence >= 40) {
        confidenceContainer.style.border = "4px solid yellow";
    } else {
        confidenceContainer.style.border = "4px solid red";
    }

    const scoresContainer = document.createElement("div");
    scoresContainer.className = "results-cards";
    scoresContainer.innerHTML = `
        <h3>Log Scores Distribution</h3>
        <h3>True = ${responseData.scores.True.toFixed(2)} || False = ${responseData.scores.False.toFixed(2)}</h3>
    `;

    scoresContainer.style.border = "4px solid white";

    resultContainer.appendChild(predictionContainer);
    resultContainer.appendChild(confidenceContainer);
    resultContainer.appendChild(scoresContainer);
}

function dePopulateResultContainer(){
    const resultContainer = document.getElementById("results-container");
    resultContainer.innerHTML = "";
}