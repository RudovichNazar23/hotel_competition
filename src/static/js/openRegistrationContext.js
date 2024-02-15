const dateFrom = document.getElementById("id_date_from");
const dateTo = document.getElementById("id_date_to");
const currentDate = new Date().getDate();
const submitButton = document.getElementById("submit_button");

const errorDivStyleAttrs = () => ["m-1", "p-1", "text-danger"];
const submitButtonStyleAttrs = () => ["disabled",];
const inputStyleAttrs = () => ["border-danger"];
