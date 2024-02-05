const currentMonth = new Date().getMonth() + 1;
const selectMonths = document.getElementById("id_date_month");

const filterMonthExpression = (option) => option.value >= currentMonth;

FilterOptions(selectMonths, selectMonths.options, filterMonthExpression);
