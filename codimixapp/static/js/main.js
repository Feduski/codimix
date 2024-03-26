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
    const user_input = document.getElementById('user_input').value;
    const selected_language = document.getElementById('language-select').value;

    if (user_input !== '' && selected_language !== 'sela') {
        fetch(`/process_user_input/?user_input=${encodeURIComponent(user_input)}&selected_language=${encodeURIComponent(selected_language)}`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('textToCopy').innerText = data.user_sent;
            })
            .catch(error => console.error('Error:', error));

        document.getElementById('user_input').value = '';
    } else {
        alert('Please enter text and select a language');
    }
}


var user_input = document.getElementById("user_input");

user_input.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
      event.preventDefault();
      document.getElementById("submit-button").click();
    }
  });
