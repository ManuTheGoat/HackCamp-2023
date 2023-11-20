document.getElementById('send-message').addEventListener('click', function() {
    if (document.getElementById('mes').value === '') {
        return;
    }
    const element = document.getElementById('message-container');
    let p1 = document.createElement('p');
    p1.innerText = 'From You:';
    element.appendChild(p1);
    let p2 = document.createElement('p');
    p2.innerText = document.getElementById('mes').value;
    element.appendChild(p2);
    let br = document.createElement('br');
    element.appendChild(br);
    document.getElementById('mes').value = '';
});
