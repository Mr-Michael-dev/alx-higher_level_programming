/*
 * fetches and prints how to say “Hello” depending on the language
 * The language code will be the value entered in the tag
 * INPUT#language_code (ex: es, fr, en etc.)
 *
 * The translation must be fetched when the user clicks on INPUT#btn_translate
 *
 * The translation of “Hello” must be displayed in the HTML tag DIV#hello
 */

$(document).ready(function() {
    $('#btn_translate').click(function() {
        var languageCode = $('#language_code').val();

        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/',
            method: 'GET',
            data: { lang: languageCode },
            success: function(data) {
                $('#hello').text(data.hello);
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
            }
        });
    });
});
