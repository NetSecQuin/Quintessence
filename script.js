document.addEventListener("DOMContentLoaded", function() {
    // Get references to the red and blue pill buttons
    var redPillButton = document.getElementById("red-pill");
    var bluePillButton = document.getElementById("blue-pill");

    // Add click event listeners to the buttons
    redPillButton.addEventListener("click", function() {
        window.location.href = "https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/BlueLanding.md";
    });

    bluePillButton.addEventListener("click", function() {
        window.location.href = "https://github.com/NetSecQuin/Quintessence/blob/main/Red%20Pages/RedLanding.md";
    });
});
