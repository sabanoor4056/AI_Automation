document.addEventListener("DOMContentLoaded", function () {

    const sendButton = document.getElementById("sendButton");
    const chatInput = document.getElementById("chatInput");
    const chatMessages = document.getElementById("chatMessages");

    if (sendButton && chatInput && chatMessages) {

        sendButton.addEventListener("click", function () {

            const message = chatInput.value.trim();

            if (message === "") {
                return;
            }

            const userMessage = document.createElement("div");
            userMessage.className = "message user-message";

            userMessage.innerHTML = `
                <div class="message-content">
                    ${message}
                </div>
            `;

            chatMessages.appendChild(userMessage);

            chatInput.value = "";

            setTimeout(function () {

                const aiMessage = document.createElement("div");
                aiMessage.className = "message ai-message";

                aiMessage.innerHTML = `
                    <div class="message-content">
                        Thanks for your message. Our AI assistant
                        is processing your request.
                    </div>
                `;

                chatMessages.appendChild(aiMessage);

                chatMessages.scrollTop = chatMessages.scrollHeight;

            }, 700);

        });

        chatInput.addEventListener("keypress", function (event) {

            if (event.key === "Enter") {
                sendButton.click();
            }

        });
    }

    const addLeadBtn = document.getElementById("addLeadBtn");

    if (addLeadBtn) {

        addLeadBtn.addEventListener("click", function () {
            alert("Lead form will be added in the next step.");
        });

    }

    

});