var app = angular.module('LRLandingPage', ['reCAPTCHA'])

app.config(function(reCAPTCHAProvider) {
    // required: please use your own key :)
    reCAPTCHAProvider.setPublicKey('6LeSyhITAAAAAO0NUAXOGJhFCl0F9l1oHXE8CmNk');

    // optional: gets passed into the Recaptcha.create call
    reCAPTCHAProvider.setOptions({
        theme: 'clean'
    });
})

app.config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});