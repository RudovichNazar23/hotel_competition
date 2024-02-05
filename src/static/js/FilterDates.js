
const selectDates = document.getElementById("id_date_day");
const currentDate = new Date().getDate();

const filterDateExpression = (option) => option.value > currentDate; 

FilterOptions(selectDates, selectDates.options, filterDateExpression);
