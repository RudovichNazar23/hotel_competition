class BaseFileFieldHandler{
    handleEvent(event){
        if(!event.target.value){
            return;
        }
        this.validateFieldProperty(event);
    }

    validateFieldProperty(event){
        return event.target;
    }
}

class CheckFileIsEmptyHandler extends BaseFileFieldHandler {
    validateFieldProperty(event){
        let file_size = event.target.files[0].size / 1024;

        if(file_size <= 0){
            AddFieldAttributes(event.target, ["invalid_field",]);
            AddFieldAttributes(event.target.nextElementSibling, ["p-2", "m-2", "text-danger"],  "Ten plik jest pusty");
        }
    }
}

class CheckFileSizeHandler extends BaseFileFieldHandler {
    validateFieldProperty(event){
        const max_size = 10000;
        let file_size = event.target.files[0].size / 1024;

         if(file_size > max_size){
            AddFieldAttributes(event.target, ["invalid_field",]);
            AddFieldAttributes(event.target.nextElementSibling, ["p-2", "m-2", "text-danger"],  "Ten plik jest za duży");
         }
    }
}

class CheckFileFormatHandler extends BaseFileFieldHandler {
    validateFieldProperty(event){
        const allowed_file_formats = ["pdf", "jpg", "jpeg", "png"];
        const file_format = event.target.files[0].name.split(".")[1];

        if(!allowed_file_formats.includes(file_format)){
            AddFieldAttributes(event.target, ["invalid_field",]);
            AddFieldAttributes(event.target.nextElementSibling, ["p-2", "m-2", "text-danger"],  "Format pliku nie jest dozwolony");
        }
    }
}

let file_inputs = document.body.querySelectorAll("input[type=file]");

for(file_input of file_inputs){
    file_input.addEventListener("blur", new CheckFileIsEmptyHandler());
    file_input.addEventListener("blur", new CheckFileSizeHandler());
    file_input.addEventListener("blur", new CheckFileFormatHandler());
};
