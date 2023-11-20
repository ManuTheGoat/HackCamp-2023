const accountUUID = '';

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
    let url = new URL(`${location.protocol}//${location.host}/list`);
    url.searchParams.append('page', 1);
    const response = await fetch(url);
    const data = await response.json();

    // add entries to html
}


