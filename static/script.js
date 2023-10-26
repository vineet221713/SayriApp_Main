$(document).ready(function () {
    const promptInput = $("#prompt");
    const generateButton = $("#generate-button");
    const output = $("#output");

    generateButton.on("click", function () {
        const prompt = promptInput.val();
        if (prompt.trim() === "") {
            output.text("Please enter a prompt.");
            return;
        }

        $.post("/generate_sayri", { prompt: prompt }, function (data) {
            if ("error" in data) {
                output.text("Error: " + data.error);
            } else {
                output.text(data.generated_sayri);
            }
        });
    });
});
