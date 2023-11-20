const accountUUID = 'b8e146eb-caec-4a00-a8b7-79ec02fe7e0b';

async function getMessages(conversationUUID) {
    let url = new URL(`${location.protocol}//${location.host}/get_messages`);
    url.searchParams.set('conversation_uuid', conversationUUID);
    const response = await fetch(url);
    const data = await response.json();

    // change html with data
}

async function sendMessage(conversationUUID, message) {
    let url = new URL(`${location.protocol}//${location.host}/chat`);
    let formData = new FormData();
    formData.append('uuid', accountUUID);
    formData.append('conversation_uuid', conversationUUID);
    formData.append('message', message);
    const response = await fetch(url, {
        method: 'POST',
        body: formData
    });

    // add message to html
}

async function startConversation(chosenUserUUID) {
    let url = new URL(`${location.protocol}//${location.host}/study`);
    let formData = new FormData();
    formData.append('uuid', accountUUID);
    formData.append('chosen_uuid', chosenUserUUID);
    const response = await fetch(url, {
        method: 'POST',
        body: formData
    });

    // switch to message page
}

async function getConversations() {
    let url = new URL(`${location.protocol}//${location.host}/get_conversations`);
    url.searchParams.append('uuid', accountUUID);
    const response = await fetch(url);
    const data = await response.json();

    // add conversations to html
}

async function getEntries() {
    let url = new URL(`http://127.0.0.1:8000/list/`);
    url.searchParams.append('page', 1);
    const response = await fetch(url);
    const data = await response.json();

    return data;
}

window.addEventListener('DOMContentLoaded', async function() {
    let element = document.getElementById('entries-list');
    const entries = await getEntries();
    for (let i = 0; i < entries.length; i++) {
        let link = document.createElement('a');
        link.className = 'button';
        link.href = 'conversations.html';
        link.innerHTML = `<span class="button_text">${entries[i].username}</span>`;
        element.appendChild(link);
        let greetings = document.createElement('div');
        greetings.className = 'greetings';
        greetings.innerHTML = `<p>Subject: ${entries[i].subject}</p><br><p>Location: ${entries[i].location}</p>`;
        element.append(greetings);
    }
});

