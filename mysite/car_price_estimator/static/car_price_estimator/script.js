let modelData;

fetch("/static/car_price_estimator/sample.json")
    .then(Response => Response.json())
    .then(data => {
        modelData = data;

        var markaSelect = document.getElementById('auto_make_id');

        var options = markaSelect.options;
        markaArray = [];

        // console.log(options);

        for (var i = 0; i < options.length; i++) {
            var markaName = options[i].text;
            var list = modelData[markaName];
            if (list != undefined) {
                markaArray.push(markaName);
            }
            // console.log(markaName);
        }
        markaSelect.innerHTML = "";


        markaSelect.appendChild(chooseOption());
        for (var i = 1; i <= markaArray.length; i++) {
            var option = document.createElement("option");
            option.text = markaArray[i - 1];
            option.value = `${i}->${markaArray[i - 1]}`;
            markaSelect.appendChild(option);
        }

    });


function chooseOption() {
    let option = document.createElement("option");
    option.text = "Choose";
    option.value = 0;
    return option;
}


function markaChanges(chosen) {
    let modelSelect = document.getElementById('auto_model_id');
    modelSelect.innerHTML = "";

    let correspondingModels = modelData[chosen];

    modelSelect.appendChild(chooseOption());
    for (var i = 1; i <= correspondingModels.length; i++) {
        var option = document.createElement("option");
        option.text = correspondingModels[i - 1];
        option.value = `${i}->${correspondingModels[i - 1]}`;
        modelSelect.appendChild(option);
    }
}



// console.log(markaSelect);
