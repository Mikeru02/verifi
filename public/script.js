hardcodeCheckButton = document.getElementById("check-hardcode");
hardcodeCheckButton.addEventListener("click", async function(){
    const titleValue = document.getElementById("title").value;
    const contentValue = document.getElementById("input-art").value;
    const payload = {
        "title": titleValue,
        "article": contentValue
    }
    const response = await axios.post("/hardcode", payload)
    console.log(response)
})

urlCheckButton = document.getElementById("check-url");
urlCheckButton.addEventListener("click", async function(){
    const urlValue = document.getElementById("url").value
    const payload = {
        "url": urlValue
    };
    const response = await axios.post("/url", payload);
    console.log(response)
})