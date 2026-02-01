const API_URL = "http://127.0.0.1:8000";

async function process(action) {
    const message = document.getElementById("inputMessage").value;
    const type = document.getElementById("encodingType").value;
    const status = document.getElementById("status");
    const output = document.getElementById("outputMessage");

    if (!message.trim()) {
        status.innerText = "⚠ Please enter a message.";
        return;
    }

    status.innerText = "⏳ Processing...";
    output.value = "";

    try {
        const response = await fetch(`${API_URL}/${action}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message, type })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail);
        }

        output.value = data.result;
        status.innerText = "✅ Success!";
    } catch (error) {
        status.innerText = "❌ " + error.message;
    }
}

function copyResult() {
    const output = document.getElementById("outputMessage");
    if (!output.value) return;

    output.select();
    document.execCommand("copy");
    document.getElementById("status").innerText = "📋 Copied to clipboard!";
}
