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
    if (document.getElementById('user_input').value !== '' && document.getElementById('language-select').value !== 'sela') {
        //receive user input
        const text = document.getElementById('user_input').value;
        fetch(`/process_user_input/?user_input=${encodeURIComponent(text)}`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('textToCopy').innerText = data.user_sent;
            })
            .catch(error => console.error('Error:', error));
        //restarts input field    
        document.getElementById('user_input').value = '';

        //receive language
        const selectedLanguage = document.getElementById('language-select').value;
        console.log('selected language: ', selectedLanguage);
        fetch(`/process_user_input/?language_selected=${encodeURIComponent(selectedLanguage)}`)
            .catch(error => console.error('Error:', error));

    } else{
        alert('Please enter text and select a language')
}};

var user_input = document.getElementById("user_input");

user_input.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
      event.preventDefault();
      document.getElementById("submit-button").click();
    }
  });
