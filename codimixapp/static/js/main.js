function copyToClipboard() {
    var copyText = document.getElementById("textToCopy");

    var range = document.createRange();
    range.selectNode(copyText);
    window.getSelection().addRange(range);

    try {
        var successful = document.execCommand('copy');
        var msg = successful ? 'successful' : 'unsuccessful';
        alert('Text copied to clipboard')
        console.log('Copy command was ' + msg);
    } catch (err) {
        console.log('Oops, unable to copy');
    }

    window.getSelection().removeAllRanges();
}

document.getElementById('submit-button').addEventListener('click', input_to_code);

function input_to_code() {
    console.log('Button clicked, function called')
    if (document.getElementById('user_input').value !== '') {
        const text = document.getElementById('user_input').value;
        fetch(`/process_user_input/?user_input=${encodeURIComponent(text)}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('textToCopy').innerText = data.user_sent;
        })
        .catch(error => console.error('Error:', error));
        console.log('Function finished')
        document.getElementById('user_input').value = '';
}};

var user_input = document.getElementById("user_input");

user_input.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
      event.preventDefault();
      document.getElementById("submit-button").click();
      input_to_code();
    }
  });