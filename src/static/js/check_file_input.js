function checkFileFormat(event){
    if(!event.target.value){
        return;
    };
    let file_format = event.target.files[0].name.split(".")[1];
    let file_formats = ["pdf", "jpg", "png", "jpeg"];
    if(!file_formats.includes(file_format)){
        AddFieldAttributes(event.target, ["invalid_field",]);
        AddFieldAttributes(event.target.nextElementSibling, ["p-2", "m-2", "text-danger"],  "Incorrect file format");
    }
};

function checkFileIsEmpty(event){
    if(!event.target.value){
        return;
    }
    let file = event.target.files[0];
    if(!file.size){
        AddFieldAttributes(event.target, ["invalid_field",]);
        AddFieldAttributes(event.target.nextElementSibling, ["p-2", "m-2", "text-danger"],  "File is empty");
    }
};

function CheckFileSize(event){
    if(!event.target.value){
        return;
    }
    const max_size = 10000;
    let file_size = event.target.files[0].size / 1024;

    if(file_size > max_size){
        AddFieldAttributes(event.target, ["invalid_field",]);
        AddFieldAttributes(event.target.nextElementSibling, ["p-2", "m-2", "text-danger"],  "File is too big");
    }
};


let file_inputs = document.body.querySelectorAll("input[type=file]");

for(let file_input of file_inputs){
    file_input.addEventListener("blur", checkFileFormat);
    file_input.addEventListener("blur", checkFileIsEmpty);
    file_input.addEventListener("blur", CheckFileSize);
};
