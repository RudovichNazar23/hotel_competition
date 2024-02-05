function FilterOptions(select_element, optionsCollection, filter_expression){
    let optionsArray = Array.from(optionsCollection);

    let filtered_options = optionsArray.filter(filter_expression);

    select_element.innerHTML = "";

    for(let i of filtered_options){
        select_element.append(i);
    }
}
