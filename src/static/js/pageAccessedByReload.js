const pageAccessedByReload = (
    (window.performance.navigation && window.performance.navigation.type === 1) ||
        window.performance
        .getEntriesByType('navigation')
        .map((nav) => nav.type)
        .includes('reload')
);
if(pageAccessedByReload){
    document.getElementById("submit_button").click();
};

// document.onvisibilitychange = () => {
//     if(document.visibilityState === "hidden"){
//         console.log("Page was hidden");
//     };
// };