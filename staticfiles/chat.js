var REST_SEND_URL = 'http://' + window.location.host + '/send/';
var REST_HISTORY_URL = 'http://' + window.location.host + '/history/';
var username = $('#username').text();



// Send message
$('form').submit(function() {
    var text = $('#text').val();
    $.ajax({
        type: 'GET',
        url: REST_SEND_URL,
        data: {'text': text, 'sender': username},
        dataType: 'text',
        cache: false,
        success: onDelivered
    });
    return false;  // return false to prevent page reload on font submit
});

function onDelivered(response) {
    $('#text').val('').focus();
    scrollHistoryDown();
}

function scrollHistoryDown() {
    var textarea = document.getElementById('textarea_id');
setInterval(function(){
    textarea.scrollTop = textarea.scrollHeight;
}, 1000);
}

function loadHistory(){
    $.ajax({
        type: 'GET',
        url: REST_HISTORY_URL,
        dataType: 'text',
        cache: false,
        success: function (response) {
            // put messages into '.history'
            $('.history').html(response);
        }
    });
}

// auto load every 2 sec
function auto_load() {
    loadHistory();
    setTimeout(auto_load, 2000);
}

window.onload = function(){
    loadHistory();
    $('#text').focus();
    setTimeout(scrollHistoryDown, 200);
    setTimeout(auto_load, 2000);
};

